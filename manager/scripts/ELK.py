from elasticsearch import Elasticsearch
from manager.scripts.useful import get_nday_list,get_day_nday_ago
import numpy as np
webinfo={'猫扑论坛':'mop','天涯BBS':'tianya_bbs','人民网论坛':'bbs_people','新华网论坛':'news_bbs','豆瓣小组':'douban_group'}
def getelkconnect():
    es = Elasticsearch([{'host': '192.168.100.201', 'port': 9200}])
    return es
def change(list):
    pass
def querdayspeed(spidername,time):
    es = Elasticsearch([{'host': '192.168.100.201', 'port': 9200}])
    body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "regexp": {
                            "page_speed": '[0-9].+'
                        }
                    },
                    {
                        "wildcard": {
                            "source": '*' + spidername + '*'
                        }
                    },
                    {
                        "range": {
                            "log_time": {
                                "gte": time + "T00:00:00",
                                "lt": time + "T23:59:59"
                            }
                        }
                    }
                ]
            }

        },
        # "from": 0,
        "size": 5000,
        "sort": {"log_time": {"order": "desc"}}
        # "aggs": {}
    }
    querydata = es.search(index='2018spiderlogs', body=body, _source='log_time,page_speed,item_speed,source')
    if querydata['hits']['total'] == 0:
        # pagesum = itemsum=0
        pageavg = itemavg = 0
    else:
        pagesum = itemsum = 0
        for data in querydata['hits']['hits']:
            pagesum = pagesum + int(data['_source']["page_speed"])
            itemsum = itemsum + int(data['_source']["item_speed"])
        pageavg = pagesum / querydata['hits']['total']
        itemavg = itemsum / querydata['hits']['total']

    # print(pagesum,itemsum)
    # print(int(pageavg), int(itemavg))
    return int(pageavg), int(itemavg)
def queryweekspeed(web,time):

    spidername = webinfo[web]
    timelist = get_nday_list(time,6)
    timelist.append(time)
    # timelist = sorted(timelist,reverse=True)
    # print(spidername, time)
    # print(timelist)
    pagelist  = []
    itemlist =  []
    for day in timelist:
        page,item = querdayspeed(spidername,day)
        pagelist.append(page)
        itemlist.append(item)
    return pagelist,itemlist,timelist
def querySpiderSpeedBynIterval(spidername,time,interval):
    es = Elasticsearch([{'host': '192.168.100.201', 'port': 9200}])
    if interval == 1:
        gte = time+ "T00:00:00"
    else:
        gte =get_day_nday_ago(time,interval-1)+ "T00:00:00"
    # print(spidername,gte,interval)
    body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "regexp": {
                            "page_speed": '[0-9].+'
                        }
                    },
                    {
                        "wildcard": {
                            "source": '*' + spidername + '*'
                        }
                    },
                    {
                        "range": {
                            "log_time": {
                                "gte": gte,
                                "lt": time + "T23:59:59"
                            }
                        }
                    }


                ]
            }
            # "regexp": {
            #     "source": '(.)+bbs'
            # }

        },
        # "from": 0,
        "size": 5000,
        "sort": {"log_time": {"order": "desc"}}
        # "aggs": {}
    }

    a = es.search(index='2018spiderlogs', body=body, _source='log_time,page_speed,item_speed,source')
    pagelist = []
    itemlist = []
    daypagelist = []
    nightpagelist = []
    dayitemlist = []
    nightitemlist = []
    # print(len(a['hits']['hits']))
    for i in a['hits']['hits']:
        pagelist.append(int(i['_source']['page_speed']))
        itemlist.append(int(i['_source']['item_speed']))

        time = i['_source']['log_time']
        hour = time.split('T')[-1]
        if hour < '08' or hour > '20':
            nightpagelist.append(int(i['_source']['page_speed']))
            nightitemlist.append(int(i['_source']['item_speed']))
        else:
            daypagelist.append(int(i['_source']['page_speed']))
            dayitemlist.append(int(i['_source']['item_speed']))
    # print(len(pagelist), max(pagelist), min(pagelist), pagelist)
    # print(len(itemlist), max(itemlist), min(itemlist), itemlist)
    if not pagelist or not itemlist:
        pagelist = itemlist =[0,0]
    if not daypagelist or not dayitemlist:
        daypagelist = dayitemlist =[0,0]
    if not nightitemlist or not nightpagelist:
        nightitemlist = nightpagelist = [0,0]
    nplist = np.array([pagelist, itemlist])
    nightlist = np.array([nightpagelist, nightitemlist])
    daylist = np.array([daypagelist, dayitemlist])
    # print(len(nplist),len(nightlist),len(daylist))
    avg1 = np.mean(nplist, axis=1)
    avg2 = np.mean(daylist, axis=1)
    avg3 = np.mean(nightlist, axis=1)
       # print(avg1, avg2, avg3)
    dic = {}

    dic['name'] = spidername
    dic['highpage'] = max(pagelist)
    dic['lowpage'] = min(pagelist)
    dic['highitem'] = max(itemlist)
    dic['lowitem'] = min(itemlist)
    dic['avgpage'] = int(avg1[0])
    dic['avgitem'] = int(avg1[1])
    dic['daypage'] = int(avg3[0])
    dic['dayitem'] = int(avg3[1])
    dic['nightpage'] = int(avg2[0])
    dic['nightitem'] = int(avg2[1])
    # print(dic)
    return dic
