from django.shortcuts import render,redirect
from visitor.models import User,Province,City,Area
from visitor import models
import time
from django.http import JsonResponse, HttpResponse
import json
from manager.mysqlNullWash import if_is_None, webType_to_strType, changeWebsite
from django.views.decorators.csrf import csrf_exempt
from visitor.scripts.signin import *
from manager.scripts.sysscript import *
from manager.scripts import SSHconnect
import uuid

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
    session.excecommand(command)
    session.sshclose()
    spider.spiderstate = '运行'
    spider.save()
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
    return JsonResponse({'data':1})


@csrf_exempt
def delconfig(request):
    print(request.POST)
    id = request.POST.get('data')
    print(id)
    config = models.NewSpiderConfig.objects.get(spiderconfigid=id).delete()
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
    return JsonResponse({'data': 1})

@csrf_exempt
def addspider(request):
    print(request.POST)
    # return JsonResponse({'data':1})







