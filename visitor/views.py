from django.shortcuts import render, redirect
from visitor.models import Province, City, Area
from visitor import models
from django.http import JsonResponse
from visitor import forms
from django.views.decorators.csrf import csrf_exempt
from visitor.scripts.signin import *
# Create your views here.
# from visitor.scripts.SysLog import Logger
import random
from manager.mysqlNullWash import if_is_None
import logging
logger = logging.getLogger('visitor')
# def login(request):
#     print(request.method)
#     # print(request.META)
#     if request.session.get('is_login',None):
#         return redirect('/person_index/')
#     if request.method == 'POST':
#         print(request.POST)
#         message = ''
#         login_form = forms.loginForm(request.POST)
#         if login_form.is_valid():
#             username = login_form.cleaned_data['username']
#             password = login_form.cleaned_data['password']
#             user_type = login_form.cleaned_data['usertype']
#             try:
#                 user = models.User.objects.get(username=username)
#                 if user_type==user.usertype:
#                     if user.password == password:
#                         request.session['is_login'] = True
#                         request.session['user_id'] = user.pk
#                         request.session['user_name'] = user.username
#                         request.session['user_type'] = user_type
#                         request.session['user_role'] = user.roleid.roleid
#                         # logger = Logger(username).getlogger()
#
#                         if user_type == "个人用户":
#                             logdata = [request.session['user_id'],request.session['user_role'],'/person_index/','登录','']
#                             logger.debug(logdata)
#                             return redirect('person_index')
#                         if user_type == "企业用户":
#                             logdata = [request.session['user_id'],request.session['user_role'], '/com_index/', '登录', '']
#                             logger.debug(logdata)
#                             return redirect('com_index')
#                         if user_type == "政府用户":
#                             logdata = [request.session['user_id'],request.session['user_role'], '/gov_index/', '登录', '']
#                             logger.debug(logdata)
#                             return redirect('gov_index')
#                         if user_type == "事业单位用户":
#                             logdata = [request.session['user_id'],request.session['user_role'], '/govcom_index/', '登录', '']
#                             logger.debug(logdata)
#                             return redirect('govcom_index')
#                         if user_type == '管理员':
#                             logdata = [request.session['user_id'],request.session['user_role'], '/bindex/', '登录', '']
#                             logger.debug(logdata)
#                             return redirect('index')
#                         else:
#                             return redirect('/login/')
#                     else:
#                         message = '密码错误'
#                 else:
#                     message = '请确认用户类型'
#
#
#             except Exception as e:
#                 print(e)
#                 request.session.flush()
#                 message = '无此用户'
#         return render(request, 'foreground/login.html', locals())
#     login_form = forms.loginForm()
#     return render(request, 'foreground/login.html',locals())

# def person_index(request):
#     return render(request, 'foreground/person_index.html')
# def com_index(request):
#     return render(request, 'foreground/com_index.html')
# def gov_index(request):
#     return render(request, 'foreground/gov_index.html')
# def govcom_index(request):
#     return render(request, 'foreground/govcom_index.html')
# def test(request):
#     return render(request, 'foreground/signin.html')
def fileSearch(request):
    role = request.session["user_type"]
    return render(request, 'foreground/ArticleSearch.html', {"role": role})
def eventSearch(request):
    role = request.session["user_type"]
    return render(request, 'foreground/eventSearch.html', {"role": role})
#
# def signin(request):
#     if request.method == 'POST':
#         userdata = request.POST
#         print(type(userdata))
#         if userdata.get('user-type') == '0':
#             personUser(userdata)
#             return redirect('/jump/')
#         elif userdata.get('user-type') == '1':
#             try:
#                 companyUser(request)
#                 return redirect('/jump/')
#             except:
#                 error = 'error'
#                 return render(request, 'foreground/signin.html', {'message': error})
#         elif userdata.get('user-type') == '2':
#             try:
#                 govUser(request)
#                 return redirect('/jump/')
#             except Exception as e:
#                 error = 'error'
#                 return render(request, 'foreground/signin.html', {'message': error})
#         elif userdata.get('user-type') == '3':
#             try:
#                 InstitutionUser(request)
#                 return  redirect('/jump/')
#             except Exception as e:
#                 error = 'error'
#                 return render(request, 'foreground/signin.html', {'message': error})
#         else:
#             pass
#
#
#     return render(request, 'foreground/signin.html')

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

def competitive_products(request):
    return render(request, 'foreground/competitive_products.html')

def events(request):
    head = request.GET
    messageDic = {"type": head["type"], "role": head["role"]}
    return render(request, 'foreground/events.html', messageDic)

def eventparticular(request):
    role = request.session["user_type"]
    return render(request, 'foreground/particular.html', {"role": role})

def fileParticular(request):
    role = request.session["user_type"]
    return render(request, 'foreground/file.html', {"role": role})

@csrf_exempt
def checkuser(request):
    username = request.POST.get('user')
    count = models.User.objects.filter(username=username).count()
    if count==0:
        msg = 1
    else:
        msg = 0
    return JsonResponse({'msg':msg})

# def test(request):
#
#     return render(request, 'foreground/com_index.html')
#
# def jump(request):
#     logdata = ['','', '/login/', '注册', '']
#     logger.debug(logdata)
#     return render(request, 'foreground/jump.html')
#
# def logout(request):
#     logdata = [request.session['user_id'],request.session['user_role'],'/login/','退出','']
#     logger.debug(logdata)
#     request.session.flush()
#     return redirect("/login/")

