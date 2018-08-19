from django.shortcuts import render,redirect
from visitor.models import User,Province,City,Area
from visitor import models
from django.http import JsonResponse, HttpResponse
from visitor import forms
from django.views.decorators.csrf import csrf_exempt
from visitor.scripts.signin import *
import time
import os
import logging
import json
logger = logging.getLogger('visitor')
@csrf_exempt
def ComUsrForm(request,a):
    print(request.POST)
    userid = request.session["user_id"]
    if(a == 1):
        dataList = []
        companydata = request.POST
        comName = companydata.get('comName')
        comType = companydata.get('comType')
        comaddress = companydata.get('comaddress')
        businessscope = companydata.get('businessscope')
        interest = companydata.get('interest')
        businessID = companydata.get('businessID')
        date = companydata.get('date')
        businesspic = companydata.get('businesspic')
        registerORG = companydata.get('registerORG')
        isAu = companydata.get('isAu')
        Qiyexiangguan = models.CompanyUser.objects.get(userid=userid)
        Usr = models.User.objects.get(userid=userid)
        Qiyexiangguan.companyname = comName
        Qiyexiangguan.companytype = comType
        Usr.address = comaddress
        Qiyexiangguan.businessscope = businessscope
        Qiyexiangguan.interest = interest
        Qiyexiangguan.businesslicenceid = businessID
        Qiyexiangguan.registertime = date
        Qiyexiangguan.businesslicenceurl = businesspic
        Qiyexiangguan.registerorg = registerORG
        Usr.isauthenticated = isAu
        Qiyexiangguan.save()
        Usr.save()
        Qiyexiangguan = models.CompanyUser.objects.get(userid=userid)
        Usr = models.User.objects.get(userid=userid)
        dataList.append({"companyname": Qiyexiangguan.companyname,
                         "companytype": Qiyexiangguan.companytype,
                         "address":Usr.address,
                         "businessscope": Qiyexiangguan.businessscope,
                         "interest":Qiyexiangguan.interest,
                         "businessLicenceId":Qiyexiangguan.businesslicenceid,
                         "registertime": Qiyexiangguan.registertime,
                         "bussinessLicenceUrl": Qiyexiangguan.businesslicenceurl,
                         "isAu": Usr.isauthenticated,
                         "registerORG": Qiyexiangguan.registerorg,
                         })
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))
    elif(a == 2):
        dataList = []
        userdata = request.POST
        usrname = userdata.get('username')
        psw = userdata.get('newpassword')
        Usrdenglu = models.User.objects.get(userid=userid)
        Usrdenglu.username = usrname
        Usrdenglu.password = psw
        Usrdenglu.save()
        currentUser = models.User.objects.get(userid=userid)
        username = currentUser.username
        password = currentUser.password
        dataList.append({"usrname": username, "psw": password})
        data = {"data": dataList}
        # personalInfoForm(request)
        # return redirect('/personalInfoForm/')
        return HttpResponse(json.dumps(data))
    elif(a == 3):
        dataList = []
        print(request.POST)
        persondata = request.POST
        realname = persondata.get('realname')
        # usrimg = persondata.get('usrimg')
        usrimg1 = request.FILES['usrimg1']

        mail = persondata.get('mail')
        IDcardNum = persondata.get('IDcardNum')
        IDcardfront = persondata.get('IDcardfront')
        IDcardback = persondata.get('IDcardback')
        registranttime = persondata.get('registranttime')
        Qiyexiangguan = models.CompanyUser.objects.get(userid=userid)
        Usr = models.User.objects.get(userid=userid)
        Qiyexiangguan.realname = realname
        Usr.photo = saveImg(usrimg1, userid, "4")
        Usr.email = mail
        Usr.registrantid = IDcardNum
        Qiyexiangguan.idfronturl = IDcardfront
        Qiyexiangguan.idbackurl = IDcardback
        Usr.registranttime = registranttime
        Qiyexiangguan.save()
        Usr.save()
        Qiyexiangguan = models.CompanyUser.objects.get(userid=userid)
        Usr = models.User.objects.get(userid=userid)
        dataList.append({"realname": Qiyexiangguan.realname,
                         "usrimg": Usr.photo,
                         "mail": Usr.email,
                         "IDcardNum": Usr.registrantid,
                         "IDcardfront": Qiyexiangguan.idfronturl,
                         "IDcardback": Qiyexiangguan.idbackurl,
                         "registranttime": Usr.registranttime
                         })
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))
def PersonUsrForm(request,a):
    userid = request.session["user_id"]
    if (a == 2):
        dataList = []
        usrdata = request.POST
        currentUser = models.User.objects.get(userid=userid)
        currentUser.username = usrdata.get('username')
        currentUser.password = usrdata.get('newpassword')
        currentUser.save()
        currentUser = models.User.objects.get(userid=userid)
        dataList.append({'username':currentUser.username,
                         'password':currentUser.password})
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))
    elif (a == 3):
        dataList = []
        usrdata = request.POST
        currentUser = models.User.objects.get(userid=userid)
        deepinfo = models.PersonUser.objects.get(userid=userid)
        deepinfo.realname = usrdata.get('realname')
        currentUser.photo= usrdata.get('usrimg')
        deepinfo.sex = usrdata.get('gender')
        deepinfo.birthday = usrdata.get('birthday')
        deepinfo.career = usrdata.get('job')
        deepinfo.hobby = usrdata.get('hobby')
        deepinfo.phonenumber = usrdata.get('phone')
        currentUser.email = usrdata.get('mail')
        currentUser.address = usrdata.get('address')
        currentUser.registranttime = usrdata.get('registranttime')
        currentUser.save()
        deepinfo.save()
        currentUser = models.User.objects.get(userid=userid)
        deepinfo = models.PersonUser.objects.get(userid=userid)
        dataList.append({'realname': deepinfo.realname,
                         'usrimg': currentUser.photo,
                         'gender': deepinfo.sex,
                         'birthday': deepinfo.birthday,
                         'career': deepinfo.career,
                         'hobby': deepinfo.hobby,
                         'phone': deepinfo.phonenumber,
                         'email': currentUser.email,
                         'address': currentUser.address,
                         'registranttime': currentUser.registranttime})
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))
def InstituUsrForm(request,a):
    userid = request.session["user_id"]
    if (a == 1):
        dataList = []
        usrdata = request.POST
        currentUser = models.User.objects.get(userid=userid)
        currentUser.username = usrdata.get('username')
        currentUser.password = usrdata.get('password')
        currentUser.save()
        currentUser = models.User.objects.get(userid=userid)
        dataList.append({'username': currentUser.username,
                         'password': currentUser.password})
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))
def GovUsrForm(request,a):
    userid = request.session["user_id"]
    if (a == 2):
        dataList = []
        usrdata = request.POST
        currentUser = models.User.objects.get(userid=userid)
        currentUser.username = usrdata.get('username')
        currentUser.password = usrdata.get('password')
        currentUser.save()
        currentUser = models.User.objects.get(userid=userid)
        dataList.append({'username': currentUser.username,
                         'password': currentUser.password})
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))
    elif (a == 3):
        dataList = []
        usrdata = request.POST
        currentUser = models.User.objects.get(userid=userid)
        currentUser.username = usrdata.get('username')
        currentUser.password = usrdata.get('password')
        currentUser.save()
        currentUser = models.User.objects.get(userid=userid)
        dataList.append({'username': currentUser.username,
                         'password': currentUser.password})
        data = {"data": dataList}
        return HttpResponse(json.dumps(data))

