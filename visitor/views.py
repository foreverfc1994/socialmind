from django.shortcuts import render, redirect
from visitor.models import Province, City, Area
from visitor import models
from django.db.models import Q
from django.http import JsonResponse
from visitor import forms
from django.views.decorators.csrf import csrf_exempt
from visitor.scripts.signin import *
import datetime
import time
# Create your views here.
# from visitor.scripts.SysLog import Logger
import random
from manager.mysqlNullWash import if_is_None, webType_to_strType, changeWebsite
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
    objectid = if_is_None(request.GET.get("objectid"), "")
    if objectid != "":
        name = if_is_None(models.Object.objects.get(objectid=objectid).name, "")
    else:
        name = ""
    operats = []

    return render(request, 'foreground/ArticleSearch.html', {"role": role, "objectid": objectid, "name": name})

def getAllFile(request):
    page = int(request.GET.get("page"))
    objectid = request.GET.get("objectid")
    keyword = request.GET.get("keyword")
    fileType = request.GET.get("fileType")
    sql = Q()
    sql.connector = 'OR'
    if objectid != "":
        sql.add(Q(objectid=objectid), 'AND')
    if keyword != "":
        sql.add(Q(content__contains=keyword)|Q(title__contains=keyword), 'AND')
    if fileType != "":
        sql.add(Q(keywords__contains=fileType), 'AND')
    articles = models.Article.objects.filter(sql).values("articleid", "authorid", "title", "content", "posttime", "websiteid")[page*20: (page+1)*20]
    data = []
    for article in articles:
        articleid = article['articleid']
        authorid = article['authorid']
        authorname = "暂缺"
        title = article['title']
        content = article['content']
        if len(content) > 20:
            content = content[0:20]+"..."
        posttime = if_is_None(article['posttime'][0:10], "暂缺")
        websiteid = article['websiteid']
        if authorid != None:
            try:
                authorname = if_is_None(models.Author.objects.get(authorid=authorid).name)
            except:
                pass
        try:
            webObj = models.Website.objects.get(websiteid=websiteid)
            webname = webObj.websitename
            webtype = webType_to_strType(webObj.websitetypeid)
        except:
            webname = "暂缺"
            webtype = "暂缺"
        data.append({"articleid": articleid, "authorname": authorname, "title": title, "content": content, "posttime": posttime,
                     "webname": webname, "webtype": webtype})
    return JsonResponse({"data": data})



def eventSearch(request):
    role = request.session["user_type"]
    return render(request, 'foreground/eventSearch.html', {"role": role})

