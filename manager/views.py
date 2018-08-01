from django.shortcuts import render,redirect
from visitor.models import User,Province,City,Area
from visitor import models
from django.http import JsonResponse, HttpResponse
import json
from manager.mysqlNullWash import if_is_None, webType_to_strType
from django.views.decorators.csrf import csrf_exempt
from visitor.scripts.signin import *
# Create your views here.
# def login(request):
#     print(request.method)
#     if request.method == 'POST':
#         print(request.POST)
#         message = ''
#         username = request.POST.get('username',None)
#         password = request.POST.get('password',None)
#         user_type = request.POST.get('user-type')
#         return redirect('/index/')
#     return render(request, 'foreground/index.html')

def index(request):
    return render(request, 'background/index.html')
def login(request):
    return render(request, 'background/login.html')
def SpiderList(request):
    return render(request, 'background/SpiderList.html')
def SpiderMonitor(request):
    return render(request, 'background/SpiderMonitor.html')
def SpiderConfigure(request):
    return render(request, 'background/SpiderConfigure.html')
def Author(request):
    return render(request, 'background/Author.html')
def ArticlesOfAuthor(request):#作者详情
    authorId = request.GET.get("id")
    result = models.Author.objects.get(authorid=authorId)
    authorID = result.authorid
    name = if_is_None(result.name)
    sex = if_is_None(result.sex, "未知")
    age = str(if_is_None(result.age, "暂缺"))
    fansNumber = str(if_is_None(result.fansnumber, 0))
    address = if_is_None(result.address, "暂缺")
    filesNumber = models.Article.objects.filter(authorid=authorID).count()
    web = "暂缺"
    if result.websiteid != None:
        web = if_is_None(result.websiteid.websitename)
    introduction = if_is_None(result.introduction, "暂缺")
    focusNum = str(if_is_None(result.focusnumber, 0))
    data = {"authorId": authorID, "authorName": name, "filesNumber": filesNumber, "fansNumber": fansNumber, "web": web,
           "sex": sex, "age": age, "address": address, "introduction": introduction, "focusNum": focusNum}
    return render(request, 'background/ArticlesOfAuthor.html', data)
def ArticlesAndComments(request):
    return render(request, 'background/ArticlesAndComments.html')
def DataCleanStatistics(request):
    return render(request, 'background/DataCleanStatistics.html')
def DataCleanStrategies(request):
    return render(request, 'background/DataCleanStrategies.html')
def DataCleanLog(request):
    return render(request, 'background/DataCleanLog.html')
def washData(request):
    return render(request, 'background/washData.html')
def topics(request):
    return render(request, 'background/topics.html')
def AddEventObject(request):
    return render(request, 'background/AddEventObject.html')
def CreateEventObject(request):
    return render(request, 'background/CreateEventObject.html')
def ShowEventObject(request):
    #return render(request, 'background/ShowEventObject.html')
    return render(request, 'background/socialobject.html')
def semanticsTools(request):
    return render(request, 'background/semanticsTools.html')
def semanticsToolkits(request):
    return render(request, 'background/semanticsToolkits.html')
def ShowToolkits(request):
    return render(request, 'background/ShowToolkits.html')
def usrCommentsSelect(request):
    return render(request, 'background/usrCommentsSelect.html')
def usrCommentsCheck(request):
    return render(request, 'background/usrCommentsCheck.html')
def usrCommentsDelete(request):
    return render(request, 'background/usrCommentsDelete.html')
def AssignAuthorities(request):
    return render(request, 'background/AssignAuthorities.html')
def usersVerify(request):
    return render(request, 'background/usersVerify.html')
def usrManagement(request):
    return render(request, 'background/usrManagement.html')
def operateDiary(request):
    return render(request, 'background/operateDiary.html')
def DouBanArticleStyle(request):
    return render(request, 'background/DouBanArticleStyle.html')
def ArticlePaticular(request):              #文章详情
    articleID = request.GET.get("id")
    allInformation = if_is_None(models.Article.objects.get(articleid=articleID), "0")
    resultDic = {}
    if allInformation != "0":
        title = allInformation.title
        authorid = if_is_None(allInformation.authorid, "0")
        author = "暂缺"
        if authorid != "0":
            author = if_is_None(authorid.name, "暂缺")
        authorID = if_is_None(authorid.authorid, "0")
        webName = if_is_None(allInformation.websiteid.websitename, "暂缺")
        webUrl = if_is_None(allInformation.websiteid.websiteurl, "暂缺")
        postTime = if_is_None(allInformation.posttime, "未知")
        content = if_is_None(allInformation.content, "暂缺")
        content = content.replace("\ue5f1\u3000", "\n")
        likeNum = str(if_is_None(allInformation.likenumber, "0"))
        scanNum = str(if_is_None(allInformation.scannumber, "0"))
        resultDic = {"title": title, "author": author, "webName": webName, "webUrl": webUrl, "postTime": postTime, "content": content,
                     "likeNum": likeNum, "scanNum": scanNum, "articleID": articleID, "authorID": authorID}
        print(resultDic)
    return render(request, 'background/ArticlePaticular.html', resultDic)