def ajaxInitComUsrForm(request):
    dataList = []
    userid = request.session["user_id"]
    role = request.session["user_type"]
    # username = request.session["user_name"]
    currentUser = models.User.objects.get(userid=userid)
    username = currentUser.username
    email = currentUser.email
    psw = currentUser.password
    IDcard = currentUser.registrantid
    photo = giveimgurl(currentUser.photo)
    personalized_data = models.CompanyUser.objects.get(userid=userid)
    idfronturl = giveimgurl(personalized_data.idfronturl)
    idbackurl = giveimgurl(personalized_data.idbackurl)
    companyname = personalized_data.companyname
    businessLicenceId = personalized_data.businesslicenceid
    bussinessLicenceUrl = giveimgurl(str(personalized_data.businesslicenceurl))
    businessscope = personalized_data.businessscope
    companytype = personalized_data.companytype
    interest = personalized_data.interest
    realname = personalized_data.realname
    # 登记机关
    registerORG = personalized_data.registerorg
    # 登记时间
    registertime = personalized_data.registertime
    address = currentUser.address
    # 注册账号时间
    registranttime = currentUser.registranttime
    dataList.append({"username": username
                        ,"psw": psw
                        ,"role": role
                        ,"IDcard": IDcard
                        , "email": email
                        , "idfronturl": idfronturl
                        , "idbackurl": idbackurl
                        , "companyname": companyname
                        , "businessLicenceId": businessLicenceId
                        , "bussinessLicenceUrl": bussinessLicenceUrl
                        , "businessscope": businessscope
                        , "companytype": companytype
                        , "interest": interest
                        , "realname": realname
                        , "registerORG": registerORG
                        , "registertime": registertime
                        , "address": address
                        ,"isAu": currentUser.isauthenticated
                        , "registranttime": registranttime
                        , "usrimg": photo
                     })
    data = {"data": dataList}
    print(data)
    return HttpResponse(json.dumps(data))
