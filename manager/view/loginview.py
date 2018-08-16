from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from manager.scripts.sysscript import *
import pymysql  # 导入 pymysql
from visitor.models import User,Event,Message
import time
import json

def index(request):
    return render(request, 'background/index.html')
def login(request):
    return redirect('/logout/')
@csrf_exempt
def bindexContent(request,a):
    if a == 0:
        dataList = []
        LASTTIMEOFADMINLOGOUT = 1531885794.0
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


