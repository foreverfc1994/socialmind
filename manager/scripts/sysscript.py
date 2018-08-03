import os
import json
import re
def readlog():
    f = open(r'log/socialmind.log',encoding='utf-8')
    logs = f.readlines()
    data = []
    for log in logs:
        logdata = log.split(' ')
        logtime = logdata[0] + ' ' + logdata[1]
        logfunName = logdata[-1].replace('\n', '') + '/views/' + logdata[2]
        message = log.split('[')[-1].split(']')[0].split(', ')
        userid = message[0].replace('\'', '')
        roleid = message[1].replace('\'', '')
        askurl = '127.0.0.1:8000' + message[2].replace('\'', '')
        logfunLname = message[3].replace('\'', '')
        para = '无参数' if message[3] == '' else message[3]
        dic = {'logtime': logtime, 'logfunName': logfunName, 'userid': userid, 'roleid': roleid, 'askurl': askurl,
               'logfunLname': logfunLname, 'para': para}
        data.append(dic)
    f.close()
    return data

