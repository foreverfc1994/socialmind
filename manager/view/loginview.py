from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from manager.scripts.sysscript import *
import pymysql  # 导入 pymysql
from visitor.models import User,Event,Message
import time,datetime
import json

def index(request):
    return render(request, 'background/index.html')
def login(request):
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
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))

