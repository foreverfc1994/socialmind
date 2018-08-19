from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from manager.scripts.sysscript import *
import pymysql  # 导入 pymysql
from visitor.models import User,Event,Message,Object
import time,datetime
import json
import re

def index(request):
    return render(request, 'background/index.html')
def login(request):
    # request.session.flush()
    return redirect('/logout/')
@csrf_exempt
def bindexContent(request,a):
    LASTTIMEOFADMINLOGOUT = 1531885794.0
    if a == 0:
        dataList = []
        usr = User.objects.all()
        count = 0
        pcount = 0
        ccount = 0
        icount = 0
        gcount = 0
        count1 = 0
        pcount1 = 0
        ccount1 = 0
        icount1 = 0
        gcount1 = 0
        for i in usr:
            if i.registranttime:
                usrrgtime = time.mktime(time.strptime(i.registranttime, "%Y-%m-%d %H:%M:%S"))
                if usrrgtime > LASTTIMEOFADMINLOGOUT:
                    count = count + 1
                    print(i.usertype)
                    if i.usertype == '个人用户':
                        pcount = pcount + 1
                    elif i.usertype == '企业用户':
                        ccount = ccount + 1
                    elif i.usertype == "事业单位用户":
                        icount = icount + 1
                    elif i.usertype == '政府用户':
                        gcount = gcount + 1
                else:
                    print("该用户注册时间为None")
            count1 = count1 + 1
            if i.usertype == '个人用户':
                pcount1 = pcount1 + 1
            elif i.usertype == '企业用户':
                ccount1 = ccount1 + 1
            elif i.usertype == '事业单位用户':
                icount1 = icount1 + 1
            elif i.usertype == '政府用户':
                gcount1 = gcount1 + 1
        dataList.append({'numofnewusrs': count
                            , "numofpusrs": pcount
                            , "numofcusrs": ccount
                            , "numofgusrs": gcount
                            , "numofiusrs": icount})
        dataList.append({'numofusrs': count1
                            , "numofpusrs": pcount1
                            , "numofcusrs": ccount1
                            , "numofgusrs": gcount1
                            , "numofiusrs": icount1})
        checked = Message.objects.values("checked")
        count = 0
        for i in checked:
            if i['checked'] == '0':
                count = count + 1
        dataList.append(count)
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))
    elif a == 2:
        dataList = []
        usr = User.objects.all()
        count = 0
        pcount = 0
        ccount = 0
        icount = 0
        gcount = 0
        count1 = 0
        pcount1 = 0
        ccount1 = 0
        icount1 = 0
        gcount1 = 0
        for i in usr:
            count1 = count1 + 1
            if i.usertype == '个人用户':
                pcount1 = pcount1 + 1
            elif i.usertype == '企业用户':
                ccount1 = ccount1 + 1
            elif i.usertype == '事业单位用户':
                icount1 = icount1 + 1
            elif i.usertype == '政府用户':
                gcount1 = gcount1 + 1
            if i.registranttime:
                usrrgtime = time.mktime(time.strptime(i.registranttime, "%Y-%m-%d %H:%M:%S"))
                if usrrgtime > LASTTIMEOFADMINLOGOUT:
                    count = count + 1
                    if i.usertype == '个人用户':
                        pcount = pcount + 1
                    elif i.usertype == '企业用户':
                        ccount = ccount + 1
                    elif i.usertype == "事业单位用户":
                        icount = icount + 1
                    elif i.usertype == '政府用户':
                        gcount = gcount + 1
        dataList.append({"zongusrs":count1})
        dataList.append({"xinzengzongusrs": count})
        dataList.append([{ "value": pcount1, "name": "个人用户数"}
                            , {"value": ccount1, "name": "企业用户数"}
                            , {"value": gcount1, "name": "政府用户数"}
                            , {"value": icount1, "name": "事业用户数"}])
        dataList.append([{ "value": pcount, "name": "新增个人用户数"}
                            , {"value": ccount, "name": "新增企业用户数"}
                            , {"value": gcount, "name": "新增政府用户数"}
                            , {"value": icount, "name": "新增事业用户数"}])
        data = {"data":dataList}
        return HttpResponse(json.dumps(data))
    elif a == 3:
        dataList = []
        datelist = []
        today = datetime.date.today()
        today = today-datetime.timedelta(days=6)
        datelist.append(today.strftime("%m.%d"))
        for i in [1, 2, 3, 4, 5, 6]:
            yesterday = today + datetime.timedelta(days=1)
            datelist.append(yesterday.strftime("%m.%d"))
            today = yesterday
        dataList.append(datelist)
        messagetime = Message.objects.values("messagetime")
        messagedatelist = [0,0,0,0,0,0,0]
        countzongliuyanliang = 0
        countzuoriliuyanliang = 0
        yesterday = datetime.date.today() - datetime.timedelta(days=1)
        yesterdaystr = yesterday.strftime("%m.%d")
        for i in messagetime:
            # print(i,type(i))
            messagetimestr = i["messagetime"]
            countzongliuyanliang = countzongliuyanliang + 1
            messagetimestrdatetime = datetime.datetime.strptime(messagetimestr, "%Y-%m-%d %H:%M:%S")
            if yesterdaystr == messagetimestrdatetime.strftime("%m.%d"):
                countzuoriliuyanliang = countzuoriliuyanliang + 1
            for index in range(len(datelist)):
                strzhuandatetime = datetime.datetime.strptime(datelist[index], "%m.%d")
                datetimezhuanstr = strzhuandatetime.strftime("%m.%d")
                if datetimezhuanstr == messagetimestrdatetime.strftime("%m.%d"):
                    messagedatelist[index] = messagedatelist[index] + 1
        # print(datelist)
        # print(messagedatelist)
        dataList.append(messagedatelist)
        dataList.append(countzongliuyanliang)
        dataList.append(countzuoriliuyanliang)
        # print(countzongliuyanliang,countzuoriliuyanliang)
        zongrizhiliang = 0
        yesterdayrizhiliang = 0
        logdatelist = [0,0,0,0,0,0,0]
        yesterdayshijianchuo = (datetime.date.today() - datetime.timedelta(days=1)).strftime("%Y-%m-%d")
        yesterdayshijianchuo = time.mktime(time.strptime(yesterdayshijianchuo,"%Y-%m-%d"))
        try:
            f = open('log/datawash.log', 'r', encoding='UTF-8')
            pattern1 = ''
            for line in f:
                zongrizhiliang = zongrizhiliang + 1
                pattern = re.search(r'^[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2} [0-9]{2,2}:[0-9]{2,2}:[0-9]{2,2}', line).group()
                patternshijianchuo = datetime.datetime.strptime(pattern, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
                patternshijianchuo = time.mktime(time.strptime(patternshijianchuo,"%Y-%m-%d"))
                # print(type(yesterdayshijianchuo),type(patternshijianchuo))
                if yesterdayshijianchuo<=patternshijianchuo:
                    yesterdayrizhiliang = yesterdayrizhiliang + 1
                for index in range(len(datelist)):
                    strzhuandatetime = datetime.datetime.strptime(pattern, "%Y-%m-%d %H:%M:%S")
                    datetimezhuanstr = strzhuandatetime.strftime("%m.%d")
                    if datetimezhuanstr == datelist[index]:
                        logdatelist[index] = logdatelist[index] + 1
            f.close()
        except Exception as e:
            raise e
        try:
            f = open('log/socialmind.log', 'r', encoding='UTF-8')
            pattern1 = ''
            for line in f:
                zongrizhiliang = zongrizhiliang + 1
                pattern = re.search(r'^[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2} [0-9]{2,2}:[0-9]{2,2}:[0-9]{2,2}', line).group()
                patternshijianchuo = datetime.datetime.strptime(pattern, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
                patternshijianchuo = time.mktime(time.strptime(patternshijianchuo,"%Y-%m-%d"))
                # print(type(yesterdayshijianchuo),type(patternshijianchuo))
                if yesterdayshijianchuo<=patternshijianchuo:
                    yesterdayrizhiliang = yesterdayrizhiliang + 1
                for index in range(len(datelist)):
                    strzhuandatetime = datetime.datetime.strptime(pattern, "%Y-%m-%d %H:%M:%S")
                    datetimezhuanstr = strzhuandatetime.strftime("%m.%d")
                    if datetimezhuanstr == datelist[index]:
                        logdatelist[index] = logdatelist[index] + 1
            f.close()
        except Exception as e:
            raise e
        try:
            f = open('log/spider.log', 'r', encoding='UTF-8')
            pattern1 = ''
            for line in f:
                zongrizhiliang = zongrizhiliang + 1
                pattern = re.search(r'^[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2} [0-9]{2,2}:[0-9]{2,2}:[0-9]{2,2}', line).group()
                patternshijianchuo = datetime.datetime.strptime(pattern, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
                patternshijianchuo = time.mktime(time.strptime(patternshijianchuo,"%Y-%m-%d"))
                # print(type(yesterdayshijianchuo),type(patternshijianchuo))
                if yesterdayshijianchuo<=patternshijianchuo:
                    yesterdayrizhiliang = yesterdayrizhiliang + 1
                for index in range(len(datelist)):
                    strzhuandatetime = datetime.datetime.strptime(pattern, "%Y-%m-%d %H:%M:%S")
                    datetimezhuanstr = strzhuandatetime.strftime("%m.%d")
                    if datetimezhuanstr == datelist[index]:
                        logdatelist[index] = logdatelist[index] + 1
            f.close()
        except Exception as e:
            raise e
        # print(zongrizhiliang,yesterdayrizhiliang,logdatelist)
        dataList.append(zongrizhiliang)
        dataList.append(yesterdayrizhiliang)
        dataList.append(logdatelist)
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))
    elif a == 9:
        dataList = []
        totalwashtimes = 0
        totalwashitems = 0
        washfrequence = 0
        lastwashtime = ''
        today = datetime.date.today()
        today = today - datetime.timedelta(days=6)
        shangzhou = today.strftime("%Y-%m-%d %H:%M:%S")
        shangzhou = time.mktime(time.strptime(shangzhou, "%Y-%m-%d %H:%M:%S"))
        try:
            f = open('log/datawash.log', 'r', encoding='UTF-8')
            pattern1 = ''
            for line in f:
                # print(line)
                pattern = re.search(r'\[[\s\S]*\] wash',line)
                # print(type(pattern))
                ms = re.sub(r' wash$',"",pattern.group())
                # print(pattern,type(pattern))
                ms = ms[1: -1]
                index = []
                for i, ch in enumerate(ms):
                    if ch == ',' and len(index) < 5:
                        index.append(i)
                # print(ms)
                ls = []
                ls.append(ms[1: index[0] - 1])
                ls.append(ms[index[0] + 3: index[1] - 1])
                ls.append(ms[index[1] + 3:index[2] - 1])
                ls.append(ms[index[2] + 2: index[3]])
                ls.append(ms[index[3] + 3: index[4] - 1])
                ls.append(ms[index[4] + 3: -1])
                # print(ls,type(ls))
                pattern = re.search(r'^[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2} [0-9]{2,2}:[0-9]{2,2}:[0-9]{2,2}', line).group()
                if pattern != pattern1:
                    if ls[4] != "撤回":
                        totalwashtimes = totalwashtimes + 1
                        thistime = time.mktime(time.strptime(pattern, "%Y-%m-%d %H:%M:%S"))
                        if shangzhou < thistime:
                            washfrequence = washfrequence + 1
                    else:
                        totalwashtimes = totalwashtimes - 1
                        thistime = time.mktime(time.strptime(pattern, "%Y-%m-%d %H:%M:%S"))
                        if shangzhou < thistime:
                            washfrequence = washfrequence - 1
                pattern1 = pattern
                if ls[4] != "撤回":
                    totalwashitems = totalwashitems + int(ls[3])
                else:
                    totalwashitems = totalwashitems - int(ls[3])
                lastwashtime = pattern
            # print(totalwashtimes,totalwashitems,washfrequence,lastwashtime)
            dataList.append([totalwashtimes,totalwashitems,washfrequence,lastwashtime])
            f.close()
        except Exception as e:
            raise e
        db = pymysql.connect(host="localhost", user="root",
                             password="461834084", db="linshitongji", port=3306)
        cur = db.cursor()
        sql = "select TABLE_NAME,SCHEMA_NAME,WebSite,WebsiteType,NUM_ROWS,TABLE_TYPE,NUM_COLUMNS from datatables,website_schema where SCHEMA_NAME=SchemaName"
        diylist = []
        try:
            cur.execute(sql)  # 执行sql语句
            results = cur.fetchall()  # 获取查询的所有记录
            print("tableName", "schemaName", "webSite", "webSiteType", "dataVolum")
            # 遍历结果
            for row in results:
                tableName = row[0]
                schemaName = row[1]
                webSite = row[2]
                webSiteType = row[3]
                dataVolum = row[4]
                tableType = row[5]
                colnumber = row[6]
                print(tableName, schemaName, webSite, webSiteType, dataVolum, tableType)
                diylist.append({"tableName": tableName,
                                "schemaName": schemaName,
                                "webSite": webSite,
                                "webSiteType": webSiteType,
                                "dataVolum": dataVolum,
                                "tableType": tableType,
                                "colnumber": colnumber})
            dataList.append(diylist)
        except Exception as e:
            raise e
        finally:
            db.close()  # 关闭连接
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))
    elif a == 10:
        dataList = []
        linshilist = []
        today = datetime.date.today()
        today = today - datetime.timedelta(days=6)
        shangzhou = today.strftime("%Y-%m-%d %H:%M:%S")
        shangzhou = time.mktime(time.strptime(shangzhou, "%Y-%m-%d %H:%M:%S"))
        try:
            f = open('log/datawash.log', 'r', encoding='UTF-8')
            for line in f:
                # print(line)
                pattern = re.search(r'\[[\s\S]*\] wash', line)
                # print(type(pattern))
                ms = re.sub(r' wash$', "", pattern.group())
                # print(pattern,type(pattern))
                ms = ms[1: -1]
                index = []
                for i, ch in enumerate(ms):
                    if ch == ',' and len(index) < 5:
                        index.append(i)
                # print(ms)
                ls = []
                ls.append(ms[1: index[0] - 1])
                ls.append(ms[index[0] + 3: index[1] - 1])
                ls.append(ms[index[1] + 3:index[2] - 1])
                ls.append(ms[index[2] + 2: index[3]])
                ls.append(ms[index[3] + 3: index[4] - 1])
                ls.append(ms[index[4] + 3: -1])
                # print(ls,type(ls))
                pattern = re.search(r'^[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2} [0-9]{2,2}:[0-9]{2,2}:[0-9]{2,2}', line).group()
                patternshijianchuo = time.mktime(time.strptime(pattern, "%Y-%m-%d %H:%M:%S"))
                if patternshijianchuo>=shangzhou:
                    linshilist.append({
                        "tableName": ls[1]
                        ,"adminname": ls[2]
                        ,"optype": ls[4]
                        ,"optime": pattern
                        ,"washitemsvolumn": ls[3]
                        ,"opdetils": ls[5]
                    })
                    # print(linshilist)
            dataList.append(linshilist)
            f.close()
        except Exception as e:
            raise e
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))
    elif a == 11:
        dataList = []
        adminnamelist = []
        adminitemslist = []
        today = datetime.date.today()
        today = today - datetime.timedelta(days=6)
        shangzhou = today.strftime("%Y-%m-%d %H:%M:%S")
        shangzhou = time.mktime(time.strptime(shangzhou, "%Y-%m-%d %H:%M:%S"))
        try:
            f = open('log/datawash.log', 'r', encoding='UTF-8')
            for line in f:
                # print(line)
                pattern = re.search(r'\[[\s\S]*\] wash', line)
                # print(type(pattern))
                ms = re.sub(r' wash$', "", pattern.group())
                # print(pattern,type(pattern))
                ms = ms[1: -1]
                index = []
                for i, ch in enumerate(ms):
                    if ch == ',' and len(index) < 5:
                        index.append(i)
                # print(ms)
                ls = []
                ls.append(ms[1: index[0] - 1])
                ls.append(ms[index[0] + 3: index[1] - 1])
                ls.append(ms[index[1] + 3:index[2] - 1])
                ls.append(ms[index[2] + 2: index[3]])
                ls.append(ms[index[3] + 3: index[4] - 1])
                ls.append(ms[index[4] + 3: -1])
                # print(ls,type(ls))
                pattern = re.search(r'^[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2} [0-9]{2,2}:[0-9]{2,2}:[0-9]{2,2}', line).group()
                patternshijianchuo = time.mktime(time.strptime(pattern, "%Y-%m-%d %H:%M:%S"))
                if patternshijianchuo >= shangzhou:
                    linshiflg = 0
                    if len(adminnamelist) == 0:
                        adminnamelist.append(ls[2])
                        adminitemslist.append(0)
                    for i in adminnamelist:
                        if i == ls[2]:
                            break
                        else:
                            linshiflg = 1
                    if linshiflg == 1:
                        adminnamelist.append(ls[2])
                        adminitemslist.append(0)
                    for index in range(len(adminnamelist)):
                        if adminnamelist[index] == ls[2]:
                            if ls[4] == '撤回':
                                adminitemslist[index] = adminitemslist[index] - int(ls[3])
                            else:
                                adminitemslist[index] = adminitemslist[index] + int(ls[3])
            print(adminnamelist,adminitemslist)
            dataList.append(adminnamelist)
            dataList.append(adminitemslist)
            f.close()
        except Exception as e:
            raise e
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))
    elif a == 12:
        dataList = []
        Objects = Object.objects.all()
        todaystr = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        yesterdaydate = datetime.datetime.strptime(todaystr, "%Y-%m-%d %H:%M:%S")-datetime.timedelta(days=1)
        yesterdaystr = yesterdaydate.strftime("%Y-%m-%d %H:%M:%S")
        yesterdayshijianchuo = time.mktime(time.strptime(yesterdaystr,"%Y-%m-%d %H:%M:%S"))
        lastweekdate = datetime.datetime.strptime(todaystr, "%Y-%m-%d %H:%M:%S") - datetime.timedelta(days=7)
        lastweekstr = lastweekdate.strftime("%Y-%m-%d %H:%M:%S")
        lastweekshijianchuo = time.mktime(time.strptime(lastweekstr, "%Y-%m-%d %H:%M:%S"))
        # print(yesterdayshijianchuo)
        shijiancount = 0
        shiticount = 0
        zuorixinzengshijiancount = 0
        zuorixinznegshiticount = 0
        lastweekxinzengshijiancount = 0
        lastweekxinzengshiticount = 0
        for i in Objects:
            if i.objecttype == "事件":
                shijiancount = shijiancount + 1
                if i.addtime:
                    adddate = datetime.datetime.strptime(i.addtime, "%Y-%m-%d %H:%M:%S")
                    adddatestr = adddate.strftime("%Y-%m-%d %H:%M:%S")
                    adddatestrshijianchuo = time.mktime(time.strptime(adddatestr, "%Y-%m-%d %H:%M:%S"))
                    if adddatestrshijianchuo >= yesterdayshijianchuo:
                        zuorixinzengshijiancount = zuorixinzengshijiancount + 1
                    if adddatestrshijianchuo >= lastweekshijianchuo:
                        lastweekxinzengshijiancount = lastweekxinzengshijiancount + 1
            elif i.objecttype == "实体":
                shiticount = shiticount + 1
                if i.addtime:
                    adddate = datetime.datetime.strptime(i.addtime, "%Y-%m-%d %H:%M:%S")
                    adddatestr = adddate.strftime("%Y-%m-%d %H:%M:%S")
                    adddatestrshijianchuo = time.mktime(time.strptime(adddatestr, "%Y-%m-%d %H:%M:%S"))
                    if adddatestrshijianchuo >= yesterdayshijianchuo:
                        zuorixinznegshiticount = zuorixinznegshiticount + 1
                    if adddatestrshijianchuo >= lastweekshijianchuo:
                        lastweekxinzengshiticount = lastweekxinzengshiticount + 1
        # print(shijiancount,shiticount,zuorixinzengshijiancount,zuorixinznegshiticount,lastweekxinzengshijiancount,lastweekxinzengshiticount)
        dataList.append([shijiancount,shiticount,zuorixinzengshijiancount,zuorixinznegshiticount,lastweekxinzengshijiancount,lastweekxinzengshiticount])
        province_shitilist = [{"name": '北京', "value": 0}, {"name": '天津', "value": 0},
                        {"name": '上海', "value": 0}, {"name": '重庆', "value": 0},
                        {"name": '河北', "value": 0}, {"name": '河南', "value": 0},
                        {"name": '云南', "value": 0}, {"name": '辽宁', "value": 0},
                        {"name": '黑龙江', "value": 0}, {"name": '湖南', "value": 0},
                        {"name": '安徽', "value": 0}, {"name": '山东', "value": 0},
                        {"name": '新疆', "value": 0}, {"name": '江苏', "value": 0},
                        {"name": '浙江', "value": 0}, {"name": '江西', "value": 0},
                        {"name": '湖北', "value": 0}, {"name": '广西', "value": 0},
                        {"name": '甘肃', "value": 0}, {"name": '山西', "value": 0},
                        {"name": '内蒙古', "value": 0}, {"name": '陕西', "value": 0},
                        {"name": '吉林', "value": 0}, {"name": '福建', "value": 0},
                        {"name": '贵州', "value": 0}, {"name": '广东', "value": 0},
                        {"name": '青海', "value": 0}, {"name": '西藏', "value": 0},
                        {"name": '四川', "value": 0}, {"name": '宁夏', "value": 0},
                        {"name": '海南', "value": 0}, {"name": '台湾', "value": 0},
                        {"name": '香港', "value": 0}, {"name": '澳门', "value": 0}
                        ];
        province_shijianlist = [{"name": '北京', "value": 0}, {"name": '天津', "value": 0},
                        {"name": '上海', "value": 0}, {"name": '重庆', "value": 0},
                        {"name": '河北', "value": 0}, {"name": '河南', "value": 0},
                        {"name": '云南', "value": 0}, {"name": '辽宁', "value": 0},
                        {"name": '黑龙江', "value": 0}, {"name": '湖南', "value": 0},
                        {"name": '安徽', "value": 0}, {"name": '山东', "value": 0},
                        {"name": '新疆', "value": 0}, {"name": '江苏', "value": 0},
                        {"name": '浙江', "value": 0}, {"name": '江西', "value": 0},
                        {"name": '湖北', "value": 0}, {"name": '广西', "value": 0},
                        {"name": '甘肃', "value": 0}, {"name": '山西', "value": 0},
                        {"name": '内蒙古', "value": 0}, {"name": '陕西', "value": 0},
                        {"name": '吉林', "value": 0}, {"name": '福建', "value": 0},
                        {"name": '贵州', "value": 0}, {"name": '广东', "value": 0},
                        {"name": '青海', "value": 0}, {"name": '西藏', "value": 0},
                        {"name": '四川', "value": 0}, {"name": '宁夏', "value": 0},
                        {"name": '海南', "value": 0}, {"name": '台湾', "value": 0},
                        {"name": '香港', "value": 0}, {"name": '澳门', "value": 0}
                        ];
        provincelist = [{"name": '北京', "value": 0}, {"name": '天津', "value": 0},
                        {"name": '上海', "value": 0}, {"name": '重庆', "value": 0},
                        {"name": '河北', "value": 0}, {"name": '河南', "value": 0},
                        {"name": '云南', "value": 0}, {"name": '辽宁', "value": 0},
                        {"name": '黑龙江', "value": 0}, {"name": '湖南', "value": 0},
                        {"name": '安徽', "value": 0}, {"name": '山东', "value": 0},
                        {"name": '新疆', "value": 0}, {"name": '江苏', "value": 0},
                        {"name": '浙江', "value": 0}, {"name": '江西', "value": 0},
                        {"name": '湖北', "value": 0}, {"name": '广西', "value": 0},
                        {"name": '甘肃', "value": 0}, {"name": '山西', "value": 0},
                        {"name": '内蒙古', "value": 0}, {"name": '陕西', "value": 0},
                        {"name": '吉林', "value": 0}, {"name": '福建', "value": 0},
                        {"name": '贵州', "value": 0}, {"name": '广东', "value": 0},
                        {"name": '青海', "value": 0}, {"name": '西藏', "value": 0},
                        {"name": '四川', "value": 0}, {"name": '宁夏', "value": 0},
                        {"name": '海南', "value": 0}, {"name": '台湾', "value": 0},
                        {"name": '香港', "value": 0}, {"name": '澳门', "value": 0}
                        ];
        maxval = 0
        for i in Objects:
            for index in range(len(provincelist)):
                if i.place == provincelist[index]["name"]:
                    provincelist[index]["value"] = provincelist[index]["value"] + 1
                    if i.objecttype == "事件":
                        province_shijianlist[index]["value"] = province_shijianlist[index]["value"] + 1
                    elif i.objecttype == "实体":
                        province_shitilist[index]["value"] = province_shitilist[index]["value"] + 1
                    if maxval < provincelist[index]["value"]:
                        maxval = maxval + 1
        # print(provincelist)
        dataList.append(provincelist)
        dataList.append(maxval)
        dataList.append(province_shijianlist)
        dataList.append(province_shitilist)
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))
@csrf_exempt
def provinceyuqing(request):
    dataList = []
    provinceinfo = request.POST
    provincename = provinceinfo.get('provincename')
    # print(provincename)
    datelist = []
    today = datetime.date.today()
    today = today - datetime.timedelta(days=6)
    datelist.append(today.strftime("%m.%d"))
    for i in [1, 2, 3, 4, 5, 6]:
        yesterday = today + datetime.timedelta(days=1)
        datelist.append(yesterday.strftime("%m.%d"))
        today = yesterday
    dataList.append(datelist)
    neweventcount = [0,0,0,0,0,0,0]
    newentitycount = [0,0,0,0,0,0,0]
    Objects = Object.objects.all()
    for i in Objects:
        if i.place == provincename:
            if i.addtime:
                addtime = datetime.datetime.strptime(i.addtime, "%Y-%m-%d %H:%M:%S")
                addtimestr = addtime.strftime("%m.%d")
                for index in range(len(datelist)):
                    # print(datelist[index], addtimestr)
                    if datelist[index] == addtimestr:
                        if i.objecttype == '事件':
                            neweventcount[index] = neweventcount[index] + 1
                        elif i.objecttype == '实体':
                            newentitycount[index] = newentitycount[index] + 1
    # print(neweventcount)
    # print(newentitycount)
    dataList.append(neweventcount)
    dataList.append(newentitycount)
    data = {"data": dataList}
    return HttpResponse(json.dumps(data))
@csrf_exempt
def searchcolnames(request):
    dataList = []
    aaa = request.POST
    webSite = aaa.get('webSite')
    tableName = aaa.get('tableName')

    # print(webSite,tableName)
    db = pymysql.connect(host="localhost", user="root",
                         password="461834084", db="linshitongji", port=3306)
    cur = db.cursor()
    sql = "select SchemaName from website_schema where WebSite='"+webSite+"'"
    try:
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        schemaName = ''
        for row in results:
            schemaName = row[0]
        print(schemaName)
        sql2 = "desc " + schemaName + "." + tableName
        cur.execute(sql2)
        results = cur.fetchall()  # 获取查询的所有记录
        colnamelist = []
        for i in results:
            print(i[0])
            colnamelist.append(i[0])
        dataList.append(colnamelist)
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接
    data = {"data": dataList}
    return HttpResponse(json.dumps(data))
