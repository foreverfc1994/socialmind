from visitor.models import Area,Province,City
from django import template

register = template.Library()

@register.simple_tag
def get_province():
    province = Province.objects.all()
    return province

@register.simple_tag
def get_city(province):
    print(province)
    pid = Province.objects.get(name=province).code[:2]
    city = City.objects.filter(code__startswith=pid)
    return city
