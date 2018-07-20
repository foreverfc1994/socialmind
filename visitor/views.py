from django.shortcuts import render,redirect
from visitor.models import User,Province,City,Area
from visitor import models
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from visitor.scripts.signin import *
# Create your views here.
def login(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        message = ''
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user_type = request.POST.get('user-type')
        if username and password:
            username = username.strip()
            try:
                user = models.User.objects.get(username=username)
                if user.password == password:
                    return  redirect('/index/')
                else:
                    message ='密码错误'
            except:
                message = '无此用户'
        return render(request, 'foreground/login.html', {'message': message})

    return render(request, 'foreground/login.html')

def index(request):
    return render(request, 'foreground/index.html')
def test(request):
    return render(request, 'foreground/signin.html')
    pass
def signin(request):
    print(request.POST)
    if request.method == 'POST':
        userdata = request.POST
        print(type(userdata))
        if userdata.get('user-type')=='0':
            personuser(userdata)
        elif userdata.get('user-type')=='1':
            files = request.FILES['idcardA']
            saveimg(files)
            companyuser(userdata)

    return render(request, 'foreground/signin.html')

def get_address(request):
    provinces=Province.objects.all()
    cities = City.objects.all()
    areas = Area.objects.all()
    citydic = {}
    for city in cities:
        citycode = city.code[:4]
        arealist = []
        for area in areas:
            if area.code[:4] == citycode:
                arealist.append(area.name)
        citydic[city.name] = arealist
    prodic = {}
    for province in provinces:
        procode = province.code[:2]
        citylist = {}
        for city in cities:
            if city.code[:2] == procode:
                citylist[city.name] = citydic[city.name]
        prodic[province.name] = citylist
    return JsonResponse({'data': prodic})

def heatIndex(request):
    return render(request, 'foreground/heatIndex.html')
def heatIndex0(request):
    return render(request, 'foreground/heatIndexPages/heatIndex0.html')
def heatIndex1(request):
    return render(request, 'foreground/heatIndexPages/heatIndex1.html')
def heatIndex2(request):
    return render(request, 'foreground/heatIndexPages/heatIndex2.html')
def heatIndex3(request):
    return render(request, 'foreground/heatIndexPages/heatIndex3.html')
def heatIndex4(request):
    return render(request, 'foreground/heatIndexPages/heatIndex4.html')
def heatIndex5(request):
    return render(request, 'foreground/heatIndexPages/heatIndex5.html')

def emotionMap(request):
    return render(request, 'foreground/emotionMap.html')
def emotionMap0(request):
    return render(request, 'foreground/emotionMap/emotionMap0.html')
def emotionMap1(request):
    return render(request, 'foreground/emotionMap/emotionMap1.html')
def emotionMap2(request):
    return render(request, 'foreground/emotionMap/emotionMap2.html')
def emotionMap3(request):
    return render(request, 'foreground/emotionMap/emotionMap3.html')
def emotionMap4(request):
    return render(request, 'foreground/emotionMap/emotionMap4.html')

def informationMonitor(request):
    return render(request, 'foreground/informationMonitor.html')
def informationMonitor0(request):
    return render(request, 'foreground/informationmonitor/informationMonitor0.html')
def informationMonitor1(request):
    return render(request, 'foreground/informationmonitor/informationMonitor1.html')
def informationMonitor2(request):
    return render(request, 'foreground/informationmonitor/informationMonitor2.html')
def informationMonitor3(request):
    return render(request, 'foreground/informationmonitor/informationMonitor3.html')

def fullTextMonitor(request):
    return render(request, 'foreground/fullTextMonitor.html')

def events(request):
    return render(request, 'foreground/events.html')
def event0(request):
    return render(request, 'foreground/event/event0.html')
def event1(request):
    return render(request, 'foreground/event/event1.html')
def event2(request):
    return render(request, 'foreground/event/event2.html')
def event3(request):
    return render(request, 'foreground/event/event3.html')
def event4(request):
    return render(request, 'foreground/event/event4.html')
def event5(request):
    return render(request, 'foreground/event/event5.html')

def reportMaker(request):
    return render(request, 'foreground/reportMaker.html')

def profile(request):
    return render(request, 'foreground/profile.html')

def eventparticular(request):
    return render(request, 'foreground/particular.html')

def fileParticular(request):
    return render(request, 'foreground/file.html')

@csrf_exempt
def checkuser(request):
    username = request.POST.get('user')
    count = models.User.objects.filter(username=username).count()
    if count==0:
        msg = 1
    else:
        msg = 0
    return JsonResponse({'msg':msg})