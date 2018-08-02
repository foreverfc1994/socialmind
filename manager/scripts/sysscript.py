import os
import json
import re
from manager.mysqlNullWash import if_is_None
from visitor import models
def readlog():
    f = open(r'log/socialmind.log', encoding='utf-8')
    logs = f.readlines()
    data = []
    for log in logs:
        logdata = log.split(' ')
        logtime = logdata[0] + ' ' + logdata[1]
        logfunName = logdata[-1].replace('\n', '') + '/views/' + logdata[2]
        message = log.split('[')[-1].split(']')[0].split(', ')
        userid = message[0].replace('\'', '')
        try:
            username = models.User.objects.get(userid=userid).username
        except:
            username = "暂缺"
        roleid = message[1].replace('\'', '')
        try:
            role = models.Role.objects.get(roleid=roleid).rolename
        except:
            role = "未知"
        askurl = '127.0.0.1:8000' + message[2].replace('\'', '')
        logfunLname = message[3].replace('\'', '')
        para = '无参数' if message[3] == '' else message[3]
        dic = {'logtime': logtime, 'logfunName': logfunName, 'userid': userid, 'role': role, 'askurl': askurl,
               'logfunLname': logfunLname, 'para': para, 'username': username}
        data.append(dic)
    return data, len(logs)

