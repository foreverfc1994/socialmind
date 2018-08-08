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
@csrf_exempt
def yuanshujubiao(request):
    wangzhan = request.POST
    tablename = {}
    for i in wangzhan:
        tablename = json.loads(i)
    dataList = []
    print("┗|｀O′|┛ 嗷~~")
    # 打开数据库连接
    db = pymysql.connect(host="localhost", user="root",
                         password="461834084", db=tablename['sitename'], port=3306)
    # db = pymysql.connect(host="192.168.100.103", user="root",
    #                      password="root", db="linshitongji", port=3306)

    # 使用cursor()方法获取操作游标
    cur = db.cursor()

    # 1.查询操作
    # 编写sql 查询语句  user 对应我的表名
    # sql ="select TABLE_NAME,SCHEMA_NAME,WebSite,WebsiteType,NUM_ROWS from datatables,website_schema where SCHEMA_NAME=SchemaName"
    sql = "select * from "+tablename['tablename']
    sql2 = "SHOW COLUMNS FROM "+tablename['tablename']
    try:
        cur.execute(sql2)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        columns = []
        for row in results:
            columns.append(row[0])
        # print(columns)
        linshidiction = {}
        for row in columns:
            linshidiction[row] = row
        dataList.append(linshidiction)
        # print(dataList)
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录

        for row in results:
            i = 0
            diction = {}
            for col in row:
                diction[columns[i]] = col
                i = i+1
            # print(diction)
            dataList.append(diction)
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接
    data = {"data": dataList}
    # print(data)
    return HttpResponse(json.dumps(data))
@csrf_exempt
def xuanzewangzhan(request):
    dataList = []
    wangzhan  = request.POST
    val = ""
    for i in wangzhan:
        val=i
    tablenames = findtablenames(val)
    diction = {}
    for row in tablenames:
        # print(row[0])
        diction[row[0]] = row[0]
    dataList.append(diction)
    data = {"data": dataList}
    return HttpResponse(json.dumps(data))
def findtablenames(val):
    db = pymysql.connect(host="localhost", user="root",
                         password="461834084", db=val, port=3306)
    cur = db.cursor()
    sql = "show tables"
    try:
        cur.execute(sql)  # 执行sql语句
        results = cur.fetchall()  # 获取查询的所有记录
        return results
    except Exception as e:
        raise e
    finally:
        db.close()  # 关闭连接
