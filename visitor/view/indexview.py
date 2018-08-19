from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.db.models import Q
from visitor import models
import datetime
def person_index(request):
    return render(request, 'foreground/person_index.html')
def com_index(request):
    userid = request.session["user_id"]
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

    user = models.CompanyUser.objects.get(userid=userid)
    interests = user.businessscope
    lis = interests.split(',')
    related = Q()
    for li in lis:
        related.add(Q(keyword__contains=li), "OR")
    relatedEvents = events.filter(related)
    relatedEventsNum = relatedEvents.count()

    heatEvents = models.IndicatorValue.objects.filter(indexname="热度", indicatorvalue__gt=80)
    heatEventsNum = 0
    for heatEvent in heatEvents:
        itemID = heatEvent.objectid.pk
        try:
            relatedEvents.get(objectid=itemID)
            heatEventsNum += 1
        except:
            pass
    heatIndexb =int(200*heatEventsNum/relatedEventsNum)
    heatIndext = str(200-heatIndexb)+"px"
    heatIndexb = str(heatIndexb)+"px"

    sensitiveEvents = models.IndicatorValue.objects.filter(indexname="敏感度", indicatorvalue__gt=80)
    sensitiveEventsNum = 0
    for sensitiveEvent in sensitiveEvents:
        itemID = sensitiveEvent.objectid.pk
        try:
            relatedEvents.get(objectid=itemID)
            sensitiveEventsNum += 1
        except:
            pass
    sensitiveIndex = int(200*sensitiveEventsNum/relatedEventsNum)
    sensitiveIndexb = str(sensitiveIndex)+"px"
    sensitiveIndext = str(200-sensitiveIndex)+"px"

    indexDic.update({"heatEventsNum": heatEventsNum, "sensitiveEventsNum": sensitiveEventsNum, "relatedEventsNum": relatedEventsNum,
                     "heatIndext": heatIndext, "heatIndexb": heatIndexb, "sensitiveIndext": sensitiveIndext, "sensitiveIndexb": sensitiveIndexb})



    return render(request, 'foreground/com_index.html', indexDic)
def gov_index(request):
    return render(request, 'foreground/gov_index.html')
def govcom_index(request):
    return render(request, 'foreground/govcom_index.html')

def index_emotionTrend(request):
    userid = request.session["user_id"]

    now = datetime.datetime.now()
    graphStartTime = now-datetime.timedelta(days=730)

    return JsonResponse({"data": []})