from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Q
from visitor import models
import datetime
def person_index(request):
    return render(request, 'foreground/person_index.html')
def com_index(request):
    indexDic = {}

    now = datetime.datetime.now()
    today = now.strftime("%Y-%m-%d %H:%M:%S")
    indexDic.update({"today": today})

    newTime = (now-datetime.timedelta(days=30))
    Q_newEvent = Q(eventbegintime__gt=newTime)
    events = models.Event.objects.filter()
    eventsNum = events.count()
    newEventNum = events.filter(Q_newEvent).count()
    indexDic.update({"eventsNum": eventsNum, "newEventsNum": newEventNum})

    sensitive = Q(indexname="敏感度")
    sensitiveInform = models.IndicatorValue.objects.filter(sensitive)
    sensitiveInformNum = sensitiveInform.count()
    currentSensitive = Q(starttime__gt=newTime)
    newSensitive = sensitiveInform.filter(currentSensitive).count()
    indexDic.update({"sensitiveInformNum": sensitiveInformNum, "newSensitive": newSensitive})

    indexDic.update({"emotionTrend": "正向"})


    return render(request, 'foreground/com_index.html', indexDic)
def gov_index(request):
    return render(request, 'foreground/gov_index.html')
def govcom_index(request):
    return render(request, 'foreground/govcom_index.html')