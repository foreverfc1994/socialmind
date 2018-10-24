#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
import json
from manager.mysqlNullWash import if_is_None, webType_to_strType
from django.views.decorators.csrf import csrf_exempt
from visitor.scripts.signin import *
from manager.scripts.sysscript import *
import pymysql  # 导入 pymysql


def  eventshow(request):
    print("┗|｀O′|┛ 嗷~~")
    dataList = []
    db = pymysql.connect(host="localhost", user="root",
                         password="461834084", db="socialmind", port=3306)
    # 使用cursor()方法获取操作游标
    cur = db.cursor()
    # 1.查询操作
    sql = "select event.objectID,name,eventBeginTime,eventEndTime,place,event.introduction,eventSummary,count(articleID) articleNumber from object right join event on object.objectID=event.objectID left join article on event.objectID = article.objectID group by event.objectID;"
    try:
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        # print("eventID", "eventName", "eventBeginTime", "eventEndTime", "introduction", "eventSummary","articleNumber")
        # 遍历结果
        for row in results:
            eventID = row[0]
            eventName = row[1]
            eventBeginTime = row[2]
            eventEndTime = row[3]
            place = row[4]
            introduction = row[5]
            eventSummary = row[6]
            articleNumber = row[7]
            # print(eventID, eventName, eventBeginTime, eventEndTime, place, introduction,eventSummary,articleNumber)
            dataList.append({"eventID": eventID,
                             "eventName": eventName,
                             "eventBeginTime": eventBeginTime,
                             "eventEndTime": eventEndTime,
                             "place": place,
                             "introduction": introduction,
                             "eventSummary": eventSummary,
                            "articleNumber": articleNumber})
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接

    data = {"data": dataList}
    return HttpResponse(json.dumps(data))
def  objectshow(request):
    print("┗|｀O′|┛ 嗷~~")
    dataList = []
    user = models.User.objects.all()
    print(user)

    data = {"data": dataList}
    return HttpResponse(json.dumps(data))
def entitydata(request):
    import pymysql
    db = pymysql.connect('localhost', 'root', '461834084', 'socialmind', port=3306)
    cur = db.cursor()
    sql = 'select * from entity'
    cur.execute(sql)
    data = []
    entities = cur.fetchall()
    for entity in entities:
        dic = {}
        dic['entityid'] = entity[0]
        dic['entityname'] = entity[1]
        dic['entitytype'] = entity[2]
        articlelist = entity[3].split(',')
        dic['articles'] = len(articlelist)
        data.append(dic)
    db.close()
    return  JsonResponse({"data":data})
    pass

def delentity(request):
    pass