def getspiderspeed(interval):
    data = []
    for i in webinfo.values():
        data.append(querySpiderSpeedBynIterval(i,'2017-05-22',interval))
    return data
def queryerrorbyday(spidername,day):
    es = Elasticsearch([{'host': '192.168.100.201', 'port': 9200}])
    body1 = {
        "query": {
            "bool": {
                "must": [

                    {
                        "wildcard": {
                            "source": '*' + spidername + '*'
                        }
                    },
                    {
                        "range": {
                            "log_time": {
                                "gte": day + "T00:00:00",
                                "lt": day + "T23:59:59"
                            }
                        }
                    }
                ]
            }

        },
    }
    body2 = {
        "query": {
            "bool": {
                "must": [

                    {
                        "wildcard": {
                            "source": '*' + spidername + '*'
                        }
                    },
                    {
                        "match": {
                            "log_level": 'ERROR'
                        }
                    },
                    {
                        "range": {
                            "log_time": {
                                "gte": day + "T00:00:00",
                                "lt": day + "T23:59:59"
                            }
                        }
                    }
                ]
            }

        },
    }
    all = es.count(index='2018spiderlogs', body=body1)['count']
    bad = es.count(index='2018spiderlogs', body=body2)['count']
    # print(all,bad)
    return all,bad
def queryerrorbymonth(spidername,time,interval):
    es = Elasticsearch([{'host': '192.168.100.201', 'port': 9200}])
    body1 = {
        "query": {
            "bool": {
                "must": [

                    {
                        "wildcard": {
                            "source": '*' + spidername + '*'
                        }
                    },

                ]
            }

        },
        # "from": 0,
        "size": 0,
        # "sort": {"log_time": {"order": "desc"}}
        "aggs": {
            "by_time": {
                "date_histogram": {
                    "field": 'log_time',
                    "interval": 'month',
                    "format": "yyyy-MM-dd",
                    "min_doc_count": 0,
                    "extended_bounds": {
                        "min": get_day_nday_ago(time, interval - 1),
                        "max": time
                    }

                }
            }
        }
    }
    body2 = {
        "query": {
            "bool": {
                "must": [

                    {
                        "wildcard": {
                            "source": '*' + spidername + '*'
                        }
                    },
                    {
                        "match": {
                            "log_level": 'ERROR'
                        }
                    },

                ]
            }

        },
        # "from": 0,
        "size": 0,
        # "sort": {"log_time": {"order": "desc"}}
        "aggs": {
            "by_time": {
                "date_histogram": {
                    "field": 'log_time',
                    "interval": 'month',
                    "format": "yyyy-MM-dd",
                    "min_doc_count": 0,
                    "extended_bounds": {
                        "min": get_day_nday_ago(time, interval - 1),
                        "max": time
                    }

                }
            }
        }
    }
    timelist=[]
    all=[]
    bad=[]
    alllist = es.search(index='2018spiderlogs', body=body1)['aggregations']['by_time']['buckets']
    badlist = es.search(index='2018spiderlogs', body=body2)['aggregations']['by_time']['buckets']
    for item  in alllist:
        timelist.append(item['key_as_string'][:7])
        all.append(item['doc_count'])
    for item in badlist:
        bad.append(item['doc_count'])
    # print(timelist)
    # print(all)
    # print(bad)
    return timelist,bad,all

def geterrorinfo(web,interval):
    spidername = webinfo[web]
    badlist = []
    alllist = []
    if interval == '一周':
        timelist = get_nday_list('2017-05-22',6)
        timelist.append('2017-05-22')
        for i in timelist:
            all,bad = queryerrorbyday(spidername,i)
            badlist.append(bad)
            alllist.append(all)
        return timelist,badlist,alllist
    if interval == '一月':
        timelist = get_nday_list('2017-05-22',30)
        timelist.append('2017-05-22')
        # print(timelist)
        for i in timelist:
            all, bad = queryerrorbyday(spidername, i)
            badlist.append(bad)
            alllist.append(all)
        return timelist, badlist, alllist
    if interval == '一年':
        timelist,badlist,alllist=queryerrorbymonth(spidername, '2017-05-22', 365)
        return timelist, badlist, alllist

def geterrorlog():
    es = Elasticsearch([{'host': '192.168.100.201', 'port': 9200}])
    # print(spidername,gte,interval)
    body = {
        "query": {
            "bool": {
                "must": [
                    {
                        "match": {
                            "log_level": 'ERROR'
                        }
                    },

                ]
            }
            # "regexp": {
            #     "source": '(.)+bbs'
            # }

        },
        # "from": 0,
        "size": 500,
        "sort": {"log_time": {"order": "desc"}}
        # "aggs": {}
    }

    a = es.search(index='2018spiderlogs', body=body, _source='log_time,message,source')
    errorlist = a['hits']['hits']
    data = []
    for error in errorlist:
        dic = {}
        dic['spidername'] = error['_source']['source'].split('/')[-2]
        dic['errortime'] = error['_source']['log_time'].split('.')[0].replace('T',' ')
        dic['errorinfo'] = error['_source']['message']
        data.append(dic)
    return data

