from django.shortcuts import render,redirect
from visitor.models import User,Province,City,Area
from django.http import JsonResponse
# Create your views here.
def login(request):
    print(request.method)
    if request.method == 'POST':
        print(request.POST)
        message=''
        username = request.POST.get('username',None)
        password = request.POST.get('password',None)
        user_type = request.POST.get('user-type')
        if username and password:
            username = username.strip()

    return render(request,'foreground/login.html')

def index(request):
    return render(request,'foreground/index.html')

def signin(request):
    if request.method == 'POST':
        print(request.POST)
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