def getEventsData(request):
    userid = request.session['user_id']
    func = request.GET.get("func")
    data = []
    if func == "企业相关":
        user = models.CompanyUser.objects.get(userid=userid)
        interests = user.businessscope
        lis = interests.split(',')
        for li in lis:
            results = models.Event.objects.filter(keyword__contains=li)
            if len(results) != 0:
                for result in results:
                    objectid = result.pk
                    object = models.Object.objects.get(objectid=objectid)
                    name = object.name
                    starttime = result.eventbegintime
                    newsNum = models.Article.objects.filter(objectid=objectid).count()
                    heatIndex = if_is_None(models.IndicatorValue.objects.filter(objectid=objectid, indexname="热度"), "暂缺")
                    if heatIndex != "暂缺" and len(heatIndex) > 0:
                        heatIndex = heatIndex[0].indicatorvalue
                        if int(heatIndex) >= 40:
                            heatIndex = "⭐热点事件"
                        else:
                            heatIndex = "一般事件"
                    else:
                        heatIndex = "数据暂缺"
                    data.append({"name": name, "heatIndex": heatIndex, "newsNum": str(newsNum), "begintime": starttime, "objectid": objectid})
        print(data)
        return JsonResponse({"data": data})

    if func == "当地新闻":
        coordinate = models.User.objects.get(userid=userid).address
        province = coordinate.split("省")[0]
        if province != coordinate:
            city = coordinate.split("省")[1].split("市")[0]
        else:
            city = coordinate.split("市")[0]
        lis = [province, city]
        data = []
        for li in lis:
            results = models.Event.objects.filter(keyword__contains=li)
            if len(results) != 0:
                for result in results:
                    objectid = result.pk
                    object = models.Object.objects.get(objectid=objectid)
                    name = object.name
                    starttime = result.eventbegintime
                    newsNum = models.Article.objects.filter(objectid=objectid).count()
                    heatIndex = if_is_None(models.IndicatorValue.objects.filter(objectid=objectid, indexname="热度"), "暂缺")
                    if heatIndex != "暂缺" and len(heatIndex) > 0:
                        heatIndex = heatIndex[0].indicatorvalue
                        if int(heatIndex) >= 40:
                            heatIndex = "⭐热点事件"
                        else:
                            heatIndex = "一般事件"
                    else:
                        heatIndex = "数据暂缺"
                    data.append({"name": name, "heatIndex": heatIndex, "newsNum": str(newsNum), "begintime": starttime, "objectid": objectid})
        print(data)
        return JsonResponse({"data": data})

    if func == "敏感信息":
        data = []
        informs = models.IndicatorValue.objects.filter(indexname="敏感度")
        for inform in informs:
            if int(inform.indicatorvalue) >= 40 :
                objectid = inform.objectid.pk
                event = models.Event.objects.get(objectid=objectid)
                name = inform.objectid.name
                newsNum = models.Article.objects.filter(objectid=objectid).count()
                starttime = event.eventbegintime
                heatIndex = if_is_None(models.IndicatorValue.objects.filter(objectid=objectid, indexname="热度"), "暂缺")
                if heatIndex != "暂缺" and len(heatIndex) > 0:
                    heatIndex = heatIndex[0].indicatorvalue
                    if int(heatIndex) >= 40:
                        heatIndex = "⭐热点事件"
                    else:
                        heatIndex = "一般事件"
                else:
                    heatIndex = "数据暂缺"
                data.append({"name": name, "heatIndex": heatIndex, "newsNum": str(newsNum), "begintime": starttime, "objectid": objectid})
        return JsonResponse({"data": data})

    if func == "领域相关":
        user = models.CompanyUser.objects.get(userid=userid)
        interests = user.interest
        lis = interests.split(',')
        for li in lis:
            results = models.Event.objects.filter(keyword__contains=li)
            if len(results) != 0:
                for result in results:
                    objectid = result.pk
                    object = models.Object.objects.get(objectid=objectid)
                    name = object.name
                    starttime = result.eventbegintime
                    newsNum = models.Article.objects.filter(objectid=objectid).count()
                    heatIndex = if_is_None(models.IndicatorValue.objects.filter(objectid=objectid, indexname="热度"),
                                           "暂缺")
                    if heatIndex != "暂缺" and len(heatIndex) > 0:
                        heatIndex = heatIndex[0].indicatorvalue
                        if int(heatIndex) >= 40:
                            heatIndex = "⭐热点事件"
                        else:
                            heatIndex = "一般事件"
                    else:
                        heatIndex = "数据暂缺"
                    data.append({"name": name, "heatIndex": heatIndex, "newsNum": str(newsNum), "begintime": starttime,
                                 "objectid": objectid})
        print(data)
        return JsonResponse({"data": data})

def getArticles(request):
    objectid = request.GET.get("objectid")
    res = models.Object.objects.get(objectid=objectid)
    print(res.name)
    files = models.Article.objects.filter(objectid=objectid)[:5]
    dataList = []
    for file in files:
        fileTitle = file.title
        fileStar = if_is_None(file.likenumber, str(random.randint(0, 1000)))
        wroteTime = file.posttime
        id = file.articleid
        dataList.append({"fileTitle": fileTitle, "fileStar": fileStar, "wroteTime": wroteTime, "id": id})
    return JsonResponse({"data": dataList})
