from __future__ import absolute_import
from __future__ import unicode_literals
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socialmind.settings")  # NoQA
import django
django.setup()  # NoQA
from visitor.models import User,Province,City,Area
provinces=Province.objects.all()
cities = City.objects.all()
areas = Area.objects.all()
citydic={}
for city in cities:
    citycode = city.code[:4]
    arealist=[]
    for area in areas:
        if area.code[:4]==citycode:
           arealist.append(area.name)
    citydic[city.name]=arealist
prodic={}
for province in provinces:
    procode = province.code[:2]
    citylist = {}
    for city in cities:
        if city.code[:2] == procode:
            citylist[city.name]= citydic[city.name]
    prodic[province.name]=citylist


