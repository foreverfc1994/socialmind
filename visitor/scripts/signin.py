from visitor import models
import uuid
import os
from time import strftime,gmtime
def saveImg(img, userid, i):
    file_path = os.path.join('static', 'upload', str(userid)+"_"+str(i)+'.jpg')
    print(file_path)
    f = open(file_path, 'wb')
    print("mark")
    for chunk in img.chunks():
        f.write(chunk)
    f.close()
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
    newuser.usertype = '个人'
    newuser.registrantid = userdata.get('idcard')
    newuser.isauthenticated = '0'
    address = ''
    try:
        address = address+userdata.get('province')
    except:
        pass
    try:
        address = address+''+userdata.get('city')
    except:
        pass
    try:
        address = address+''+userdata.get('area')
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

def companyUser(userdata):
    newuser = models.User()
    userid = uuid.uuid4()
    newuser.userid = userid
    newuser.username = userdata.get('username')
    newuser.password = userdata.get('pwd')
    newuser.email = userdata.get('companyemail')
    newuser.usertype = "个人"
    newuser.registrantid = userdata.get('idcard')
    newuser.isauthenticated = '0'
    address = ''
    try:
        address = address + userdata.get('province')
    except:
        pass
    try:
        address = address + '' + userdata.get('city')
    except:
        pass
    try:
        address = address + '' + userdata.get('area')
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
    newCompanyUser.bossname = userdata.get('bossname')
    newCompanyUser.companyname = userdata.get('companyname')
    newCompanyUser.idfronturl = "static/"+str(userid)+"_"+"1"+'.jpg'
    newCompanyUser.idbackurl = "static/"+str(userid)+"_"+"2"+'.jpg'
    newCompanyUser.businesslicenceurl = "static/"+str(userid)+"_"+"3"+'.jpg'
    newCompanyUser.type = userdata.get('companytype')
    newCompanyUser.businesslicenceid = userdata.get('businessLicenceId')
    newCompanyUser.save()
    return userid

def govUser(userdata):
    newuser = models.User()
    userid = uuid.uuid4()
    newuser.userid = userid
    newuser.username = userdata.get('username')
    newuser.password = userdata.get('pwd')
    newuser.email = userdata.get('companyemail')
    newuser.usertype = "政府"
    newuser.registrantid = userdata.get('idcard')
    newuser.isauthenticated = '0'
    address = ''
    try:
        address = address + userdata.get('province')
    except:
        pass
    try:
        address = address + '' + userdata.get('city')
    except:
        pass
    try:
        address = address + '' + userdata.get('area')
    except:
        pass
    newuser.address = address
    role = models.Role.objects.get(rolename='政府')
    newuser.roleid = role
    newuser.registranttime = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    newuser.save()