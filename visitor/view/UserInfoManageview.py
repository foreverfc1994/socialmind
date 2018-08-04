from django.shortcuts import render,redirect
from visitor.models import User,Province,City,Area
from visitor import models
from django.http import JsonResponse
from visitor import forms
from django.views.decorators.csrf import csrf_exempt
from visitor.scripts.signin import *
import logging
logger = logging.getLogger('visitor')
def profile(request):
    userid = request.session["user_id"]
    print("userid: "+userid)
    role = request.session["user_type"]
    print("role: " + role)
    username = request.session["user_name"]
    currentUser = models.User.objects.get(userid=userid)
    email = currentUser.email
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
                           "sex": sex, "phoneNumber": phoneNumber, "hobby": hobby,
                           "career": career, "realname": realName, "birthday": birthday})
        elif(role == "企业用户"):
            personalized_data = models.CompanyUser.objects.get(userid=userid)
            idfronturl = personalized_data.idfronturl
            idbackurl = personalized_data.idbackurl
            companyname = personalized_data.companyname
            businessLicenceId = personalized_data.businesslicenceid
            bussinessLicenceUrl = str(personalized_data.businesslicenceurl)
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
            return render(request, 'foreground/personalInformation.html',
                          {"userid": userid, "role": role, "username": username, "email": email,
                           "companyname": companyname, "companytype": companytype, "idfronturl": idfronturl,
                           "idbackurl": idbackurl, "businessLicenceId": businessLicenceId,
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
                          {"userid": userid, "role": role, "username": username, "email": email,
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
                           "institutionname": institutionname, "institutecode": institutecode,
                           "institutionlevel": institutionlevel, "institutiontype": institutiontype,
                           "interest": interest})
    except:
        return render(request, 'foreground/login.html')