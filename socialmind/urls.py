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
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vviews.login, name='first'),
    path('captcha',include('captcha.urls')),
    path('logout/',vviews.logout),
    path('com_index/', vviews.com_index, name='com_index'),
    path('gov_index/', vviews.gov_index, name='gov_index'),
    path('person_index/', vviews.person_index, name='person_index'),
    path('govcom_index/', vviews.govcom_index, name='govcom_index'),
    path('login/', vviews.login, name='login'),
    path('signin/', vviews.signin, name='signin'),
    path('get_address/', vviews.get_address),
    path('checkuser/', vviews.checkuser),
    path('events/', vviews.events),
    path('profile/', vviews.profile),
    path('eventParticular/', vviews.eventparticular),
    path('fileParticular/', vviews.fileParticular),
    path('fileSearch/', vviews.fileSearch, name='fileSearch'),
    path('eventSearch/', vviews.eventSearch, name='eventSearch'),
    # background url
    path('bindex/', bviews.index, name='index'),
    path('blogin/', bviews.login, name='login'),
    path('SpiderList/', bviews.SpiderList),
    path('SpiderMonitor/', bviews.SpiderMonitor),
    path('SpiderConfigure/', bviews.SpiderConfigure),
    path('Author/', bviews.Author),
    path('ArticlesOfAuthor/', bviews.ArticlesOfAuthor),
    path('ArticlesAndComments/', bviews.ArticlesAndComments),
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
    path('operateDiary/', bviews.operateDiary),
    path('DouBanArticleStyle/', bviews.DouBanArticleStyle),
    path('usrManagement/<int:a>/', bviews.usrManagement1),
    path('test/',bviews.test),














]