def ArticlePaticularComments(request):
    articleID = request.GET.get("id")
    comments = if_is_None(models.ArticleComment.objects.filter(articleid=articleID))
    resultList = []
    for comment in comments:
        if comment.fathercommentid == None:
            commentID = comment.article_commentid
            commenterID = comment.authorid
            commenterName = "暂缺"
            if commenterID != None:
                commenterName = commenterID.name
            commentTime = if_is_None(comment.commenttime, "暂缺")
            content = comment.content
            content = content.replace("\ue5f1", "")
            resultList.append({"commentID": commentID, "commenterID": commenterID, "commenterName": commenterName, "commentTime": commentTime,
                               "contentt": content})
    result = {"data": resultList}
    return HttpResponse(json.dumps(result))

def usrManagement1(request,a):

    if a == 0:
        return render(request, 'background/usrManagement.html', {'type0': 1})
    elif a == 1:
        return render(request, 'background/usrManagement.html', {'type1': 1})
    elif a == 2:
        return render(request, 'background/usrManagement.html', {'type2': 1})
    elif a == 3:
        return render(request, 'background/usrManagement.html', {'type3': 1})
    else:
        return render(request, 'background/usrManagement.html')

def test(request):
    return render(request,'background/usrManagement1.html')
def test(request):
    return render(request,'1.html')
def yuandatashow(request):
    return render(request, 'background/yuandatashow.html')
def operate(request,a):
    return render(request, 'background/operateDiary.html')
def articleslsit(request):
    return render(request,'background/Articleslist.html')
def objectshow(request):
    return  render(request,'background/socialobject.html')
def eventshow(request):
    return render(request,'background/Eventlist.html')
def jianbao(request):
    return render(request,'background/jianbao.html')
def qiantaimotaikuang(request):
    # userid = request.session["user_id"]
    # role = request.session["user_type"]
    # username = request.session["user_name"]
    # currentUser = models.User.objects.get(userid=userid)
    # email = currentUser.email
    # personalized_data = models.CompanyUser.objects.get(userid=userid)
    # bossname = personalized_data.bossname
    # companyname = personalized_data.companyname
    # businessLicenceId = personalized_data.businesslicenceid
    # bussinessLicencePic = str(personalized_data.businesslicenceurl)
    return render(request, 'foreground/personalInformation.html',
                  {"userid": '123', "username": 123, "role": '个人用户', "email": '461834084@qq.com',
                   "bossname": '123', "companyname": '123',
                   "businessLicenceId": '123', "bussinessLicencePic":
                       '123'})
    # return render(request,'foreground/personalInformation.html')


def getAuthors(request):
    dataList = []
    results = models.Author.objects.filter()
    for result in results:
        try:
            authorID = result.authorid
            name = if_is_None(result.name)
            fansNumber = str(result.fansnumber)
            web = "暂缺"
            filesNumber = models.Article.objects.filter(authorid=authorID).count()
            if result.websiteid != None:
                web = if_is_None(result.websiteid.websitename)
            dic = {"authorId": authorID, "name": name, "filesNumber": filesNumber, "fansNumber": fansNumber, "web": web}
            dataList.append(dic)
        except:
            print(authorID+" was wrong")
    data = {"data": dataList}
    return HttpResponse(json.dumps(data))

def getArticleList(request):
    dataList = []
    results = models.Article.objects.filter()
    for result in results:
        articleId = result.articleid
        authorId = if_is_None(result.authorid)
        authorName = "暂缺"
        title = if_is_None(result.title)
        readed = if_is_None(result.scannumber, 0)#数据类型为int
        if(readed >= 100):
            heat = "超热"
        else:
            heat = "不热"
        webName = if_is_None(result.websiteid.websitename)
        webType = webType_to_strType(if_is_None(result.websiteid.websitetypeid, "0"))
        if(authorId != ""):
            authorName = authorId.name
        dataList.append({"id": articleId, "title": title, "web": webName, "author": authorName, "type": webType, "readed": str(readed), "heat": heat})
    res = {"data": dataList}
    return HttpResponse(json.dumps(res))

def getAuthor_ArticleList(request):
    authorID = request.GET.get("id")
    name = models.Author.objects.get(authorid=authorID).name
    results = models.Article.objects.filter(authorid=authorID)
    dataList = []
    for result in results:
        articleID = result.articleid
        posttime = if_is_None(result.posttime, "未知")
        title = result.title
        content = result.content
        if(len(content) >= 140):
            content = content[:140]+"..."
        content = content.replace("\u3000", "")
        scannumber = str(if_is_None(result.scannumber, 0))
        commentnumber = str(if_is_None(result.commentnumber, 0))
        collectnumber = str(if_is_None(result.collectnumber, 0))
        dataList.append({"articleID": articleID, "name": name, "posttime": posttime, "title": title, "content": content,
                         "scanNum": scannumber, "commentNum": commentnumber, "collectNum": collectnumber})
        print(dataList)
    data = {"data": dataList}
    return HttpResponse(json.dumps(data))