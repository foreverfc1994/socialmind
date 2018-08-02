from django.shortcuts import render,redirect
def person_index(request):
    return render(request, 'foreground/person_index.html')
def com_index(request):
    return render(request, 'foreground/com_index.html')
def gov_index(request):
    return render(request, 'foreground/gov_index.html')
def govcom_index(request):
    return render(request, 'foreground/govcom_index.html')