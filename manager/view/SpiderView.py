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
        dic['runcommand'] = spider.runcommand
        dic['spiderconfigid'] = spider.spiderconfigid
        dic['spiderstate'] = spider.spiderstate
        a = 1





    print(111)
    pass