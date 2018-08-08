from django.shortcuts import render,redirect
from visitor import models
from django.http import JsonResponse
from manager.mysqlNullWash import countAge, if_is_None

def checkComments(request):
    unchecked = models.Message.objects.filter(checked="0")
    data = []
    for item in unchecked:
        try:
            messageid = item.messageid
            content = if_is_None(item.messagecontent, "数据丢失")
            time = if_is_None(item.messagetime, "数据丢失")
            objectid = if_is_None(item.objectid, "暂无")
            if objectid.objecttype == "事件":
                if objectid != "暂无":
                    objectname = objectid.name
                    objectid = objectid.objectid
                else:
                    objectname = "暂无"
                data.append({"messageid": messageid, "content": content, "time": time, "objectname": objectname, "objectid": objectid})
            else:
                pass
        except:
            print("messageid: "+messageid+" was wrong!")
    return JsonResponse({"data": data})


def manageComments(request):
    unchecked = models.Message.objects.filter(checked="1")
    data = []
    for item in unchecked:
        try:
            messageid = item.messageid
            content = if_is_None(item.messagecontent, "数据丢失")
            time = if_is_None(item.messagetime, "数据丢失")
            objectid = if_is_None(item.objectid, "暂无")
            if objectid.objecttype == "事件":
                if objectid != "暂无":
                    objectname = objectid.name
                    objectid = objectid.objectid
                else:
                    objectname = "暂无"
                data.append({"messageid": messageid, "content": content, "time": time, "objectname": objectname,
                             "objectid": objectid})
            else:
                pass
        except:
            print("messageid: " + messageid + " was wrong!")
    return JsonResponse({"data": data})


def commentPass(request):
    messageid = request.GET.get("messageid")
    try:
        item = models.Message.objects.get(messageid=messageid)
        item.checked = "1"
        item.save()
        return JsonResponse({"data": "true"})
    except:
        return JsonResponse({"data": "false"})

def noPass(request):
    messageid = request.GET.get("messageid")
    try:
        item = models.Message.objects.get(messageid=messageid)
        item.delete()
        item.save()
        return JsonResponse({"data": "true"})
    except:
        return JsonResponse({"data": "false"})

def deleteComment(request):
    messageid = request.GET.get("messageid")
    try:
        models.Message.objects.get(messageid=messageid).delete()
        print("~")
        return JsonResponse({"data": "true"})
    except:
        return JsonResponse({"data": "false"})