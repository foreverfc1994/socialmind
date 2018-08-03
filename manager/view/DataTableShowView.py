#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.shortcuts import render,redirect
# from visitor.models import User,Province,City,Area
# from visitor import models
from django.http import JsonResponse, HttpResponse
import json
from manager.mysqlNullWash import if_is_None, webType_to_strType
from django.views.decorators.csrf import csrf_exempt
from visitor.scripts.signin import *
from manager.scripts.sysscript import *
import pymysql  # 导入 pymysql

def yuandatashow(request):
    dataList = []
    print("┗|｀O′|┛ 嗷~~")
    # 打开数据库连接
    # db = pymysql.connect(host="localhost", user="root",
    #                      password="461834084", db="linshitongji", port=3306)
    db = pymysql.connect(host="192.168.100.103", user="root",
                         password="root", db="linshitongji", port=3306)

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    # 1.查询操作
    # 编写sql 查询语句  user 对应我的表名
    # sql = "select * from datatables"
    # sql2 = "select * from website_schema"
    sql ="select TABLE_NAME,SCHEMA_NAME,WebSite,WebsiteType,NUM_ROWS from datatables,website_schema where SCHEMA_NAME=SchemaName"
    try:
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        print("tableName", "schemaName", "webSite", "webSiteType", "dataVolum")
        # 遍历结果
        for row in results:
            tableName = row[0]
            schemaName = row[1]
            webSite = row[2]
            webSiteType = row[3]
            dataVolum = row[4]
            print(tableName, schemaName, webSite, webSiteType, dataVolum)
            dataList.append({"tableName":tableName,
                             "schemaName":schemaName,
                             "webSite":webSite,
                             "webSiteType":webSiteType,
                             "dataVolum":dataVolum})
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接
    data = {"data": dataList}
    return HttpResponse(json.dumps(data))