def personalInfoForm(request,a):
    userid = request.session["user_id"]
    if(a == 1):
        return render(request, 'foreground/PersonUsrInfoForm.html')
    elif (a == 2):
        return render(request, 'foreground/CompanyUsrInfoForm.html')
    elif (a == 3):
        return render(request, 'foreground/GovUsrInfoForm.html')
    elif (a == 4):
        return render(request, 'foreground/CompanyUsrInfoForm.html')

def giveimgurl(url):
    try:
        if(url[:7] == "static/"):
            newurl = "/static/upload/"
            newurl += url[7:]
            print(newurl)
        else:
            newurl = url
        return newurl
    except:
        return "/static/upload/test.jpg"
def profile(request):
    userid = request.session["user_id"]
    print("userid: "+userid)
    role = request.session["user_type"]
    print("role: " + role)
    username = request.session["user_name"]
    currentUser = models.User.objects.get(userid=userid)
    email = currentUser.email
    photo = giveimgurl(currentUser.photo)
    try:
        if(role == "个人用户"):
            personalized_data = models.PersonUser.objects.get(userid=userid)
            sex = personalized_data.sex
            birthday = personalized_data.birthday
            phoneNumber = personalized_data.phonenumber
            hobby = personalized_data.hobby
            career = personalized_data.career
            realName = personalized_data.realname
            return render(request, 'foreground/personalInformation.html',
                          {"userid": userid, "role": role, "username": username, "email": email,
                           "sex": sex, "phoneNumber": phoneNumber, "hobby": hobby,"photo":photo,
                           "career": career, "realname": realName, "birthday": birthday})
        elif(role == "企业用户"):
            personalized_data = models.CompanyUser.objects.get(userid=userid)
            idfronturl = giveimgurl(personalized_data.idfronturl)
            idbackurl = giveimgurl(personalized_data.idbackurl)
            companyname = personalized_data.companyname
            businessLicenceId = personalized_data.businesslicenceid
            bussinessLicenceUrl = giveimgurl(str(personalized_data.businesslicenceurl))
            businessscope = personalized_data.businessscope
            companytype = personalized_data.companytype
            interest = personalized_data.interest
            realname = personalized_data.realname
            # 登记机关
            registerORG = personalized_data.registerorg
            # 登记时间
            registertime = personalized_data.registertime
            address = currentUser.address
            #注册账号时间
            registranttime = currentUser.registranttime
            print(idfronturl)
            return render(request, 'foreground/personalInformation.html',
                          {"userid": userid, "role": role, "username": username, "email": email,
                           "companyname": companyname, "companytype": companytype, "idfronturl": idfronturl,
                           "idbackurl": idbackurl, "businessLicenceId": businessLicenceId,"photo":photo,
                           "bussinessLicenceUrl": bussinessLicenceUrl,"businessscope":businessscope,
                           "interest":interest,"realname":realname,"registerORG":registerORG,
                           "registertime":registertime,"address":address,"registranttime":registranttime})
        elif(role == "政府用户"):
            gov_User = models.GovUser.objects.get(userid=userid)
            govname = gov_User.govname
            govcode = gov_User.govcode
            # idfronturl = gov_User.idfronturl
            # idbackurl = gov_User.idbackurl
            govtype = gov_User.govtype
            interest = gov_User.interest
            return render(request, 'foreground/personalInformation.html',
                          {"userid": userid, "role": role, "username": username, "email": email,"photo":photo,
                           "govname": govname, "govcode": govcode, "govtype": govtype, "interest": interest})
        elif(role == "事业单位用户"):
            institu_User = models.InstitutionUser.objects.get(userid=userid)
            institutionname = institu_User.institutionname
            institutecode = institu_User.institudecode
            institutionlevel = institu_User.institutionlevel
            institutiontype = institu_User.institutiontype
            interest = institu_User.interest
            return render(request, 'foreground/personalInformation.html',
                          {"userid": userid, "role": role, "username": username, "email": email,
                           "institutionname": institutionname, "institutecode": institutecode,"photo":photo,
                           "institutionlevel": institutionlevel, "institutiontype": institutiontype,
                           "interest": interest})
    except:
        return render(request, 'foreground/login.html')

def ajaxInitPersonUsrForm(request):
    dataList = []
    userid = request.session["user_id"]
    role = request.session["user_type"]
    # username = request.session["user_name"]
    currentUser = models.User.objects.get(userid=userid)
    username = currentUser.username
    email = currentUser.email
    psw = currentUser.password
    IDcard = currentUser.registrantid
    photo = giveimgurl(currentUser.photo)
    address = currentUser.address
    registranttime = currentUser.registranttime

    personalized_data = models.PersonUser.objects.get(userid=userid)
    realname = personalized_data.realname
    gender = "暂缺"
    if(personalized_data.sex == "1"):
        gender = "男"
    elif(personalized_data.sex == "2"):
        gender = "女"
    birthday = personalized_data.birthday
    phone = personalized_data.phonenumber
    hobby = personalized_data.hobby
    career = personalized_data.career

    dataList.append({"username": username
                        , "psw": psw
                        , "role": role
                        , "IDcard": IDcard
                        , "email": email
                        , "gender": gender
                        , "birthday": birthday
                        , "phone": phone
                        , "hobby": hobby
                        , "career": career
                        , "realname": realname
                        , "address": address
                        , "isAu": currentUser.isauthenticated
                        , "registranttime": registranttime
                        , "usrimg": photo
                     })
    data = {"data": dataList}
    print(data)
    return HttpResponse(json.dumps(data))
