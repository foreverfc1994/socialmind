from django.shortcuts import render,redirect
from visitor.models import User,Province,City,Area
from visitor import models
import time
from django.http import JsonResponse, HttpResponse
import json
from manager.mysqlNullWash import if_is_None, webType_to_strType, changeWebsite
from django.views.decorators.csrf import csrf_exempt
from visitor.scripts.signin import *
from manager.scripts.sysscript import *
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
        try:
            authorID = if_is_None(authorid.authorid, "0")
        except:
            authorID = ""
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

def getAuthors(request):
    dataList = []
    results = models.Author.objects.values("authorid", "name", "fansnumber", "websiteid")
    files = models.Article.objects.values("authorid")
    for result in results:
        try:
            authorID = result['authorid']
            name = if_is_None(result['name'], "暂缺")
            fansNumber = str(if_is_None(result['fansnumber'], 0))
            web = "暂缺"
            filesNumber = files.filter(authorid=authorID).count()
            if result['websiteid'] != None:
                web, webtype = changeWebsite(if_is_None(int(result['websiteid'])-1, 2))
            dic = {"authorId": authorID, "name": name, "filesNumber": filesNumber, "fansNumber": fansNumber, "web": web}
            dataList.append(dic)
        except:
            print(authorID+" was wrong.")
    data = {"data": dataList}
    return JsonResponse(data)

def getArticleList(request):
    dataList = []
    results = models.Article.objects.values("articleid", "authorid", "title", "scannumber", "websiteid")
    authorInform = models.Author.objects.values("authorid", "name")
    for result in results:
        articleId = result['articleid']
        authorId = if_is_None(result['authorid'])
        authorName = "暂缺"
        title = if_is_None(result['title'])
        readed = if_is_None(result['scannumber'], 0)
        if(readed >= 100):
            heat = "超热"
        else:
            heat = "不热"
        webName, webType = changeWebsite(if_is_None(int(result['websiteid'])-1, 2))
        if(authorId != ""):
            authorName = authorInform.get(authorid=authorId)['name']
        dataList.append({"id": articleId, "title": title, "web": webName, "author": authorName, "type": webType, "readed": str(readed), "heat": heat})
    res = {"data": dataList}
    return JsonResponse(res)


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
def Author(request):
    return render(request, 'background/Author.html')
def ArticlesAndComments(request):
    return render(request, 'background/ArticlesAndComments.html')
def articleslsit(request):
    return render(request,'background/Articleslist.html')
@csrf_exempt
def objectarticlelist(request):
    url = request.POST.get('url')
    id = url.split('/')[-2]
    dataList = []
    object = models.Object.objects.get(objectid=id)
    results = models.Article.objects.filter(objectid=object)
    authorInform = models.Author.objects.values("authorid", "name")
    for result in results:
        articleId = result.articleid
        authorId = if_is_None(result.authorid.authorid)
        authorName = "暂缺"
        title = if_is_None(result.title)
        readed = if_is_None(result.scannumber, 0)
        if (readed >= 100):
            heat = "超热"
        else:
            heat = "不热"
        webName, webType = changeWebsite(if_is_None(int(result.websiteid.websiteid) - 1, 2))
        if (authorId != ""):
            authorName = authorInform.get(authorid=authorId)['name']
        dataList.append({"id": articleId, "title": title, "web": webName, "author": authorName, "type": webType,
                         "readed": str(readed), "heat": heat})
    res = {"data": dataList}
    # print(res)
    return JsonResponse(res)
def objectarticle(request,id):
    # try:
    #     object = models.Object.objects.get(objectid=id)
    #     articles = models.Article.objects.filter(objectid=object)
    #     for a in articles:
    #         dic = {}
    #         dic['id'] = a.articleid
    #         dic['title']= a.title
    #         dic['web'] = a.websiteid.websitename
    #         try:
    #            dic['author'] = a.authorid.name
    #         except:
    #             dic['author'] = '未知'
    #         webName, webType = changeWebsite(if_is_None(int(a['websiteid']) - 1, 2))
    #         dic['type'] =  webType
    #         dic['readed']
    #         dic['heat']
    #
    #     print(len(articles))
    # except:
    #     pass

    return render(request,'background/ObjectArticel.html')
    pass

def deleteArticle(request):
    id = request.GET.get("id")
    try:
        models.Article.objects.filter(articleid=id).delete()
        return HttpResponse(json.dumps({"data": "succeed"}))
    except:
        return HttpResponse(json.dumps({"data": "failed"}))

def deleteAuthor(request):
    id = request.GET.get("id")
    try:
        models.Author.objects.filter(authorid=id).delete()
        return HttpResponse(json.dumps({"data": "succeed"}))
    except:
        return HttpResponse(json.dumps({"data": "failed"}))