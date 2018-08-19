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
from manager.view import userManagement as umView, washData
from manager.view import DataTableShowView,ObjectShowview, userCommentsManage as ucView,SpiderView,washlog
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', loginviews.login, name='first'),
    path('captcha',include('captcha.urls')),
    path('logout/',loginviews.logout),
    path('com_index/', indexview.com_index, name='com_index'),
    path('loadOrganizationData/emotionTrend/', indexview.index_emotionTrend),
    path('gov_index/', indexview.gov_index, name='gov_index'),
    path('person_index/', indexview.person_index, name='person_index'),
    path('govcom_index/', indexview.govcom_index, name='govcom_index'),
    path('login/', loginviews.login, name='login'),
    path('signin/', loginviews.signin, name='signin'),
    path('get_address/', vviews.get_address),
    path('checkuser/', loginviews.checkuser),
    path('events/', vviews.events),
    path('events/getData/', vviews.getEventsData),
    path('events/getArticle/', vviews.getArticles),
    path('profile/', UserInfoManageview.profile),
    path('jump/',loginviews.jump),
    path('eventParticular/', vviews.eventparticular),
    path('eventParticular/getCorrelationFiles/', vviews.getCorrelationFiles),
    path('eventParticular/getComments/', vviews.getEventComments),
    path('eventParticular/getOperaData/', vviews.getEventOpera),
    path('fileParticular/', vviews.fileParticular),
    path('fileParticular/getCorrelationFiles/', vviews.getCorrelatFiles),
    path('fileParticular/getComments/', vviews.getArticleParticular),
    path('fileParticular/getOperaData/', vviews.getOperaData),
    path('fileSearch/', vviews.fileSearch, name='fileSearch'),
    path('fileSearch/getAllFile/', vviews.getAllFile, name='fileSearch'),
    path('addOperation/', vviews.addOperation),
    path('subOperation/', vviews.subOperation),
    path('addComment/', vviews.addComments),
    path('eventSearch/', vviews.eventSearch, name='eventSearch'),
    path('eventSearch/getEventList/', vviews.getEventList),
    path('competitive_products/', vviews.competitive_products),
    path('personalInfoForm/<int:a>/',UserInfoManageview.personalInfoForm),
    path('ComUsrForm/<int:a>/',UserInfoManageview.ComUsrForm),
    # path('PersonUsrForm/<int:a>/',UserInfoManageview.PersonUsrForm),
    # path('InstituUsrForm/<int:a>/',UserInfoManageview.InstituUsrForm),
    # path('GovUsrForm/<int:a>/',UserInfoManageview.GovUsrForm),
    path('ajaxInitComUsrForm/',UserInfoManageview.ajaxInitComUsrForm),
    path('ajaxInitPersonUsrForm/',UserInfoManageview.ajaxInitPersonUsrForm),
    path('ajaxInitInstitutionUsrForm/',UserInfoManageview.ajaxInitInstitutionUsrForm),
    path('ajaxInitGovUsrForm/',UserInfoManageview.ajaxInitGovUsrForm),
    # background url
    path('bindex/', bloginview.index, name='index'),
    path('bindex/bindexContent/<int:a>/', bloginview.bindexContent),
    path('bindex/searchcolnames/', bloginview.searchcolnames),
    path('bindex/bindexprovinceyuqing/', bloginview.provinceyuqing),
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
    path('washData/yuanshujubiao/',washData.yuanshujubiao),
    path('washData/xuanzewangzhan/',washData.xuanzewangzhan),
    path('washData/DIYfenye/',washData.DIYfenye),
    path('washData/tongji/',washData.tongji),
    path('washData/washaction/',washData.washaction),
    path('washData/rollback/',washData.rollback),
    path('topics/', bviews.topics),
    path('AddEventObject/', bviews.AddEventObject),
    path('CreateEventObject/', bviews.CreateEventObject),
    path('ShowEventObject/', bviews.ShowEventObject),
    path('semanticsTools/', bviews.semanticsTools),
    path('semanticsToolkits/', bviews.semanticsToolkits),
    path('ShowToolkits/', bviews.ShowToolkits),
    path('usrCommentsSelect/', bviews.usrCommentsSelect),#用户留言管理
    path('usrCommentsSelect/commentsCheck/', ucView.checkComments),
    path('usrCommentsSelect/commentsManage/', ucView.manageComments),
    path('usrCommentsSelect/commentsManage/pass/', ucView.commentPass),
    path('usrCommentsSelect/commentsManage/noPass/', ucView.noPass),
    path('usrCommentsSelect/commentsManage/deleteComment/', ucView.deleteComment),
    path('usrCommentsCheck/', bviews.usrCommentsCheck),
    path('usrCommentsDelete/', bviews.usrCommentsDelete),
    path('AssignAuthorities/', bviews.AssignAuthorities),
    path('usersVerify/', bviews.usersVerify),
    path('usrManagement/', bviews.usrManagement),
    path('usrManagement/List/person/', umView.personList),#个人用户管理
    path('usrManagement/List/company/', umView.companyList),#企业用户管理
    path('usrManagement/List/goverment/', umView.govermentList),#政府用户管理
    path('usrManagement/List/institute/', umView.instituteList),#事业单位用户管理
    path('usrManagement/deleteUser/', umView.deleteUser),
    path('operateDiary/', bviews.operateDiary),#日志管理
    path('DouBanArticleStyle/', bviews.DouBanArticleStyle),
    path('ArticlePaticular/', bAAview.ArticlePaticular),
    path('ArticlePaticular/getComments/', bAAview.ArticlePaticularComments),
    path('usrManagement/<int:a>/', bviews.usrManagement1),
    path('yuandatashow/',bviews.yuandatashow),
    path('yuandatashow/getyuandatas/',DataTableShowView.yuandatashow),
    path('operate/<int:a>/', bviews.operate),
    path('articlelist/',bAAview.articleslsit),
    path('objectarticle/<str:id>/',bAAview.objectarticle),
    path('objectarticlelsit/',bAAview.objectarticlelist),
    path('objectshow/',bviews.objectshow),
    path('objectshow/event/',ObjectShowview.eventshow),
    path('objectshow/object/',ObjectShowview.objectshow),
    path('objectshow/entity/',ObjectShowview.entitydata),
    path('Eventshow/',bviews.eventshow),
    path('jianbao/',bviews.jianbao),
    path('qiantaimotaikuang',bviews.qiantaimotaikuang),
    path('operateDiary/getlogs/<int:logtype>/',bviews.getlogs),
    path('author/getAuthors/', bAAview.getAuthors), #/Author/作者信息ajax路径
    path('articlelist/getArticleList/', bAAview.getArticleList), #/articleList/文章信息ajax路径
    path('ArticlesOfAuthor/getAuthor_ArticleList/', bAAview.getAuthor_ArticleList), #/ArticlesOfAuthor/获得作者所有文章信息

    path('articlelist/deleteArticle/', bAAview.deleteArticle), #/articlelist/删除文章
    path('Author/authorDelete/', bAAview.deleteAuthor), #/Author/删除作者
    path('getspiderlist/',SpiderView.getspiderlist) , #获取爬虫列表
    path('runspider/',SpiderView.runspider),
    path('stopspider/',SpiderView.stopspider),
    path('getspiderconfig/',SpiderView.getspiderconfig),
    path('getspiderconfigbyid/',SpiderView.getspiderconfigbyid),
    path('changeconfig/',SpiderView.changeconfig),
    path('delconfig/',SpiderView.delconfig),
    path('addconfig/',SpiderView.addconfig),
    path('addspider/',SpiderView.addspider),
    path('delspider/',SpiderView.delspider),
    path('queryspider/',SpiderView.queryspider),
    path('queryspiderspeed/',SpiderView.queryspiderspeed),
    path('queryerror/',SpiderView.queryerror),
    path('queryspidernum/',SpiderView.queryspidernum),
    path('errorlog/',SpiderView.geterrorlog),
    path('spiderlog/',SpiderView.getspiderlog),
    path('delentity/',ObjectShowview.delentity),
    path('washlog/',washlog.washlog)









]