def ajaxInitInstitutionUsrForm(request):
    dataList = []
    userid = request.session["user_id"]
    role = request.session["user_type"]
    # username = request.session["user_name"]
    currentUser = models.User.objects.get(userid=userid)
    username = currentUser.username
    email = currentUser.email
    psw = currentUser.password
    IDcard = currentUser.registrantid
    photo = currentUser.photo
    personalized_data = models.CompanyUser.objects.get(userid=userid)
    idfronturl = giveimgurl(personalized_data.idfronturl)
    idbackurl = giveimgurl(personalized_data.idbackurl)
    companyname = personalized_data.companyname
    businessLicenceId = personalized_data.businesslicenceid
    bussinessLicenceUrl = giveimgurl(str(personalized_data.businesslicenceurl))
    businessscope = personalized_data.businessscope
    companytype = personalized_data.companytype
    interest = personalized_data.interest
    realname = personalized_data.realname
    # 登记机关
    registerORG = personalized_data.registerorg
    # 登记时间
    registertime = personalized_data.registertime
    address = currentUser.address
    # 注册账号时间
    registranttime = currentUser.registranttime
    dataList.append({"username": username
                        , "psw": psw
                        , "role": role
                        , "IDcard": IDcard
                        , "email": email
                        , "idfronturl": idfronturl
                        , "idbackurl": idbackurl
                        , "companyname": companyname
                        , "businessLicenceId": businessLicenceId
                        , "bussinessLicenceUrl": bussinessLicenceUrl
                        , "businessscope": businessscope
                        , "companytype": companytype
                        , "interest": interest
                        , "realname": realname
                        , "registerORG": registerORG
                        , "registertime": registertime
                        , "address": address
                        , "isAu": currentUser.isauthenticated
                        , "registranttime": registranttime
                        , "usrimg": photo
                     })
    data = {"data": dataList}
    return HttpResponse(json.dumps(data))
def ajaxInitGovUsrForm(request):
    dataList = []
    userid = request.session["user_id"]
    role = request.session["user_type"]
    # username = request.session["user_name"]
    currentUser = models.User.objects.get(userid=userid)
    username = currentUser.username
    email = currentUser.email
    psw = currentUser.password
    IDcard = currentUser.registrantid
    photo = currentUser.photo
    personalized_data = models.CompanyUser.objects.get(userid=userid)
    idfronturl = giveimgurl(personalized_data.idfronturl)
    idbackurl = giveimgurl(personalized_data.idbackurl)
    companyname = personalized_data.companyname
    businessLicenceId = personalized_data.businesslicenceid
    bussinessLicenceUrl = giveimgurl(str(personalized_data.businesslicenceurl))
    businessscope = personalized_data.businessscope
    companytype = personalized_data.companytype
    interest = personalized_data.interest
    realname = personalized_data.realname
    # 登记机关
    registerORG = personalized_data.registerorg
    # 登记时间
    registertime = personalized_data.registertime
    address = currentUser.address
    # 注册账号时间
    registranttime = currentUser.registranttime
    dataList.append({"username": username
                        , "psw": psw
                        , "role": role
                        , "IDcard": IDcard
                        , "email": email
                        , "idfronturl": idfronturl
                        , "idbackurl": idbackurl
                        , "companyname": companyname
                        , "businessLicenceId": businessLicenceId
                        , "bussinessLicenceUrl": bussinessLicenceUrl
                        , "businessscope": businessscope
                        , "companytype": companytype
                        , "interest": interest
                        , "realname": realname
                        , "registerORG": registerORG
                        , "registertime": registertime
                        , "address": address
                        , "isAu": currentUser.isauthenticated
                        , "registranttime": registranttime
                        , "usrimg": photo
                     })
    data = {"data": dataList}
    return HttpResponse(json.dumps(data))

def saveImg(img, userid, i):
    file_path = os.path.join('static', 'upload', str(userid)+"_"+str(i)+'.jpg')
    print(file_path)
    f = open(file_path, 'wb')
    print("mark")
    for chunk in img.chunks():
        f.write(chunk)
    f.close()
    return "static/"+str(userid)+"_"+str(i)+'.jpg'