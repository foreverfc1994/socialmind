from django.shortcuts import render,redirect
from visitor.models import User,Province,City,Area
from visitor import models
import time
import random
from django.http import JsonResponse, HttpResponse
import json
from manager.mysqlNullWash import if_is_None, webType_to_strType, changeWebsite
from django.views.decorators.csrf import csrf_exempt
from visitor.scripts.signin import *
from manager.scripts.sysscript import *
from manager.scripts import SSHconnect,ELK
import uuid
import logging
logger = logging.getLogger('spider')
def getspiderlist(request):
    spiders = models.SpiderInfo.objects.all()
    datalist =[]
    for spider in spiders:
        dic = {}
        dic['spiderid'] = spider.spiderid
        dic['spidername'] = spider.spidername
        dic['spiderpath'] = spider.spidersourcepath
        dic['addtime'] = spider.addtime
        website = spider.websiteid.websitename
        # website = models.Website.objects.get(websiteid=spider.websiteid).websitename
        dic['website'] = website
        dic['runcommand'] = spider.RunCommand
        dic['spiderconfigid'] = spider.spiderconfigid.configname
        dic['spiderstate'] = spider.spiderstate
        dic['vimname'] = spider.vimname
        datalist.append(dic)
    logdata = [request.session['user_id'], request.session['user_role'], '', '获取爬虫列表', []]
    logger.debug(logdata)
    return JsonResponse({'data':datalist})
@csrf_exempt
def runspider(request):
    print(request.POST.get('id'))
    spiderid = request.POST.get('id')
    spider = models.SpiderInfo.objects.get(spiderid=spiderid)
    # vmid = spider.vimname
    spdierpath = spider.spidersourcepath
    runcommand  = spider.RunCommand
    session = SSHconnect.SSHsession('test','root','foreverfc')
    command = 'cd '+spdierpath+';'+runcommand
    print(command)
    session.excecommand(command)
    session.sshclose()
    spider.spiderstate = '运行'
    spider.save()
    logdata = [request.session['user_id'], request.session['user_role'], '', '运行爬虫', [spiderid]]
    logger.debug(logdata)
    return JsonResponse({'data':'sucess'})
def getPID(session,name):
    stdin, stdout, stderr = session.session.exec_command(
        'ps -ef')
    for i in stdout.readlines():
        if len(i.split(name))==2:
            PID = [l for l in i.split(' ') if l!=''][1]
            print(PID)
            return PID
@csrf_exempt
def stopspider(request):
    spiderid = request.POST.get('id')
    print(spiderid)
    spider = models.SpiderInfo.objects.get(spiderid=spiderid)
    name = spider.spiderrunname
    print(name)
    session = SSHconnect.SSHsession('test', 'root', 'foreverfc')
    PID = getPID(session,name)
    print(PID)
    session.excecommand('kill -9 '+PID)
    session.sshclose()
    spider.spiderstate = '暂停'
    spider.save()
    logdata = [request.session['user_id'], request.session['user_role'], '', '停止爬虫', [spiderid]]
    logger.debug(logdata)
    return JsonResponse({'data': 'sucess'})

def getspiderconfig(request):
    configs = models.NewSpiderConfig.objects.all()
    datalist = []
    for config in configs:
        dic = {}
        dic['configid'] = config.spiderconfigid
        dic['configname'] = config.spiderconfigname
        dic['isrobot'] = config.isrobot
        dic['maxdownload'] = config.maxdownbytes
        dic['downloadtimeout'] = config.downloadtimeout
        dic['dnstimeout'] = config.dnstimeout
        dic['maxdeep'] = config.maxdeep
        dic['ipmax'] = config.ipconcurrentrequest
        dic['webmax'] = config.siteconcurrentrequest
        dic['dealmax'] = config.maxconcurrentprocessing
        dic['isdeep'] = config.iscollectdeepdata
        datalist.append(dic)
    logdata = [request.session['user_id'], request.session['user_role'], '', '获取爬虫配置列表', []]
    logger.debug(logdata)
    return JsonResponse({'data':datalist})
@csrf_exempt
def getspiderconfigbyid(request):
    id = request.POST.get('data')
    config = models.NewSpiderConfig.objects.get(spiderconfigid=id)
    dic = {}
    dic['configid'] = config.spiderconfigid
    dic['configname'] = config.spiderconfigname
    dic['isrobot'] = config.isrobot
    dic['maxdownload'] = config.maxdownbytes
    dic['downloadtimeout'] = config.downloadtimeout
    dic['dnstimeout'] = config.dnstimeout
    dic['maxdeep'] = config.maxdeep
    dic['ipmax'] = config.ipconcurrentrequest
    dic['webmax'] = config.siteconcurrentrequest
    dic['dealmax'] = config.maxconcurrentprocessing
    dic['isdeep'] = config.iscollectdeepdata
    logdata = [request.session['user_id'], request.session['user_role'], '', '获取爬虫配置列表', [id]]
    logger.debug(logdata)
    return JsonResponse({'data':dic})
