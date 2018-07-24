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
                    if user_type == "个人用户":
                        return redirect('person_index')
                    if user_type == "企业用户":
                        return redirect('com_index')
                    if user_type == "政府用户":
                        return redirect('gov_index')
                    if user_type == "事业单位用户":
                        return redirect('person_index')
                    else:
                        return redirect('/login/')
                else:
                    message ='密码错误'
            except:
                message = '无此用户'
        return render(request, 'foreground/login.html', {'message': message})

    return render(request, 'foreground/login.html')

def person_index(request):
    return render(request, 'foreground/person_index.html')
def com_index(request):
    return render(request, 'foreground/com_index.html')
def gov_index(request):
    return render(request, 'foreground/gov_index.html')
def govcom_index(request):
    return render(request, 'foreground/govcom_index.html')
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
            return redirect('/jump/')
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





def events(request):
    return render(request, 'foreground/events.html')

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

def test(request):
    return render(request, 'foreground/com_index.html')

def jump(request):
    return render(request, 'foreground/jump.html')