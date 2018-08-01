from visitor import models
import uuid
import os
from time import strftime,gmtime
from visitor.scripts import SysLog
def saveImg(img, userid, i):
    file_path = os.path.join('static', 'upload', str(userid)+"_"+str(i)+'.jpg')
    print(file_path)
    f = open(file_path, 'wb')
    print("mark")
    for chunk in img.chunks():
        f.write(chunk)
    f.close()
    return "static/"+str(userid)+"_"+str(i)+'.jpg'
def rollbackFunction(userid):
    models.CompanyUser.objects.filter(userid=userid).delete()
    models.User.objects.filter(userid=userid).delete()
def personUser(userdata):
    newuser = models.User()
    userid = uuid.uuid4()
    newuser.userid = userid
    newuser.username =userdata.get('username')
    newuser.password = userdata.get('pwd')
    newuser.email = userdata.get('email')
    role = models.Role.objects.get(rolename='个人')
    newuser.roleid = role
    newuser.usertype = '个人用户'
    newuser.registrantid = userdata.get('idcard')
    newuser.isauthenticated = '0'
    address = ''
    try:
        address = address+userdata.get('province')
    except:
        pass
    try:
        address = address+' '+userdata.get('city')
    except:
        pass
    try:
        address = address+' '+userdata.get('country')
    except:
        pass
    newuser.address = address
    newuser.registranttime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    newuser.save()
    newperson = models.PersonUser()
    newperson.userid = newuser
    newperson.sex = userdata.get('sex')
    newperson.birthday = userdata.get('birthday')
    newperson.phonenumber = userdata.get('phone')
    newperson.hobby = userdata.get('interest')
    newperson.career = userdata.get('job')
    newperson.realname = userdata.get('realname')
    newperson.save()

def companyUser(request):
    userdata = request.POST
    newuser = models.User()
    userid = uuid.uuid4()
    newuser.userid = userid
    newuser.username = userdata.get('username')
    newuser.password = userdata.get('pwd')
    newuser.email = userdata.get('email')
    newuser.usertype = "企业用户"
    newuser.registrantid = userdata.get('idcard')
    newuser.isauthenticated = '0'
    address = ''
    try:
        address = address + userdata.get('province')
    except:
        pass
    try:
        address = address + ' ' + userdata.get('city')
    except:
        pass
    try:
        address = address + ' ' + userdata.get('country')
    except:
        pass
    newuser.address = address
    role = models.Role.objects.get(rolename='企业')
    newuser.roleid = role
    newuser.registranttime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    newuser.save()
    newCompanyUser = models.CompanyUser()
    foreignUserid = models.User.objects.get(userid=userid)
    newCompanyUser.userid = foreignUserid
    newCompanyUser.realname = userdata.get('realname')
    newCompanyUser.companyname = userdata.get('companyname')
    newCompanyUser.companytype = userdata.get('companytype')
    idcardA = request.FILES['idcardA']
    idcardB = request.FILES['idcardB']
    licence = request.FILES['licence']
    newCompanyUser.idfronturl=saveImg(idcardA, userid, "1")
    newCompanyUser.idbackurl = saveImg(idcardB, userid, "2")
    newCompanyUser.businesslicenceurl = saveImg(licence, userid, "3")
    newCompanyUser.businesslicenceid = userdata.get('licenceid')
    newCompanyUser.businessscope = userdata.get('shop_scope')
    newCompanyUser.interest = userdata.get('interest')
    newCompanyUser.registerorg = userdata.get('register_ins')
    newCompanyUser.registertime = userdata.get('birthday')
    newCompanyUser.save()


def govUser(request):
    userdata = request.POST
    newuser = models.User()
    userid = uuid.uuid4()
    newuser.userid = userid
    newuser.username = userdata.get('username')
    newuser.password = userdata.get('pwd')
    newuser.email = userdata.get('email')
    newuser.usertype = "政府用户"
    newuser.registrantid = userdata.get('idcard')
    newuser.isauthenticated = '0'
    address = ''
    try:
        address = address + userdata.get('province')
    except:
        pass
    try:
        address = address + ' ' + userdata.get('city')
    except:
        pass
    try:
        address = address + ' ' + userdata.get('country')
    except:
        pass
    newuser.address = address
    role = models.Role.objects.get(rolename='企业')
    newuser.roleid = role
    newuser.registranttime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    newuser.save()
    newGovUser = models.GovUser()
    foreignUserid = models.User.objects.get(userid=userid)
    newGovUser.userid = foreignUserid
    newGovUser.govname = userdata.get('gov-name')
    newGovUser.govtype = userdata.get('gov-type')
    newGovUser.govcode = userdata.get('gov-code')
    idcardA = request.FILES['idcardA']
    idcardB = request.FILES['idcardB']
    newGovUser.idfronturl = saveImg(idcardA, userid, "1")
    newGovUser.idbackurl = saveImg(idcardB, userid, "2")
    newGovUser.idcard = userdata.get('idcard')
    newGovUser.realname = userdata.get('realname')
    newGovUser.interest = userdata.get('interest')
    newGovUser.save()

def InstitutionUser(request):
    userdata = request.POST
    newuser = models.User()
    userid = uuid.uuid4()
    newuser.userid = userid
    newuser.username = userdata.get('username')
    newuser.password = userdata.get('pwd')
    newuser.email = userdata.get('email')
    newuser.usertype = "事业单位用户"
    newuser.registrantid = userdata.get('idcard')
    newuser.isauthenticated = '0'
    address = ''
    try:
        address = address + userdata.get('province')
    except:
        pass
    try:
        address = address + ' ' + userdata.get('city')
    except:
        pass
    try:
        address = address + ' ' + userdata.get('country')
    except:
        pass
    newuser.address = address
    role = models.Role.objects.get(rolename='事业单位')
    newuser.roleid = role
    newuser.registranttime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    newuser.save()
    newInUser = models.InstitutionUser()
    foreignUserid = models.User.objects.get(userid=userid)
    newInUser.userid = foreignUserid
    newInUser.realname = userdata.get('realname')
    newInUser.institutionname = userdata.get('in-name')
    newInUser.institutionlevel = userdata.get('in-level')
    newInUser.institutiontype = userdata.get('in-type')
    newInUser.institudecode = userdata.get('in-code')
    newInUser.interest = userdata.get('interest')
    idcardA = request.FILES['idcardA']
    idcardB = request.FILES['idcardB']
    institude = request.FILES['in-photo']
    newInUser.idfronturl = saveImg(idcardA, userid, "1")
    newInUser.idbackurl = saveImg(idcardB, userid, "2")
    newInUser.institudeurl = saveImg(institude, userid, "3")
    newInUser.save()

    pass