@csrf_exempt
def changeconfig(request):
    data  = request.POST
    id = request.POST.get('mid')
    config = models.NewSpiderConfig.objects.get(spiderconfigid=id)
    config.spiderconfigname = data['mname']
    config.isrobot = data['mrebot']
    config.maxdownbytes = data['mmd']
    config.downloadtimeout = data['mdt']
    config.dnstimeout = data['mdnst']
    config.maxdeep = data['mmdeep']
    config.ipconcurrentrequest = data['mipm']
    config.siteconcurrentrequest = data['mwm']
    config.maxconcurrentprocessing = data['mmp']
    config.iscollectdeepdata = data['mcd']
    config.save()
    logdata = [request.session['user_id'], request.session['user_role'], '', '修改爬虫配置', [id]]
    logger.debug(logdata)
    return JsonResponse({'data':1})


@csrf_exempt
def delconfig(request):
    print(request.POST)
    id = request.POST.get('data')
    print(id)
    config = models.NewSpiderConfig.objects.get(spiderconfigid=id).delete()
    logdata = [request.session['user_id'], request.session['user_role'], '', '删除爬虫配置', [id]]
    logger.debug(logdata)
    return JsonResponse({'data': 1})
@csrf_exempt
def addconfig(request):
    data = request.POST
    config = models.NewSpiderConfig()
    config.spiderconfigid = uuid.uuid4()
    config.spiderconfigname = data['name']
    config.isrobot = data['rebot']
    config.maxdownbytes = data['md']
    config.downloadtimeout = data['dt']
    config.dnstimeout = data['dnst']
    config.maxdeep = data['mdeep']
    config.ipconcurrentrequest = data['ipm']
    config.siteconcurrentrequest = data['wm']
    config.maxconcurrentprocessing = data['mp']
    config.iscollectdeepdata = data['cd']
    config.save()
    logdata = [request.session['user_id'], request.session['user_role'], '', '添加爬虫配置', []]
    logger.debug(logdata)
    return JsonResponse({'data': 1})

@csrf_exempt
def addspider(request):
    print(request.POST)
    spider = models.SpiderInfo()
    data = request.POST
    spider.spidername = data.get('spider-name')
    site = data.get('website')
    config = data.get('config')
    vm = data.get('vm')
    command= data.get('command')
    try:
        spider.websiteid = models.Website.objects.get(websitename=site)
    except:
        return JsonResponse({'data': 'errorsite'})

    spider.spiderconfigid = models.SpiderConfig.objects.get(configname='配置一')
    spider.vimname = vm
    spider.spiderid = uuid.uuid4()
    spider.RunCommand = command
    file = request.FILES['path']
    spider.addtime =time.strftime("%Y-%m-%d %H:%M",time.localtime(time.time()))
    runname = str(file).split('.')[0]
    path = '/home/fengcong/spider/spiders/'+runname+'/'+runname
    spider.spiderrunname = runname
    spider.spidersourcepath = path
    spider.spiderstate='暂停'
    savefile(file)
    spider.save()
    logdata = [request.session['user_id'], request.session['user_role'], '', '添加爬虫', []]
    logger.debug(logdata)
    return JsonResponse({'data': 'sucess'})
    # file  = request.FILES['path']

    # return JsonResponse({'data':1})

def savefile(file):
    file_path = os.path.join('static', 'upload\\file', str(file))
    print(file_path)
    f = open(file_path, 'wb')
    print("mark")
    for chunk in file.chunks():
        f.write(chunk)
    f.close()
    import paramiko
    trans = paramiko.Transport(('192.168.100.97', 22))
    # 建立连接
    trans.connect(username='root', password='foreverfc')

    # 实例化一个 sftp对象,指定连接的通道
    sftp = paramiko.SFTPClient.from_transport(trans)
    # 发送文件
    sftp.put(localpath=file_path, remotepath='/home/fengcong/spider/spiders/'+str(file))
    ssh = paramiko.SSHClient()
    ssh._transport = trans
    print('cd /home/fengcong/spider/spiders;unzip '+str(file))
    stdin, stdout, stderr = ssh.exec_command('cd /home/fengcong/spider/spiders;unzip '+str(file))
    for i  in stdout.readlines():
        print(i)
    stdin, stdout, stderr = ssh.exec_command('cd /home/fengcong/spider/spiders;rm -rf '+str(file))
    stdin, stdout, stderr = ssh.exec_command('cd /home/fengcong/spider/spider_logs;mkdir '+str(file).split('.')[0])
    stdin, stdout, stderr = ssh.exec_command('cd /home/fengcong/spider/spider_logs/'+str(file).split('.')[0]+';touch ' + str(file).split('.')[0]+'.logs')
    # 下载文件
    # sftp.get(remotepath, localpath)
    ssh.close()
    trans.close()
