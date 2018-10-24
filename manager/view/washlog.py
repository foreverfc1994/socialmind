#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import datetime
import logging
import json
import re

@csrf_exempt
def washlog(request):
    dataList = []
    loglist = []
    try:
        f = open('log/datawash.log', 'r', encoding='UTF-8')
        pattern1 = ''
        for line in f:
            time = re.search(r'^[0-9]{4,4}-[0-9]{2,2}-[0-9]{2,2} [0-9]{2,2}:[0-9]{2,2}:[0-9]{2,2}', line).group()
            pattern = re.search(r'\[[\s\S]*\] wash', line)
            # print(type(pattern))
            ms = re.sub(r' wash$', "", pattern.group())
            # print(pattern,type(pattern))
            ms = ms[1: -1]
            index = []
            for i, ch in enumerate(ms):
                if ch == ',' and len(index) < 5:
                    index.append(i)
            # print(ms)
            ls = []
            ls.append(ms[1: index[0] - 1])
            ls.append(ms[index[0] + 3: index[1] - 1])
            ls.append(ms[index[1] + 3:index[2] - 1])
            ls.append(ms[index[2] + 2: index[3]])
            ls.append(ms[index[3] + 3: index[4] - 1])
            ls.append(ms[index[4] + 3: -1])
            schemaname = ls[0]
            tablename = ls[1]
            adminname = ls[2]
            optype = ls[4]
            # 2018 - 0
            # 8 - 18
            # 23: 29:47, 380
            # rollback[
            #     'newsbbs', 'bbs_news_author', 'LRX', 87594, '撤回', 'insert into bbs_news_author select * from beifen_bbs_news_authorLRX0']
            # wash
            #
            # funcname =re.search(r' ^', line).group()
            funcname = "wash"
            changeitems = ls[3]
            opdetial = ls[5]
            loglist.append({
                "schemaname": schemaname,
                "tablename": tablename,
                "adminname": adminname,
                "optype": optype,
                "time": time,
                "changeitems": changeitems,
                "funcname": funcname,
                "opdetial": opdetial
            })
        f.close()

    except Exception as e:
        raise e
    data = {"data": loglist}
    return HttpResponse(json.dumps(data))