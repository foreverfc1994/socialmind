from django.http import JsonResponse, HttpResponse
from django.shortcuts import render,redirect
from visitor.scripts.signin import *
from visitor import forms
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger('visitor')
def login(request):
    print(request.method)
    # print(request.META)
    if request.session.get('is_login',None):
        return redirect('/person_index/')
    if request.method == 'POST':
        print(request.POST)
        message = ''
        login_form = forms.loginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user_type = login_form.cleaned_data['usertype']
            try:
                user = models.User.objects.get(username=username)
                if user_type==user.usertype:
                    if user.password == password:
                        request.session['is_login'] = True
                        request.session['user_id'] = user.pk
                        request.session['user_name'] = user.username
                        request.session['user_type'] = user_type
                        request.session['user_role'] = user.roleid.rolename
                        # logger = Logger(username).getlogger()

                        if user_type == "个人用户":
                            logdata = [request.session['user_id'],request.session['user_role'],'/person_index/','登录','']
                            logger.debug(logdata)
                            return redirect('person_index')
                        if user_type == "企业用户":
                            logdata = [request.session['user_id'],request.session['user_role'], '/com_index/', '登录', '']
                            logger.debug(logdata)
                            return redirect('com_index')
                        if user_type == "政府用户":
                            logdata = [request.session['user_id'],request.session['user_role'], '/gov_index/', '登录', '']
                            logger.debug(logdata)
                            return redirect('gov_index')
                        if user_type == "事业单位用户":
                            logdata = [request.session['user_id'],request.session['user_role'], '/govcom_index/', '登录', '']
                            logger.debug(logdata)
                            return redirect('govcom_index')
                        if user_type == '管理员':
                            logdata = [request.session['user_id'],request.session['user_role'], '/bindex/', '登录', '']
                            logger.debug(logdata)
                            return redirect('index')
                        else:
                            return redirect('/login/')
                    else:
                        message = '密码错误'
                else:
                    message = '请确认用户类型'


            except Exception as e:
                print(e)
                request.session.flush()
                message = '无此用户'
        return render(request, 'foreground/login.html', locals())
    login_form = forms.loginForm()
    return render(request, 'foreground/login.html',locals())

def signin(request):
    if request.method == 'POST':
        userdata = request.POST
        print(type(userdata))
        if userdata.get('user-type') == '0':
            personUser(userdata)
            return redirect('/jump/')
        elif userdata.get('user-type') == '1':
            try:
                companyUser(request)
                return redirect('/jump/')
            except:
                error = 'error'
                return render(request, 'foreground/signin.html', {'message': error})
        elif userdata.get('user-type') == '2':
            try:
                govUser(request)
                return redirect('/jump/')
            except Exception as e:
                error = 'error'
                return render(request, 'foreground/signin.html', {'message': error})
        elif userdata.get('user-type') == '3':
            try:
                InstitutionUser(request)
                return  redirect('/jump/')
            except Exception as e:
                error = 'error'
                return render(request, 'foreground/signin.html', {'message': error})
        else:
            pass


    return render(request, 'foreground/signin.html')

@csrf_exempt
def checkuser(request):
    username = request.POST.get('user')
    count = models.User.objects.filter(username=username).count()
    if count==0:
        msg = 1
    else:
        msg = 0
    return JsonResponse({'msg':msg})

def jump(request):
    logdata = ['','', '/login/', '注册', '']
    logger.debug(logdata)
    return render(request, 'foreground/jump.html')

def logout(request):
    logdata = [request.session['user_id'],request.session['user_role'], '/login/', '退出', '']
    logger.debug(logdata)
    request.session.flush()
    return redirect("/login/")


