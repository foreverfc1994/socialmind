from django.shortcuts import render,redirect
from visitor import models
from django.http import JsonResponse
import datetime
from manager.mysqlNullWash import countAge, if_is_None

def personList(request):
    valuePerson = models.PersonUser.objects.values("userid", "sex", "birthday", "phonenumber", "career", "realname")
    valueCommen = models.User.objects.values("userid", "email", "registranttime", "username")
    data = []
    for item in valuePerson:
        userid = item['userid']
        realname = if_is_None(item['realname'], "无记录")
        try:
            birthday = item['birthday']
            bt = datetime.datetime.strptime(birthday, '%Y-%m-%d')
            age = str(countAge(bt))
        except:
            age = "未知"
        sex = "男" if item['sex'] == "1" else "女"
        phoneNum = if_is_None(item['phonenumber'], "无数据")
        job = if_is_None(item['career'], "无数据")
        commvalue = valueCommen.get(userid=userid)
        try:
            email = if_is_None(commvalue['email'], "暂缺")
            registranttime = if_is_None(commvalue['registranttime'], "这个嘛……")
            username = if_is_None(commvalue['username'], "出错")
            data.append({"userid": userid, "realname": realname, "sex": sex, "age": age, "phoneNum": phoneNum,
                         "email": email, "job": job, "registrantTime": registranttime, "username": username})
        except:
            print(userid+" was wrong")
    return JsonResponse({"data": data})


def companyList(request):
    valueCompany = models.CompanyUser.objects.values("userid", "companyname", "companytype", "registertime")
    valueCommen = models.User.objects.values("userid", "email", "registranttime", "username")
    data = []
    for item in valueCompany:
        userid = item['userid']
        companyname = if_is_None(item['companyname'], "无记录")
        companytype = if_is_None(item['companytype'], "未知")
        registertime = if_is_None(item['registertime'], "无数据")
        commvalue = valueCommen.get(userid=userid)
        try:
            email = if_is_None(commvalue['email'], "暂缺")
            registranttime = if_is_None(commvalue['registranttime'], "这个嘛……")
            username = if_is_None(commvalue['username'], "出错")
            data.append({"userid": userid, "companyname": companyname, "companytype": companytype,
                         "registertime": registertime, "email": email, "registrantTime": registranttime, "username": username})
        except:
            print(userid+" was wrong")
    return JsonResponse({"data": data})


def govermentList(request):
    data = []
    valueGov = models.GovUser.objects.values("userid", "govname", "govcode", "govtype")
    valueCommen = models.User.objects.values("userid", "email", "registranttime", "username")
    for item in valueGov:
        userid = item['userid']
        govname = if_is_None(item['govname'], "无记录")
        govcode = if_is_None(item['govcode'], "未知")
        govType = if_is_None(item['govtype'], "无数据")
        commvalue = valueCommen.get(userid=userid)
        try:
            email = if_is_None(commvalue['email'], "暂缺")
            registranttime = if_is_None(commvalue['registranttime'], "这个嘛……")
            username = if_is_None(commvalue['username'], "出错")
            data.append({"userid": userid, "govname": govname, "govcode": govcode,
                         "govType": govType, "email": email, "registrantTime": registranttime, "username": username})
        except:
            print(userid+" was wrong")
    return JsonResponse({"data": data})


def instituteList(request):
    data = []
    valueCompany = models.InstitutionUser.objects.values("userid", "institutionname", "institudecode", "institutionlevel", "institutiontype")
    valueCommen = models.User.objects.values("userid", "email", "registranttime", "username")
    for item in valueCompany:
        userid = item['userid']
        institutionname = if_is_None(item['institutionname'], "无记录")
        institudecode = if_is_None(item['institudecode'], "未知")
        institutionlevel = if_is_None(item['institutionlevel'], "无数据")
        institutiontype = if_is_None(item['institutiontype'], "无记录")
        commvalue = valueCommen.get(userid=userid)
        try:
            email = if_is_None(commvalue['email'], "暂缺")
            registranttime = if_is_None(commvalue['registranttime'], "这个嘛……")
            username = if_is_None(commvalue['username'], "出错")
            data.append({"userid": userid, "institutionname": institutionname, "institudecode": institudecode, "institutionlevel": institutionlevel,
                         "institutiontype": institutiontype, "email": email, "registrantTime": registranttime, "username": username})
        except:
            print(userid+" was wrong")
    return JsonResponse({"data": data})


def deleteUser(request):
    userid = request.GET.get("userid")
    try:
        models.User.objects.get(userid=userid).delete()
        return JsonResponse({"data": "success"})
    except:
        return JsonResponse({"data": "error"})