"""socialmind URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from visitor import views as vviews
from manager import views as bviews
from django.conf.urls import include
from visitor.view import loginviews,indexview,UserInfoManageview
from manager.view import loginview as bloginview,ArticleandAuthorview as bAAview
from manager.view import userManagement as umView
from manager.view import DataTableShowView,ObjectShowview
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginviews.login, name='first'),
    path('captcha',include('captcha.urls')),
    path('logout/',loginviews.logout),
    path('com_index/', indexview.com_index, name='com_index'),
    path('gov_index/', indexview.gov_index, name='gov_index'),
    path('person_index/', indexview.person_index, name='person_index'),
    path('govcom_index/', indexview.govcom_index, name='govcom_index'),
    path('login/', loginviews.login, name='login'),
    path('signin/', loginviews.signin, name='signin'),
    path('get_address/', vviews.get_address),
    path('checkuser/', loginviews.checkuser),
    path('events/', vviews.events),
    path('profile/', UserInfoManageview.profile),
    path('jump/',loginviews.jump),
    path('eventParticular/', vviews.eventparticular),
    path('fileParticular/', vviews.fileParticular),
    path('fileSearch/', vviews.fileSearch, name='fileSearch'),
    path('eventSearch/', vviews.eventSearch, name='eventSearch'),
    path('competitive_products/', vviews.competitive_products),
    # background url
    path('bindex/', bloginview.index, name='index'),
    path('blogin/', bloginview.login, name='login'),
    path('SpiderList/', bviews.SpiderList),
    path('SpiderMonitor/', bviews.SpiderMonitor),
    path('SpiderConfigure/', bviews.SpiderConfigure),
    path('Author/', bAAview.Author),
    path('ArticlesOfAuthor/', bAAview.ArticlesOfAuthor),#作者详情
    path('ArticlesAndComments/', bAAview.ArticlesAndComments),
    path('DataCleanStatistics/', bviews.DataCleanStatistics),
    path('DataCleanStrategies/', bviews.DataCleanStrategies),
    path('DataCleanLog/', bviews.DataCleanLog),
    path('washData/', bviews.washData),
    path('topics/', bviews.topics),
    path('AddEventObject/', bviews.AddEventObject),
    path('CreateEventObject/', bviews.CreateEventObject),
    path('ShowEventObject/', bviews.ShowEventObject),
    path('semanticsTools/', bviews.semanticsTools),
    path('semanticsToolkits/', bviews.semanticsToolkits),
    path('ShowToolkits/', bviews.ShowToolkits),
    path('usrCommentsSelect/', bviews.usrCommentsSelect),
    path('usrCommentsCheck/', bviews.usrCommentsCheck),
    path('usrCommentsDelete/', bviews.usrCommentsDelete),
    path('AssignAuthorities/', bviews.AssignAuthorities),
    path('usersVerify/', bviews.usersVerify),
    path('usrManagement/', bviews.usrManagement),
    path('usrManagement/List/person/', umView.personList),#个人用户管理
    path('usrManagement/List/company/', umView.companyList),#企业用户管理
    path('usrManagement/List/goverment/', umView.govermentList),#政府用户管理
    path('usrManagement/List/institute/', umView.instituteList),#事业单位用户管理
    path('operateDiary/', bviews.operateDiary),#日志管理
    path('DouBanArticleStyle/', bviews.DouBanArticleStyle),
    path('ArticlePaticular/', bAAview.ArticlePaticular),
    path('ArticlePaticular/getComments/', bAAview.ArticlePaticularComments),
    path('usrManagement/<int:a>/', bviews.usrManagement1),
    path('yuandatashow/',bviews.yuandatashow),
    path('yuandatashow/getyuandatas/',DataTableShowView.yuandatashow),
    path('operate/<int:a>/', bviews.operate),
    path('articlelist/',bAAview.articleslsit),
    path('objectshow/',bviews.objectshow),
    path('objectshow/event/',ObjectShowview.eventshow),
    path('objectshow/object/',ObjectShowview.objectshow),
    path('Eventshow/',bviews.eventshow),
    path('jianbao/',bviews.jianbao),
    path('qiantaimotaikuang',bviews.qiantaimotaikuang),
    path('operateDiary/getlogs/<int:logtype>/',bviews.getlogs),
    path('author/getAuthors/', bAAview.getAuthors), #/Author/作者信息ajax路径
    path('articlelist/getArticleList/', bAAview.getArticleList), #/articleList/文章信息ajax路径
    path('ArticlesOfAuthor/getAuthor_ArticleList/', bAAview.getAuthor_ArticleList), #/ArticlesOfAuthor/获得作者所有文章信息

    path('articlelist/deleteArticle/', bAAview.deleteArticle), #/articlelist/删除文章
    path('Author/authorDelete/', bAAview.deleteAuthor), #/Author/删除作者







]
