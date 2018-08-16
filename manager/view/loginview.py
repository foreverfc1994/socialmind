from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from manager.scripts.sysscript import *
import pymysql  # 导入 pymysql
from visitor.models import User
import time
import json

def index(request):
    return render(request, 'background/index.html')
def login(request):
    return redirect('/logout/')
@csrf_exempt
def bindexContent(request):
    dataList = []
    a =  User.objects.values("registranttime")
    count = 0
    LASTTIMEOFADMINLOGOUT = 1531885794.0
    for i in a:
        if i['registranttime']:
            # print(i['registranttime'])
            usrrgtime = time.mktime(time.strptime(i['registranttime'],"%Y-%m-%d %H:%M:%S"))
            if usrrgtime>LASTTIMEOFADMINLOGOUT:
                count = count + 1
        else:
            print("该用户注册时间为None")
    dataList.append(count)
    data = {"data": dataList}
    return HttpResponse(json.dumps(data))