@csrf_exempt
def delspider(request):
    id = request.POST.get('id')
    models.SpiderInfo.objects.get(spiderid=id).delete()
    logdata = [request.session['user_id'], request.session['user_role'], '', '删除爬虫', [id]]
    logger.debug(logdata)
    return JsonResponse({'data':1})

@csrf_exempt
def queryspider(request):
    type = request.POST.get('type')
    if type == 'SpiderWeekSpeed':
        dic = {}
        website = request.POST.get('web')
        pagespeed,itemspeed,timelist = ELK.queryweekspeed(website,'2017-05-22')
        dic['page'] = pagespeed
        dic['item'] = itemspeed
        dic['time'] = timelist
        # print(dic)
    website = request.POST.get('web')
    logdata = [request.session['user_id'], request.session['user_role'], '', '查询爬虫速率', [website,type]]
    logger.debug(logdata)
    return JsonResponse({'data':dic})


@csrf_exempt
def queryspiderspeed(request):
    jg = request.POST.get('data')
    if jg == '今日':
        interval = 1
    elif jg == '一周':
        interval = 7
    else:
        interval = 30

    data = ELK.getspiderspeed(interval)
    logdata = [request.session['user_id'], request.session['user_role'], '', '查询爬虫速率', [jg]]
    logger.debug(logdata)
    return JsonResponse({'data':data})
    pass
@csrf_exempt
def queryerror(request):
    web = request.POST.get('web')
    interval = request.POST.get('time')
    time,bad,all = ELK.geterrorinfo(web,interval)
    # print(web,interval)
    dic = {}
    dic['time']=time
    dic['bad']=bad
    dic['all']=all
    # print(dic)
    logdata = [request.session['user_id'], request.session['user_role'], '', '查询爬虫错误数据', [web,time]]
    logger.debug(logdata)
    return JsonResponse(dic)