def getEventList(request):
    page = int(request.GET.get("page"))
    keyword = request.GET.get("keyword")
    if keyword == "undefined" or keyword == None:
        keyword = ""
    items = models.Object.objects.filter(objecttype="事件").filter(name__contains=keyword).values \
                  ("objectid", "name", "introduction", "collectnumber", "likenumber", "commentnumber")[page*20: (page+1)*20]
    data = []
    for item in items:
        objectid = item['objectid']
        title = item['name']
        introduction = if_is_None(item['introduction'], "简介暂缺")
        collectNum = if_is_None(item['collectnumber'], "0")
        likeNum = if_is_None(item['likenumber'])
        commentNum = if_is_None(item['commentnumber'])
        try:
            starttime = if_is_None(models.Event.objects.get(objectid=objectid).eventbeaintime, "暂缺")
        except:
            starttime = "暂缺"
        try:
            heatIndex = models.IndicatorValue.objects.get(indexname="热度", objectid=objectid).indicatorvalue
        except:
            heatIndex = "暂缺"
        data.append({"objectid": objectid, "title": title, "introduction": introduction, "collectNum": collectNum,
                     "likeNum": likeNum, "commentNum": commentNum, "heatIndex": heatIndex, "starttime": starttime})
    return JsonResponse({"data": data})

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
    userid = request.session["user_id"]
    objectid = request.GET.get("objectid")
    event = models.Object.objects.get(objectid=objectid)

    judge = models.UserOpera.objects.filter(userid=userid, type="浏览", operatype="object", objectid=objectid)
    judgeCount = judge.count()
    if judgeCount == 0:
        historyDic = {"operaid": uuid.uuid4(), "userid": models.User.objects.get(userid=userid), "type": "浏览", "operatype": "object",
                      "objectid": event,
                      "operatime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        models.UserOpera.objects.create(**historyDic).save()
    else:
        judge.update(operatime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

    title = event.name
    introduction = if_is_None(models.Event.objects.get(objectid=objectid).introduction, "")
    trueNum = if_is_None(event.truenumber, "0")
    flaseNum = if_is_None(event.falsenumber, "0")
    likeNum = if_is_None(event.likenumber, "0")
    collectNum = if_is_None(event.collectnumber, "0")
    begintime = if_is_None(models.Event.objects.get(objectid=objectid).eventbegintime, "暂缺")
    endtime = if_is_None(models.Event.objects.get(objectid=objectid).eventendtime, "暂缺")
    data = {"role": role, "objectid": objectid, "title": title, "introduction": introduction, "trueNum": trueNum, "falseNum": flaseNum,
            "likeNum": likeNum, "collectNum": collectNum, "begintime": begintime, "endtime": endtime}
    return render(request, 'foreground/particular.html', data)

def getEventComments(request):
    objectid = request.GET.get("objectid")
    data = []
    comments = models.Message.objects.filter(objectid=objectid, checked="1")
    if(len(comments)>0):
        for comment in comments:
            content = comment.messagecontent
            messageTime = if_is_None(comment.messagetime)
            userid = comment.userid
            username = if_is_None(models.User.objects.get(userid=userid).username, "未知用户")
            data.append({"content": content, "messageTime": messageTime, "username": username})
    return JsonResponse({"data": data})

def getEventOpera(request):
    userid = request.session["user_id"]
    objectid = request.GET.get("objectid")
    operaData = {}
    collect = models.UserOpera.objects.filter(type="收藏", objectid=objectid)
    collectedNum = collect.count()
    collected = collect.filter(userid=userid).count()
    if collected == 0:
        operaData.update({"collected": "false", "collectNum": collectedNum})
    else:
        operaData.update({"collected": "true", "collectNum": collectedNum})
    like = models.UserOpera.objects.filter(type="点赞", objectid=objectid)
    likeNum = like.count()
    liked = like.filter(userid=userid).count()
    if liked == 0:
        operaData.update({"liked": "false", "likeNum": likeNum})
    else:
        operaData.update({"liked": "true", "likeNum": likeNum})
    isTrue = models.UserOpera.objects.filter(type="判真", objectid=objectid)
    isFalse = models.UserOpera.objects.filter(type="判假", objectid=objectid)
    isTrueNum = isTrue.count()
    isFalseNum = isFalse.count()
    if isTrue.filter(userid=userid).count() != 0:
        operaData.update({"isTrue": "true", "isTrueNum": isTrueNum})
        operaData.update({"isFalse": "false", "isFalseNum": isFalseNum})
    elif isFalse.filter(userid=userid).count() != 0:
        operaData.update({"isTrue": "false", "isTrueNum": isTrueNum})
        operaData.update({"isFalse": "true", "isFalseNum": isFalseNum})
    else:
        operaData.update({"isTrue": "false", "isTrueNum": isTrueNum})
        operaData.update({"isFalse": "false", "isFalseNum": isFalseNum})
    print(operaData)
    return JsonResponse({"data": operaData})


def getCorrelationFiles(request):
    objectid = request.GET.get("objectid")
    page = int(request.GET.get("page"))
    files = models.Article.objects.filter(objectid=objectid)[page*10: (page+1)*10]
    data = []
    for file in files:
        title = file.title
        posttime = if_is_None(file.posttime, "暂缺")
        content = file.content
        if len(content) >= 140:
            content = content[:140]+"..."
        articleid = file.articleid
        likeNum = if_is_None(file.likenumber, "0")
        commentNum = if_is_None(file.commentnumber, "0")
        collectNum = if_is_None(file.collectnumber, "0")
        webSource = if_is_None(file.websiteid.websitename, "暂缺")
        data.append({"articleid": articleid, "title": title, "posttime": posttime, "content": content, "likeNum": likeNum,
                     "commentNum": commentNum, "collectNum": collectNum, "webSource": webSource})
    return JsonResponse({"data": data})



def fileParticular(request):
    role = request.session["user_type"]
    userid = request.session["user_id"]
    articleid = request.GET.get("articleid")
    article = models.Article.objects.get(articleid=articleid)

    judge = models.UserOpera.objects.filter(userid=userid, type="浏览", operatype="article", articleid=article)
    judgeCount = judge.count()
    if judgeCount == 0:
        historyDic = {"operaid": uuid.uuid4(), "userid": models.User.objects.get(userid=userid), "type": "浏览", "operatype": "article",
                      "articleid": article,
                      "operatime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
        models.UserOpera.objects.create(**historyDic).save()
    else:
        judge.update(operatime=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


    title = article.title
    posttime = if_is_None(article.posttime, "暂缺")
    introduction = if_is_None(article.keywords, "暂无")
    content = article.content
    commentNum = if_is_None(article.commentnumber, "0")
    collectNum = if_is_None(article.collectnumber, "0")
    likeNum = if_is_None(article.likenumber, "0")
    webSource = if_is_None(article.websiteid.websitename, "暂缺")
    try:
        objectid = article.objectid.pk
    except:
        objectid = ""
    data = {"role": role, "articleid": articleid, "title": title, "posttime": posttime,
            "introduction": introduction, "content": content, "commentNum": commentNum,
            "collectNum": collectNum, "likeNum": likeNum, "webSource": webSource, "objectid": objectid}
    return render(request, 'foreground/file.html', data)

def getOperaData(request):
    userid = request.session["user_id"]
    articleid = request.GET.get("articleid")
    operaData = {}
    collect = models.UserOpera.objects.filter(type="收藏", articleid=articleid)
    collectedNum = collect.count()
    collected = collect.filter(userid=userid).count()
    if collected == 0:
        operaData.update({"collected": "false", "collectNum": collectedNum})
    else:
        operaData.update({"collected": "true", "collectNum": collectedNum})
    like = models.UserOpera.objects.filter(type="点赞", articleid=articleid)
    likeNum = like.count()
    liked = like.filter(userid=userid).count()
    if liked == 0:
        operaData.update({"liked": "false", "likeNum": likeNum})
    else:
        operaData.update({"liked": "true", "likeNum": likeNum})
    isTrue = models.UserOpera.objects.filter(type="判真", articleid=articleid)
    isFalse = models.UserOpera.objects.filter(type="判假", articleid=articleid)
    isTrueNum = isTrue.count()
    isFalseNum = isFalse.count()
    if isTrue.filter(userid=userid).count() != 0:
        operaData.update({"isTrue": "true", "isTrueNum": isTrueNum})
        operaData.update({"isFalse": "false", "isFalseNum": isFalseNum})
    elif isFalse.filter(userid=userid).count() != 0:
        operaData.update({"isTrue": "false", "isTrueNum": isTrueNum})
        operaData.update({"isFalse": "true", "isFalseNum": isFalseNum})
    else:
        operaData.update({"isTrue": "false", "isTrueNum": isTrueNum})
        operaData.update({"isFalse": "false", "isFalseNum": isFalseNum})
    print(operaData)
    return JsonResponse({"data": operaData})

def getCorrelatFiles(request):
    objectid = request.GET.get("objectid")
    page = int(request.GET.get("page"))
    files = models.Article.objects.filter(objectid=objectid)[page * 10: (page + 1) * 10]
    data = []
    for file in files:
        title = file.title
        posttime = if_is_None(file.posttime, "暂缺")
        content = file.content
        if len(content) >= 140:
            content = content[:140] + "..."
        articleid = file.articleid
        likeNum = if_is_None(file.likenumber, "0")
        commentNum = if_is_None(file.commentnumber, "0")
        collectNum = if_is_None(file.collectnumber, "0")
        webSource = if_is_None(file.websiteid.websitename, "暂缺")
        data.append(
            {"articleid": articleid, "title": title, "posttime": posttime, "content": content, "likeNum": likeNum,
             "commentNum": commentNum, "collectNum": collectNum, "webSource": webSource})
    return JsonResponse({"data": data})

def getArticleParticular(request):
    articleid = request.GET.get('articleid')
    data = []
    results = models.Comment.objects.filter(articleid=articleid, checked="1")
    for result in results:
        name = if_is_None(result.userid.username, "未知用户")
        content_row = result.commentcontent
        if result.fathercommentid == None:
            content = content_row
        else:
            content = ""
        commentTime = if_is_None(result.commenttime, "未知")
        data.append({"username": name, "content": content, "commentTime": commentTime})
    #print(data)
    return JsonResponse({"data": data})


def addOperation(request):
    try:
        userid = request.session['user_id']
        operatype = request.GET.get("type")
        num = int(request.GET.get("num"))
        operaList = ["收藏", "点赞", "判真", "判假"]
        type = operaList[num]
        # 新建条目
        createDic = {"operaid": str(uuid.uuid4()),
                     "userid": models.User.objects.get(userid=userid),
                     "operatype": operatype,
                     "type": type,
                     "operatime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                     }
        # 判真/判假时若出现已经判断的情况则覆盖
        sql = Q(userid=userid)
        sql.add(Q(operatype=operatype), 'AND')
        sql.add(Q(type="判真")|Q(type="判假"), 'AND')
        if operatype == "article":
            articleid = request.GET.get("articleid")
            createDic.update({"articleid": models.Article.objects.get(articleid=articleid)})
            sql.add(Q(articleid=articleid), 'AND')
        elif operatype == "object":
            objectid = request.GET.get("objectid")
            createDic.update({"objectid": models.Object.objects.get(objectid=objectid)})
            sql.add(Q(objectid=objectid), 'AND')
        if num <= 1:
            models.UserOpera.objects.create(**createDic).save()
        else:
            try:
                find = models.UserOpera.objects.get(sql)
                find.type = type
                find.operatime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                find.save()
            except:
                models.UserOpera.objects.create(**createDic).save()
        return JsonResponse({"data": "true"})
    except:
        return JsonResponse({"data": "false"})

def subOperation(request):
    userid = request.session['user_id']
    operatype = request.GET.get("type")
    num = int(request.GET.get("num"))
    operaList = ["收藏", "点赞", "判真", "判假"]
    type = operaList[num]
    sql = Q(operatype=operatype)
    sql.add(Q(userid=userid), 'AND')
    sql.add(Q(type=type), 'AND')
    if operatype == "article":
        articleid = request.GET.get('articleid')
        sql.add(Q(articleid=articleid), 'AND')
    elif operatype == "object":
        objectid = request.GET.get('objectid')
        sql.add(Q(objectid=objectid), 'AND')
    models.UserOpera.objects.get(sql).delete()

    return JsonResponse({"data": "succeed"})

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
        # print(data)
        return JsonResponse({"data": data})

    elif func == "当地新闻":
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
        # print(data)
        return JsonResponse({"data": data})

    elif func == "敏感信息":
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

    elif func == "领域相关":
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
        # print(data)
        return JsonResponse({"data": data})

    elif func == "行业信息":
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
        # print(data)
        return JsonResponse({"data": data})

    else:
        return JsonResponse({"data": [{"name": "name", "heatIndex": "热度", "newsNum": "信息数", "begintime": "开始时间", "objectid": "对象id"}]})

def getArticles(request):
    objectid = request.GET.get("objectid")
    res = models.Object.objects.get(objectid=objectid)
    files = models.Article.objects.filter(objectid=objectid)[:5]
    dataList = []
    for file in files:
        fileTitle = file.title
        fileStar = if_is_None(file.likenumber, str(random.randint(0, 1000)))
        wroteTime = file.posttime
        id = file.articleid
        dataList.append({"fileTitle": fileTitle, "fileStar": fileStar, "wroteTime": wroteTime, "id": id})
    return JsonResponse({"data": dataList})


def addComments(request):
    userid = request.session["user_id"]
    type = request.GET.get("type")
    comment = request.GET.get("comment")
    id = request.GET.get("id")
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if type == "event":
        try:
            object = models.Object.objects.get(objectid=id)
            res = models.Message.objects.create(messageid=uuid.uuid4(), messagecontent=comment, messagetime=time,
                                                  objectid=object, checked="0", userid=userid)
            res.save()
            return JsonResponse({"data": "succeed"})
        except:
            return JsonResponse({"data": "failed"})