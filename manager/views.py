from django.shortcuts import render,redirect
from visitor.models import User,Province,City,Area
from visitor import models
from django.http import JsonResponse, HttpResponse
import json
from manager.mysqlNullWash import if_is_None, webType_to_strType
from django.views.decorators.csrf import csrf_exempt
from visitor.scripts.signin import *
from manager.scripts.sysscript import *
# Create your views here.
def SpiderList(request):
    return render(request, 'background/SpiderList.html')
def SpiderMonitor(request):
    return render(request, 'background/SpiderMonitor.html')
def SpiderConfigure(request):
    return render(request, 'background/SpiderConfigure.html')
def DataCleanStatistics(request):
    return render(request, 'background/DataCleanStatistics.html')
def DataCleanStrategies(request):
    return render(request, 'background/DataCleanStrategies.html')
def DataCleanLog(request):
    return render(request, 'background/DataCleanLog.html')
def washData(request):
    return render(request, 'background/washData.html')
def topics(request):
    return render(request, 'background/topics.html')
def AddEventObject(request):
    return render(request, 'background/AddEventObject.html')
def CreateEventObject(request):
    return render(request, 'background/CreateEventObject.html')
def ShowEventObject(request):
    #return render(request, 'background/ShowEventObject.html')
    return render(request, 'background/socialobject.html')
def semanticsTools(request):
    return render(request, 'background/semanticsTools.html')
def semanticsToolkits(request):
    return render(request, 'background/semanticsToolkits.html')
def ShowToolkits(request):
    return render(request, 'background/ShowToolkits.html')
def usrCommentsSelect(request):
    return render(request, 'background/usrCommentsSelect.html')
def usrCommentsCheck(request):
    return render(request, 'background/usrCommentsCheck.html')
def usrCommentsDelete(request):
    return render(request, 'background/usrCommentsDelete.html')
def AssignAuthorities(request):
    return render(request, 'background/AssignAuthorities.html')
def usersVerify(request):
    return render(request, 'background/usersVerify.html')
def usrManagement(request):
    return render(request, 'background/usrManagement.html')
def operateDiary(request):  #日志管理
    return render(request, 'background/operateDiary.html')
def DouBanArticleStyle(request):
    return render(request, 'background/DouBanArticleStyle.html')
def DouBanArticleStyle2(request):
    return render(request, 'background/DouBanArticleStyle2.html')
def usrManagement1(request,a):

    if a==0:

        return render(request, 'background/usrManagement.html',{'type0':1})
    elif a==1:
        return render(request, 'background/usrManagement.html',{'type1':1})
    elif  a==2:
        return render(request, 'background/usrManagement.html',{'type2':1})
    elif  a==3:
        return render(request, 'background/usrManagement.html',{'type3':1})
    else:
        return render(request, 'background/usrManagement.html')

def yuandatashow(request):
    return render(request, 'background/yuandatashow.html')
def operate(request,a):
    return render(request, 'background/operateDiary.html')
def articleslsit(request):
    return render(request,'background/Articleslist.html')
def objectshow(request):
    return  render(request,'background/socialobject.html')
def eventshow(request):
    return render(request,'background/Eventlist.html')
def jianbao(request):
    return render(request,'background/jianbao.html')
def qiantaimotaikuang(request):
    # userid = request.session["user_id"]
    # role = request.session["user_type"]
    # username = request.session["user_name"]
    # currentUser = models.User.objects.get(userid=userid)
    # email = currentUser.email
    # personalized_data = models.CompanyUser.objects.get(userid=userid)
    # bossname = personalized_data.bossname
    # companyname = personalized_data.companyname
    # businessLicenceId = personalized_data.businesslicenceid
    # bussinessLicencePic = str(personalized_data.businesslicenceurl)
    return render(request, 'foreground/personalInformation.html',
                  {"userid": '123', "username": 123, "role": '个人用户', "email": '461834084@qq.com',
                   "bossname": '123', "companyname": '123',
                   "businessLicenceId": '123', "bussinessLicencePic":
                       '123'})
    # return render(request,'foreground/personalInformation.html')


def getlogs(request,logtype):
    if logtype ==1:
        page = request.GET.get("page")
        limit = request.GET.get("limit")
        data, count = readlog(page, limit)
        return HttpResponse(json.dumps({"code": 0, "msg": "", "count": count, "data": data}))