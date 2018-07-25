from visitor import models
import uuid
import os
from time import strftime,gmtime
def saveimg(img):
    file_path = os.path.join('static','upload',img.name)
    f = open(file_path, 'wb')
    for chunk in img.chunks():
        f.write(chunk)
    f.close()
    pass
def personuser(userdata):
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
def companyuser(userdata):
    print(userdata)

    pass