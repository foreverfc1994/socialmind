from django.shortcuts import render,redirect
from django.http import JsonResponse, HttpResponse
from manager.scripts.sysscript import *

def index(request):
    return render(request, 'background/index.html')
def login(request):
    return redirect('/logout/')

