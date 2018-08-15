from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from manager.scripts.sysscript import *
import pymysql  # 导入 pymysql
import json

def index(request):
    return render(request, 'background/index.html')
def login(request):
    return redirect('/logout/')
def bindexContent(request):
    data = {"data": "success"}
    return HttpResponse(json.dumps(data))

