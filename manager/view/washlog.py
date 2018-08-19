#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import time,datetime
import logging
import json
import re

@csrf_exempt
def washlog(request):
    dataList = []

    # try:
    #     f = open('log/datawash.log', 'r', encoding='UTF-8')
    #     pattern1 = ''
    #     for line in f:
    #         zongrizhiliang = zongrizhiliang + 1
    #         pattern = re.search(r'^[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2} [0-9]{2,2}:[0-9]{2,2}:[0-9]{2,2}', line).group()
    #         patternshijianchuo = datetime.datetime.strptime(pattern, "%Y-%m-%d %H:%M:%S").strftime("%Y-%m-%d")
    #         patternshijianchuo = time.mktime(time.strptime(patternshijianchuo, "%Y-%m-%d"))
    #         # print(type(yesterdayshijianchuo),type(patternshijianchuo))
    #         if yesterdayshijianchuo <= patternshijianchuo:
    #             yesterdayrizhiliang = yesterdayrizhiliang + 1
    #         for index in range(len(datelist)):
    #             strzhuandatetime = datetime.datetime.strptime(pattern, "%Y-%m-%d %H:%M:%S")
    #             datetimezhuanstr = strzhuandatetime.strftime("%m.%d")
    #             if datetimezhuanstr == datelist[index]:
    #                 logdatelist[index] = logdatelist[index] + 1
    #     f.close()
    # except Exception as e:
    #     raise e
    data = {"data": dataList}
    return HttpResponse(json.dumps(data))