@csrf_exempt
def queryspidernum(request):
    web = request.POST.get('web')
    interval = request.POST.get('interval')
    dic = {}
    dic['web'] = web
    if interval=="一周":
        dic['time'] = ['2018-02-11', '2018-02-12', '2018-02-13', '2018-02-14', '2018-02-15', '2018-02-16', '2018-02-17']
        if web == '天涯BBS':
            dic['topic'] = [301, 251, 417, 0, 610, 741, 0]
            dic['comment'] = [2014, 1879, 3645, 0, 5981, 6214, 0]
            dic['author'] = [151, 21, 41, 0, 51, 65, 0]

        elif web == "猫扑论坛":
            dic['topic'] = [19, 418, 388, 0, 245, 495, 916]
            dic['comment'] = [87, 2103, 4441, 0, 1318, 3915, 2793]
            dic['author'] = [251, 451, 365, 0, 189, 296, 324]
        elif web =="人民网论坛":
            dic['topic']=[131, 939, 489, 318, 332, 375, 448]
            dic['comment'] = [236, 828, 2458, 3451, 542, 3908, 733]
            dic['author'] = [283, 315, 247, 220, 401, 333, 437]
        elif web=="新华网论坛":
            dic['topic']=[779, 468, 221, 615, 51, 347, 547]
            dic['comment'] = [3643, 7, 1405, 2980, 3985, 1401, 2140]
            dic['author'] = [0, 1, 1, 1, 0, 1, 1]
        else:
            dic['topic'] = [305, 266, 350, 22, 104, 921, 971]
            dic['comment'] = [273, 379, 401, 452, 544, 421, 216]
            dic['author'] = [306, 386, 503, 589, 490, 103, 84]
    if interval=="一月":
        dic['time'] = ['2018-01-19', '2018-01-20', '2018-01-21', '2018-01-22', '2018-01-23', '2018-01-24', '2018-01-25', '2018-01-26', '2018-01-27', '2018-01-28', '2018-01-29', '2018-01-30', '2018-01-31', '2018-02-01', '2018-02-02', '2018-02-03', '2018-02-04', '2018-02-05', '2018-02-06', '2018-02-07', '2018-02-08', '2018-02-09', '2018-02-10', '2018-02-11', '2018-02-12', '2018-02-13', '2018-02-14', '2018-02-15', '2018-02-16', '2018-02-17']
        if web == '天涯BBS':
            dic['topic'] = [301, 251, 417, 0, 610, 741, 0,340, 218, 969, 361, 270, 852, 211, 743, 954, 313, 219, 822, 61, 186, 41, 554, 792, 716, 772, 578, 735, 385, 436]
            dic['comment'] = [2014, 1879, 3645, 0, 5981, 6214, 0,1208, 482, 6004, 2676, 1854, 5928, 1064, 4671, 5005, 2193, 852, 5933, 51, 668, 337, 3430, 3266, 4561, 4433, 2807, 2327, 2515, 2866]
            dic['author'] = [151, 21, 41, 0, 51, 65, 0,171, 75, 409, 187, 11, 503, 142, 566, 728, 82, 260, 398, 35, 136, 29, 246, 505, 254, 367, 398, 461, 217, 308]

        elif web == "猫扑论坛":
            dic['topic'] = [19, 418, 388, 0, 245, 495, 916,923, 608, 126, 209, 604, 903, 341, 574, 440, 114, 615, 220, 988, 828, 186, 281, 996, 760, 267, 680, 599, 903, 40]
            dic['comment'] = [87, 2103, 4441, 0, 1318, 3915, 2793,4618, 1765, 990, 1529, 2362, 6342, 2466, 2380, 2551, 549, 3956, 779, 5791, 5052, 693, 1982, 5990, 4050, 1063, 3510, 2901, 3907, 228]
            dic['author'] = [251, 451, 365, 0, 189, 296, 324,367, 413,6, 186, 492, 581, 144, 433, 374, 84, 402, 77, 739, 448, 163, 91, 664, 308, 73, 378, 314, 810, 20]
        elif web =="人民网论坛":
            dic['topic']=[131, 939, 489, 318, 332, 375, 448,690, 484, 751, 85, 788, 689, 329, 578, 367, 391, 371, 20, 750, 688, 404, 431, 179, 624, 859, 909, 625, 553, 101]
            dic['comment'] = [236, 828, 2458, 3451, 542, 3908, 733,3448, 2327, 5435, 485, 2552, 4009, 2280, 1783, 2033, 2684, 1370, 200, 3950, 2930, 1319, 1762, 1330, 1771, 6236, 5343, 3699, 3551, 368]
            dic['author'] = [283, 315, 247, 220, 401, 333, 437,360, 234, 368, 161, 474, 435, 93, 423, 232, 165, 253, 44, 542, 462, 350, 276, 155, 263, 330, 586, 203, 291, 137]
        elif web=="新华网论坛":
            dic['topic']=[779, 468, 221, 615, 51, 347, 547,682, 407, 197, 498, 432, 693, 352, 468, 359, 699, 73, 497, 118, 229, 430, 960, 162, 204, 296, 237, 106, 693, 805]
            dic['comment'] = [3643, 7, 1405, 2980, 3985, 1401, 2140,3534, 2260, 801, 2790, 2246, 2276, 2356, 1380, 1560, 4490, 391, 3771, 858, 849, 1400, 6978, 513, 1249, 1589, 719, 341, 3423, 4731]
            dic['author'] = [0, 1, 1, 1, 0, 1, 1,0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        else:
            dic['topic'] = [305, 266, 350, 22, 104, 921, 971,234, 824, 300, 946, 371, 404, 727, 252, 927, 749, 488, 252, 705, 740, 438, 974, 338, 415, 636, 45, 774, 800, 242]
            dic['comment'] = [273, 379, 401, 452, 544, 421, 216,1509, 3219, 1180, 4639, 2876, 2803, 4413, 1800, 4591, 5254, 1402, 1119, 2368, 2896, 3341, 4783, 1706, 1201, 2490, 229, 3843, 4800, 1421]
            dic['author'] = [306, 386, 503, 589, 490, 103, 84,6, 476, 42, 689, 200, 191, 446, 227, 427, 415, 281, 104, 465, 355, 286, 464, 285, 251, 473, 41, 582, 639, 94]

    sumlist = [sum(dic['topic']), sum(dic['comment']), sum(dic['author'])]
    print(sumlist)
    dic['sum'] = sumlist
    print(len(dic['time']))

    logdata = [request.session['user_id'], request.session['user_role'], '', '查询爬虫数据量', [web, interval]]
    logger.debug(logdata)
    return JsonResponse(dic)

def geterrorlog(request):
    data = ELK.geterrorlog()

    return JsonResponse({'data':data})
    pass
def getspiderlog(request):
    data = readspiderlog()
    return JsonResponse({'data':data})