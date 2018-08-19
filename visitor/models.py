# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Admin(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', primary_key=True)  # Field name made lowercase.
    realname = models.CharField(db_column='realName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class Area(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    citycode = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'area'


class Article(models.Model):
    articleid = models.CharField(db_column='articleID', primary_key=True, max_length=36)  # Field name made lowercase.
    sourcearticleid = models.CharField(db_column='sourceArticleID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    authorid = models.ForeignKey('Author', models.DO_NOTHING, db_column='authorID', blank=True, null=True)  # Field name made lowercase.
    title = models.CharField(max_length=256, blank=True, null=True)
    keywords = models.CharField(db_column='keyWords', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    posttime = models.CharField(db_column='postTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    commentnumber = models.IntegerField(db_column='commentNumber', blank=True, null=True)  # Field name made lowercase.
    scannumber = models.IntegerField(db_column='scanNumber', blank=True, null=True)  # Field name made lowercase.
    participationnumber = models.IntegerField(db_column='participationNumber', blank=True, null=True)  # Field name made lowercase.
    replynumber = models.IntegerField(db_column='replyNumber', blank=True, null=True)  # Field name made lowercase.
    likenumber = models.IntegerField(db_column='likeNumber', blank=True, null=True)  # Field name made lowercase.
    recommendnumber = models.IntegerField(db_column='recommendNumber', blank=True, null=True)  # Field name made lowercase.
    collectnumber = models.IntegerField(db_column='collectNumber', blank=True, null=True)  # Field name made lowercase.
    givereward = models.IntegerField(db_column='giveReward', blank=True, null=True)  # Field name made lowercase.
    transmitnumber = models.IntegerField(db_column='transmitNumber', blank=True, null=True)  # Field name made lowercase.
    tramplenumber = models.IntegerField(db_column='trampleNumber', blank=True, null=True)  # Field name made lowercase.
    newsresource = models.CharField(db_column='newsResource', max_length=64, blank=True, null=True)  # Field name made lowercase.
    similardegree = models.FloatField(db_column='similarDegree', blank=True, null=True)  # Field name made lowercase.
    websiteid = models.ForeignKey('Website', models.DO_NOTHING, db_column='websiteID', blank=True, null=True)  # Field name made lowercase.
    objectid = models.ForeignKey('Object', models.DO_NOTHING, db_column='objectID', blank=True, null=True)  # Field name made lowercase.
    sourceauthorid = models.CharField(db_column='sourceAuthorID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'article'


class ArticleComment(models.Model):
    article_commentid = models.CharField(db_column='article_commentID', primary_key=True, max_length=36)  # Field name made lowercase.
    sourcecommentid = models.CharField(db_column='sourceCommentID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    authorid = models.ForeignKey('Author', models.DO_NOTHING, db_column='authorID', blank=True, null=True)  # Field name made lowercase.
    likenumber = models.IntegerField(db_column='likeNumber', blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    commenttime = models.CharField(db_column='commentTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    replaynumber = models.IntegerField(db_column='replayNumber', blank=True, null=True)  # Field name made lowercase.
    graphurl = models.CharField(db_column='graphURL', max_length=64, blank=True, null=True)  # Field name made lowercase.
    articleid = models.ForeignKey(Article, models.DO_NOTHING, db_column='articleID', blank=True, null=True)  # Field name made lowercase.
    fathercommentid = models.ForeignKey('self', models.DO_NOTHING, db_column='fatherCommentID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'article_comment'


class ArticleLabeled(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    articleid = models.CharField(db_column='articleID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    istrue = models.CharField(db_column='isTrue', max_length=10, blank=True, null=True)  # Field name made lowercase.
    credtype = models.CharField(db_column='credType', max_length=20, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'article_labeled'


class ArticleSimilar(models.Model):
    articlesimilarid = models.CharField(db_column='articleSimilarID', primary_key=True, max_length=64)  # Field name made lowercase.
    articleoneid = models.ForeignKey(Article, models.DO_NOTHING, db_column='articleOneID', blank=True, null=True, related_name="articleoneid")  # Field name made lowercase.
    articletwoid = models.ForeignKey(Article, models.DO_NOTHING, db_column='articleTwoID', blank=True, null=True, related_name="articletwoid")  # Field name made lowercase.
    similardegree = models.FloatField(db_column='similarDegree', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'article_similar'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Author(models.Model):
    authorid = models.CharField(db_column='authorID', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(max_length=64, blank=True, null=True)
    sex = models.CharField(max_length=16, blank=True, null=True)
    birthday = models.CharField(max_length=32, blank=True, null=True)
    address = models.CharField(max_length=64, blank=True, null=True)
    focusnumber = models.IntegerField(db_column='focusNumber', blank=True, null=True)  # Field name made lowercase.
    fansnumber = models.IntegerField(db_column='fansNumber', blank=True, null=True)  # Field name made lowercase.
    age = models.IntegerField(blank=True, null=True)
    friendnumber = models.IntegerField(db_column='friendNumber', blank=True, null=True)  # Field name made lowercase.
    replaynumber = models.IntegerField(db_column='replayNumber', blank=True, null=True)  # Field name made lowercase.
    clicknumber = models.IntegerField(db_column='clickNumber', blank=True, null=True)  # Field name made lowercase.
    loginnumber = models.IntegerField(db_column='loginNumber', blank=True, null=True)  # Field name made lowercase.
    introduction = models.CharField(max_length=255, blank=True, null=True)
    registrationtime = models.CharField(db_column='registrationTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    educationbackground = models.CharField(db_column='educationBackground', max_length=32, blank=True, null=True)  # Field name made lowercase.
    career = models.CharField(max_length=32, blank=True, null=True)
    elitepostnumber = models.IntegerField(db_column='elitePostNumber', blank=True, null=True)  # Field name made lowercase.
    score = models.IntegerField(blank=True, null=True)
    onlinetime = models.CharField(db_column='onlineTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    famedegree = models.IntegerField(db_column='fameDegree', blank=True, null=True)  # Field name made lowercase.
    lastlogintime = models.CharField(db_column='lastLoginTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    workunit = models.CharField(db_column='workUnit', max_length=64, blank=True, null=True)  # Field name made lowercase.
    updatearticaltime = models.CharField(db_column='updateArticalTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    phonenumber = models.CharField(db_column='phoneNumber', max_length=32, blank=True, null=True)  # Field name made lowercase.
    reputation = models.IntegerField(blank=True, null=True)
    getreward = models.IntegerField(db_column='getReward', blank=True, null=True)  # Field name made lowercase.
    givereward = models.IntegerField(db_column='giveReward', blank=True, null=True)  # Field name made lowercase.
    iscertification = models.IntegerField(db_column='isCertification', blank=True, null=True)  # Field name made lowercase.
    portraiturl = models.CharField(db_column='portraitURL', max_length=64, blank=True, null=True)  # Field name made lowercase.
    realname = models.CharField(db_column='realName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    sexualorientation = models.CharField(db_column='sexualOrientation', max_length=16, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(max_length=64, blank=True, null=True)
    qq = models.CharField(db_column='QQ', max_length=64, blank=True, null=True)  # Field name made lowercase.
    bloodtype = models.CharField(db_column='bloodType', max_length=16, blank=True, null=True)  # Field name made lowercase.
    isbigv = models.IntegerField(db_column='isBigV', blank=True, null=True)  # Field name made lowercase.
    sourceauthorid = models.CharField(db_column='sourceAuthorID', max_length=255, blank=True, null=True)  # Field name made lowercase.
    websiteid = models.ForeignKey('Website', models.DO_NOTHING, db_column='websiteID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'author'


class Bulletin(models.Model):
    bulletinid = models.CharField(db_column='bulletinID', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(max_length=64, blank=True, null=True)
    introduction = models.CharField(max_length=255, blank=True, null=True)
    bulletinurl = models.CharField(db_column='bulletinURL', max_length=64, blank=True, null=True)  # Field name made lowercase.
    bulletintype = models.CharField(db_column='bulletinType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    generatetime = models.CharField(db_column='generateTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    bulletinstyleid = models.ForeignKey('BulletinStyleId', models.DO_NOTHING, db_column='bulletinStyleID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bulletin'


class BulletinImageUrl(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    event_name = models.CharField(max_length=128, blank=True, null=True)
    image_url = models.CharField(max_length=512)

    class Meta:
        managed = False
        db_table = 'bulletin_image_url'


class BulletinStyleId(models.Model):
    bulletinstyleid = models.CharField(db_column='bulletinStyleID', primary_key=True, max_length=36)  # Field name made lowercase.
    name = models.CharField(max_length=64, blank=True, null=True)
    introduction = models.CharField(max_length=255, blank=True, null=True)
    covergraph = models.TextField(db_column='coverGraph', blank=True, null=True)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=64, blank=True, null=True)  # Field name made lowercase.
    uploadtime = models.CharField(db_column='uploadTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    downloadnumber = models.IntegerField(db_column='downloadNumber', blank=True, null=True)  # Field name made lowercase.
    likenumber = models.IntegerField(db_column='likeNumber', blank=True, null=True)  # Field name made lowercase.
    collectnumber = models.IntegerField(db_column='collectNumber', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'bulletin_style_id'


class CaptchaCaptchastore(models.Model):
    challenge = models.CharField(max_length=32)
    response = models.CharField(max_length=32)
    hashkey = models.CharField(unique=True, max_length=40)
    expiration = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'captcha_captchastore'


class City(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)
    provincecode = models.CharField(max_length=6)

    class Meta:
        managed = False
        db_table = 'city'


class CleanLocation(models.Model):
    cleanlocationid = models.CharField(db_column='cleanLocationID', primary_key=True, max_length=36)  # Field name made lowercase.
    tableid = models.CharField(db_column='tableID', max_length=32, blank=True, null=True)  # Field name made lowercase.
    columnname = models.CharField(db_column='columnName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    rowkey = models.CharField(max_length=64, blank=True, null=True)
    columnfamily = models.CharField(db_column='columnFamily', max_length=64, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.IntegerField(db_column='timeStamp', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clean_location'


class CleanLogManager(models.Model):
    cleanlogid = models.CharField(db_column='cleanLogID', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    user_define_old_value = models.CharField(max_length=255, blank=True, null=True)
    cleantime = models.CharField(db_column='cleanTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    cleanstategyid = models.ForeignKey('CleanStrategy', models.DO_NOTHING, db_column='cleanStategyID', blank=True, null=True)  # Field name made lowercase.
    tablename = models.CharField(db_column='tableName', max_length=36, blank=True, null=True)  # Field name made lowercase.
    columnname = models.CharField(db_column='columnName', max_length=36, blank=True, null=True)  # Field name made lowercase.
    user_define_new_value = models.CharField(max_length=255, blank=True, null=True)
    resultstate = models.CharField(db_column='resultState', max_length=36, blank=True, null=True)  # Field name made lowercase.
    response_time = models.CharField(max_length=255, blank=True, null=True)
    errorcode = models.CharField(db_column='errorCode', max_length=255, blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=36, blank=True, null=True)  # Field name made lowercase.
    errormessage = models.TextField(db_column='errorMessage', blank=True, null=True)  # Field name made lowercase.
    self_defining_value = models.CharField(max_length=255, blank=True, null=True)
    cleanlocationid = models.CharField(db_column='cleanLocationID', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'clean_log_manager'


class CleanStrategy(models.Model):
    isuse = models.CharField(db_column='IsUse', max_length=8, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=64, blank=True, null=True)
    cleanstategyid = models.CharField(db_column='cleanStategyID', primary_key=True, max_length=36)  # Field name made lowercase.
    type = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'clean_strategy'


class CleanerrorNotUsed(models.Model):
    exceptionid = models.CharField(db_column='exceptionID', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.CharField(db_column='UserID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    operatime = models.CharField(db_column='operaTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    userip = models.CharField(db_column='userIP', max_length=36, blank=True, null=True)  # Field name made lowercase.
    errorcode = models.CharField(db_column='errorCode', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'cleanerror(not used)'


class ClickEvent(models.Model):
    objectid = models.CharField(db_column='objectID', max_length=36)  # Field name made lowercase.
    clicknum = models.IntegerField(db_column='clickNum', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'click_event'


class Comment(models.Model):
    commentid = models.CharField(db_column='commentID', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    commentcontent = models.CharField(db_column='commentContent', max_length=255, blank=True, null=True)  # Field name made lowercase.
    fathercommentid = models.ForeignKey('self', models.DO_NOTHING, db_column='fathercommentID', blank=True, null=True)  # Field name made lowercase.
    commenttime = models.CharField(db_column='commentTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    articleid = models.ForeignKey(Article, models.DO_NOTHING, db_column='articleid', blank=True, null=True)
    checked = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'comment'


class CompanyUser(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', primary_key=True)  # Field name made lowercase.
    idfronturl = models.CharField(db_column='IDFrontUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    companyname = models.CharField(db_column='companyName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    idbackurl = models.CharField(db_column='IDBackUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    businesslicenceurl = models.CharField(db_column='businessLicenceUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    businesslicenceid = models.CharField(db_column='businessLicenceId', max_length=64, blank=True, null=True)  # Field name made lowercase.
    businessscope = models.CharField(db_column='businessScope', max_length=32, blank=True, null=True)  # Field name made lowercase.
    companytype = models.CharField(db_column='companyType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    interest = models.CharField(max_length=32, blank=True, null=True)
    realname = models.CharField(db_column='RealName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    registerorg = models.CharField(db_column='registerORG', max_length=32, blank=True, null=True)  # Field name made lowercase.
    registertime = models.CharField(db_column='registerTime', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'company_user'


class ConfigConfigitem(models.Model):
    spiderconfigitemid = models.CharField(db_column='spiderConfigItemID', primary_key=True, max_length=36)  # Field name made lowercase.
    spiderconfigid = models.ForeignKey('SpiderConfig', models.DO_NOTHING, db_column='spiderConfigID', blank=True, null=True)  # Field name made lowercase.
    configitemid = models.ForeignKey('Configitem', models.DO_NOTHING, db_column='configItemID', blank=True, null=True)  # Field name made lowercase.
    configitemvalue = models.CharField(db_column='configItemValue', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'config_configitem'


class Configitem(models.Model):
    configitemid = models.CharField(db_column='configItemID', primary_key=True, max_length=36)  # Field name made lowercase.
    displayname = models.CharField(db_column='displayName', max_length=500, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=1000, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    defaultvalue = models.CharField(db_column='defaultValue', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'configitem'


class DataDictionary(models.Model):
    attributevalue = models.CharField(db_column='attributeValue', max_length=128, blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=255, blank=True, null=True)
    attributename = models.CharField(db_column='attributeName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    datadictionaryid = models.CharField(db_column='dataDictionaryID', primary_key=True, max_length=36)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data_dictionary'


class DataSource(models.Model):
    tablenameid = models.CharField(db_column='tableNameID', primary_key=True, max_length=36)  # Field name made lowercase.
    tablename = models.CharField(db_column='tableName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    websiteid = models.ForeignKey('Website', models.DO_NOTHING, db_column='websiteID', blank=True, null=True)  # Field name made lowercase.
    count = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data_source'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Entity(models.Model):
    objectid = models.CharField(db_column='objectID', max_length=64, blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=512, blank=True, null=True)
    type = models.CharField(max_length=512, blank=True, null=True)
    articlelist = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'entity'


class Event(models.Model):
    objectid = models.ForeignKey('Object', models.DO_NOTHING, db_column='objectID', primary_key=True)  # Field name made lowercase.
    eventsummary = models.CharField(db_column='eventSummary', max_length=1024, blank=True, null=True)  # Field name made lowercase.
    eventbegintime = models.CharField(db_column='eventBeginTime', max_length=128, blank=True, null=True)  # Field name made lowercase.
    eventendtime = models.CharField(db_column='eventEndTime', max_length=128, blank=True, null=True)  # Field name made lowercase.
    introduction = models.CharField(max_length=1024, blank=True, null=True)
    eventbeaintime = models.CharField(db_column='eventBeainTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    eventovertime = models.CharField(db_column='eventOverTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(max_length=256, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event'


class EventOpinion(models.Model):
    opinionid = models.CharField(db_column='opinionID', primary_key=True, max_length=36)  # Field name made lowercase.
    objectid = models.CharField(db_column='objectID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    articleid = models.CharField(db_column='articleID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    content = models.TextField(blank=True, null=True)
    direct_weight = models.FloatField(blank=True, null=True)
    place_weight = models.FloatField(blank=True, null=True)
    similar_title = models.FloatField(blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_opinion'


class EventSeedsBase(models.Model):
    eventid = models.CharField(db_column='eventID', primary_key=True, max_length=36)  # Field name made lowercase.
    eventname = models.CharField(db_column='eventName', max_length=512, blank=True, null=True)  # Field name made lowercase.
    eventintroduction = models.TextField(db_column='eventIntroduction', blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='startTime', max_length=256, blank=True, null=True)  # Field name made lowercase.
    istrue = models.CharField(db_column='isTrue', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'event_seeds_base'


class GovUser(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', primary_key=True)  # Field name made lowercase.
    govname = models.CharField(db_column='govName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    govcode = models.CharField(db_column='govCode', max_length=32, blank=True, null=True)  # Field name made lowercase.
    idfronturl = models.CharField(db_column='IDFrontUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idbackurl = models.CharField(db_column='IDBackUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    govtype = models.CharField(db_column='govType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    idcard = models.CharField(db_column='IDCard', max_length=255, blank=True, null=True)  # Field name made lowercase.
    interest = models.CharField(max_length=255, blank=True, null=True)
    realname = models.CharField(db_column='realName', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'gov_user'


class IndicatorValue(models.Model):
    indicatorvalueid = models.CharField(db_column='indicatorValueID', primary_key=True, max_length=36)  # Field name made lowercase.
    objectid = models.ForeignKey('Object', models.DO_NOTHING, db_column='objectID', blank=True, null=True)  # Field name made lowercase.
    indicatorvalue = models.CharField(db_column='indicatorValue', max_length=64, blank=True, null=True)  # Field name made lowercase.
    indexname = models.CharField(db_column='indexName', max_length=36, blank=True, null=True)  # Field name made lowercase.
    dimensionname = models.CharField(db_column='dimensionName', max_length=36, blank=True, null=True)  # Field name made lowercase.
    dimensionvalue = models.CharField(db_column='dimensionValue', max_length=36, blank=True, null=True)  # Field name made lowercase.
    starttime = models.CharField(db_column='startTime', max_length=128, blank=True, null=True)  # Field name made lowercase.
    endtime = models.CharField(db_column='endTime', max_length=128, blank=True, null=True)  # Field name made lowercase.
    timesolt = models.CharField(db_column='timeSolt', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'indicator_value'


class InstitutionUser(models.Model):
    realname = models.CharField(db_column='realName', max_length=32, blank=True, null=True)  # Field name made lowercase.
    idfronturl = models.CharField(db_column='IDFrontUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idbackurl = models.CharField(db_column='IDBackUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    institutionname = models.CharField(db_column='institutionName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    institudecode = models.CharField(db_column='institudeCode', max_length=64, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', primary_key=True)  # Field name made lowercase.
    idfront = models.CharField(db_column='IDFront', max_length=255, blank=True, null=True)  # Field name made lowercase.
    idback = models.CharField(db_column='IDBack', max_length=255, blank=True, null=True)  # Field name made lowercase.
    institudeurl = models.CharField(db_column='institudeUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    institutionlevel = models.CharField(db_column='institutionLevel', max_length=64, blank=True, null=True)  # Field name made lowercase.
    institutiontype = models.CharField(db_column='institutionType', max_length=64, blank=True, null=True)  # Field name made lowercase.
    interest = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institution_user'


class Keyword(models.Model):
    keywordid = models.CharField(db_column='keywordID', primary_key=True, max_length=36)  # Field name made lowercase.
    objectid = models.ForeignKey('Object', models.DO_NOTHING, db_column='objectID', blank=True, null=True)  # Field name made lowercase.
    keyword = models.CharField(max_length=64, blank=True, null=True)
    weight = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'keyword'


class KeywordRelatedDegree(models.Model):
    keyworddegreeid = models.CharField(db_column='keywordDegreeID', primary_key=True, max_length=64)  # Field name made lowercase.
    keywordoneid = models.ForeignKey(Keyword, models.DO_NOTHING, db_column='keywordOneID', blank=True, null=True, related_name='keywordoneid')  # Field name made lowercase.
    keywordtwoid = models.ForeignKey(Keyword, models.DO_NOTHING, db_column='keywordTwoID', blank=True, null=True, related_name='keywordtwoid')  # Field name made lowercase.
    relateddegree = models.FloatField(db_column='relatedDegree', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'keyword_related_degree'


class Log(models.Model):
    logid = models.CharField(db_column='logID', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=64, blank=True, null=True)  # Field name made lowercase.
    logtime = models.CharField(db_column='logTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    methodlogicname = models.CharField(db_column='methodLogicName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    method = models.CharField(max_length=255, blank=True, null=True)
    param = models.CharField(max_length=1000, blank=True, null=True)
    sourcepage = models.CharField(db_column='sourcePage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    targetpage = models.CharField(db_column='targetPage', max_length=255, blank=True, null=True)  # Field name made lowercase.
    staytime = models.CharField(db_column='stayTime', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'log'


class Message(models.Model):
    messageid = models.CharField(db_column='messageID', primary_key=True, max_length=36)  # Field name made lowercase.
    messagecontent = models.TextField(db_column='messageContent', blank=True, null=True)  # Field name made lowercase.
    messagetime = models.CharField(db_column='messageTime', max_length=36, blank=True, null=True)  # Field name made lowercase.
    objectid = models.ForeignKey('Object', models.DO_NOTHING, db_column='objectID', blank=True, null=True)  # Field name made lowercase.
    checked = models.CharField(max_length=1, blank=True, null=True)
    userid = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message'


class MessageUser(models.Model):
    messageuserid = models.CharField(db_column='messageUserID', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    messageid = models.ForeignKey(Message, models.DO_NOTHING, db_column='messageID', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=36, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'message_user'


class News(models.Model):
    article_key = models.CharField(primary_key=True, max_length=45)
    article_id = models.BigIntegerField(unique=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    path_text = models.CharField(max_length=100, blank=True, null=True)
    path_href = models.TextField(blank=True, null=True)
    keywords = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=45, blank=True, null=True)
    author = models.CharField(max_length=45, blank=True, null=True)
    editor = models.CharField(max_length=45, blank=True, null=True)
    date_time = models.DateTimeField(blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    picture_url = models.TextField(blank=True, null=True)
    join_count = models.IntegerField(blank=True, null=True)
    reply_count = models.IntegerField(blank=True, null=True)
    comment_ids = models.TextField(blank=True, null=True)
    b_picture = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'news'
        unique_together = (('article_key', 'article_id'),)


class Notice(models.Model):
    noticeid = models.CharField(db_column='noticeID', primary_key=True, max_length=36)  # Field name made lowercase.
    noticetitle = models.TextField(db_column='noticeTitle', blank=True, null=True)  # Field name made lowercase.
    noticecontent = models.TextField(db_column='noticeContent', blank=True, null=True)  # Field name made lowercase.
    notictime = models.CharField(db_column='noticTime', max_length=36, blank=True, null=True)  # Field name made lowercase.
    adminid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='adminID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notice'


class NoticeRole(models.Model):
    noticeroleid = models.CharField(db_column='noticeRoleID', primary_key=True, max_length=36)  # Field name made lowercase.
    noticeid = models.ForeignKey(Notice, models.DO_NOTHING, db_column='noticeID', blank=True, null=True)  # Field name made lowercase.
    roleid = models.ForeignKey('Role', models.DO_NOTHING, db_column='roleID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'notice_role'


class Object(models.Model):
    objectid = models.CharField(db_column='objectID', primary_key=True, max_length=36)  # Field name made lowercase.
    scannumber = models.IntegerField(db_column='scanNumber', blank=True, null=True)  # Field name made lowercase.
    collectnumber = models.IntegerField(db_column='collectNumber', blank=True, null=True)  # Field name made lowercase.
    likenumber = models.IntegerField(db_column='likeNumber', blank=True, null=True)  # Field name made lowercase.
    truenumber = models.IntegerField(db_column='trueNumber', blank=True, null=True)  # Field name made lowercase.
    falsenumber = models.IntegerField(db_column='falseNumber', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(max_length=64, blank=True, null=True)
    addtime = models.CharField(db_column='addTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    place = models.CharField(max_length=64, blank=True, null=True)
    objecttype = models.CharField(db_column='objectType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    objectfatherid = models.ForeignKey('self', models.DO_NOTHING, db_column='objectFatherID', blank=True, null=True)  # Field name made lowercase.
    commentnumber = models.IntegerField(db_column='commentNumber', blank=True, null=True)  # Field name made lowercase.
    introduction = models.CharField(max_length=255, blank=True, null=True)
    credibility = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'object'


class ObjectUser(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    otype = models.CharField(db_column='oType', max_length=255, blank=True, null=True)  # Field name made lowercase.
    objectid = models.ForeignKey(Object, models.DO_NOTHING, db_column='objectID', blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    keywords = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'object_user'


class Operate(models.Model):
    operateid = models.CharField(db_column='operateID', primary_key=True, max_length=36)  # Field name made lowercase.
    operatename = models.CharField(db_column='operateName', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'operate'


class Permission(models.Model):
    permissionid = models.CharField(db_column='permissionID', primary_key=True, max_length=36)  # Field name made lowercase.
    permissionname = models.CharField(db_column='permissionName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    action = models.CharField(max_length=128, blank=True, null=True)
    resourceid = models.ForeignKey('Resource', models.DO_NOTHING, db_column='resourceID', blank=True, null=True)  # Field name made lowercase.
    operateid = models.ForeignKey(Operate, models.DO_NOTHING, db_column='operateID', blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)
    name_logic = models.CharField(max_length=255, blank=True, null=True)
    permission_physics = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'permission'


class PersonUser(models.Model):
    userid = models.ForeignKey('User', models.DO_NOTHING, db_column='userID', primary_key=True)  # Field name made lowercase.
    sex = models.CharField(max_length=16, blank=True, null=True)
    birthday = models.CharField(max_length=32, blank=True, null=True)
    phonenumber = models.CharField(db_column='phoneNumber', max_length=64, blank=True, null=True)  # Field name made lowercase.
    hobby = models.CharField(max_length=64, blank=True, null=True)
    career = models.CharField(max_length=32, blank=True, null=True)
    realname = models.CharField(db_column='realName', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'person_user'


class Province(models.Model):
    code = models.CharField(max_length=6)
    name = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'province'


class Resource(models.Model):
    resourceid = models.CharField(db_column='resourceID', primary_key=True, max_length=36)  # Field name made lowercase.
    resourcename = models.CharField(db_column='resourceName', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'resource'


class Role(models.Model):
    roleid = models.CharField(db_column='roleID', primary_key=True, max_length=36)  # Field name made lowercase.
    rolename = models.CharField(db_column='roleName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'role'


class RolePermission(models.Model):
    role_permissionid = models.CharField(db_column='role_permissionID', primary_key=True, max_length=36)  # Field name made lowercase.
    roleid = models.ForeignKey(Role, models.DO_NOTHING, db_column='roleID', blank=True, null=True)  # Field name made lowercase.
    permissionid = models.ForeignKey(Permission, models.DO_NOTHING, db_column='permissionID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'role_permission'


class Similaraa(models.Model):
    articleid = models.CharField(db_column='articleID', primary_key=True, max_length=64)  # Field name made lowercase.
    similararticle = models.TextField(blank=True, null=True)
    keywords = models.CharField(max_length=512, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'similaraa'


class SpiderConfig(models.Model):
    spiderconfigid = models.CharField(db_column='spiderConfigID', primary_key=True, max_length=36)  # Field name made lowercase.
    configtime = models.CharField(db_column='configTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    spiderruntime = models.CharField(db_column='spiderRunTime', max_length=64, blank=True, null=True)  # Field name made lowercase.
    logpath = models.CharField(db_column='logPath', max_length=64, blank=True, null=True)  # Field name made lowercase.
    filepath = models.CharField(db_column='filePath', max_length=64, blank=True, null=True)  # Field name made lowercase.
    spiderfrequency = models.IntegerField(db_column='spiderFrequency', blank=True, null=True)  # Field name made lowercase.
    configname = models.CharField(db_column='configName', max_length=64, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spider_config'


class SpiderConfigItem(models.Model):
    spiderconfigitemid = models.CharField(db_column='spiderConfigItemID', primary_key=True, max_length=36)  # Field name made lowercase.
    spiderconfigid = models.ForeignKey(SpiderConfig, models.DO_NOTHING, db_column='spiderConfigID', blank=True, null=True)  # Field name made lowercase.
    configitemname = models.CharField(db_column='configItemName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    configitemvalue = models.TextField(db_column='configItemValue', blank=True, null=True)  # Field name made lowercase.
    note = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'spider_config_item'


class SpiderErrorLog(models.Model):
    logid = models.CharField(db_column='logID', primary_key=True, max_length=36)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=255, blank=True, null=True)  # Field name made lowercase.
    erroritem = models.CharField(db_column='errorItem', max_length=255, blank=True, null=True)  # Field name made lowercase.
    errordetails = models.TextField(db_column='errorDetails', blank=True, null=True)  # Field name made lowercase.
    websiteid = models.ForeignKey('Website', models.DO_NOTHING, db_column='websiteID', blank=True, null=True)  # Field name made lowercase.
    spiderid = models.ForeignKey('SpiderInfo', models.DO_NOTHING, db_column='spiderID', blank=True, null=True)  # Field name made lowercase.
    errortime = models.CharField(db_column='errorTime', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'spider_error_log'


class SpiderInfo(models.Model):
    spiderid = models.CharField(db_column='spiderID', primary_key=True, max_length=36)  # Field name made lowercase.
    spidername = models.CharField(db_column='spiderName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    addtime = models.CharField(db_column='addTime', max_length=32, blank=True, null=True)  # Field name made lowercase.
    spidersourcepath = models.CharField(db_column='spiderSourcePath', max_length=64, blank=True, null=True)  # Field name made lowercase.
    # filename = models.CharField(db_column='fileName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    websiteid = models.ForeignKey('Website', models.DO_NOTHING, db_column='websiteID', blank=True, null=True)  # Field name made lowercase.
    # RunCommand = models.CharField(db_column='runcommend', max_length=128, blank=True, null=True)  # Field name made lowercase.
    RunCommand = models.CharField(db_column='runcommand', max_length=128, blank=True, null=True)  # Field name made lowercase.
    spiderstate = models.CharField(db_column='spiderState', max_length=32, blank=True, null=True)  # Field name made lowercase.
    spiderconfigid = models.ForeignKey(SpiderConfig, models.DO_NOTHING, db_column='spiderConfigID', blank=True, null=True)  # Field name made lowercase.
    vimname = models.CharField(max_length=16, blank=True, null=True)
    spiderrunname = models.CharField(max_length=32,blank=True,null=True)
    # spiderrunname1 = models.CharField(max_length=32,blank=True,null=True)
    class Meta:
        db_table = 'spider_info'

class NewSpiderConfig(models.Model):
    spiderconfigid = models.CharField(max_length=64,primary_key=True)
    spiderconfigname = models.CharField(max_length=32,blank=True,null=True)
    isrobot = models.CharField(max_length=4,blank=True,null=True)
    maxdownbytes = models.CharField(max_length=32,blank=True,null=True)
    downloadtimeout = models.CharField(max_length=32,blank=True,null=True)
    dnstimeout = models.CharField(max_length=32,blank=True,null=True)
    maxdeep = models.CharField(max_length=32,blank=True,null=True)
    ipconcurrentrequest = models.CharField(max_length=32,blank=True,null=True)
    siteconcurrentrequest = models.CharField(max_length=32,blank=True,null=True)
    maxconcurrentprocessing = models.CharField(max_length=32,blank=True,null=True)
    iscollectdeepdata = models.CharField(max_length=32,blank=True,null=True)

    class Meta:
        db_table = 'spiderconfig'

class TbUser(models.Model):
    u_id = models.AutoField(primary_key=True)
    u_name = models.CharField(max_length=50, blank=True, null=True)
    u_pwd = models.CharField(max_length=128, blank=True, null=True)
    u_telphone = models.CharField(max_length=30, blank=True, null=True)
    u_mail = models.CharField(max_length=30, blank=True, null=True)
    u_sex = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'tb_user'


class Tool(models.Model):
    toolid = models.CharField(db_column='toolID', primary_key=True, max_length=36)  # Field name made lowercase.
    toolname = models.CharField(db_column='toolName', max_length=36, blank=True, null=True)  # Field name made lowercase.
    version = models.CharField(max_length=36, blank=True, null=True)
    versiondescribe = models.CharField(db_column='versionDescribe', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    jarurl = models.CharField(db_column='jarUrl', max_length=255, blank=True, null=True)  # Field name made lowercase.
    toolkitid = models.ForeignKey('Toolkit', models.DO_NOTHING, db_column='toolkitID', blank=True, null=True)  # Field name made lowercase.
    state = models.CharField(max_length=26, blank=True, null=True)
    uploadtime = models.CharField(db_column='uploadTime', max_length=36, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tool'


class Toolkit(models.Model):
    toolkitid = models.CharField(db_column='toolkitID', primary_key=True, max_length=36)  # Field name made lowercase.
    toolkitname = models.CharField(db_column='toolkitName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    toolkitdescribe = models.CharField(db_column='toolkitDescribe', max_length=1000, blank=True, null=True)  # Field name made lowercase.
    userid = models.ForeignKey(Admin, models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'toolkit'


class Topic(models.Model):
    name = models.CharField(max_length=32)

    class Meta:
        managed = False
        db_table = 'topic'


class User(models.Model):
    userid = models.CharField(db_column='userID', primary_key=True, max_length=36)  # Field name made lowercase.
    username = models.CharField(db_column='userName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    password = models.CharField(max_length=64, blank=True, null=True)
    email = models.CharField(max_length=32, blank=True, null=True)
    roleid = models.ForeignKey(Role, models.DO_NOTHING, db_column='roleID', blank=True, null=True, related_name='userRoleId')  # Field name made lowercase.
    registrantid = models.CharField(db_column='registrantID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    usertype = models.CharField(db_column='userType', max_length=32, blank=True, null=True)  # Field name made lowercase.
    isauthenticated = models.CharField(db_column='isAuthenticated', max_length=2, blank=True, null=True)  # Field name made lowercase.
    address = models.CharField(max_length=255, blank=True, null=True)
    role = models.ForeignKey(Role, models.DO_NOTHING, db_column='role', blank=True, null=True, related_name='userRole')
    registranttime = models.CharField(db_column='registrantTime', max_length=255, blank=True, null=True)  # Field name made lowercase.
    photo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'


class UserOpera(models.Model):
    operaid = models.CharField(db_column='operaID', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    objectid = models.ForeignKey(Object, models.DO_NOTHING, db_column='objectID', blank=True, null=True)  # Field name made lowercase.
    operatype = models.CharField(db_column='operaType', max_length=36, blank=True, null=True)  # Field name made lowercase.
    operatime = models.CharField(db_column='operaTime', max_length=36, blank=True, null=True)  # Field name made lowercase.
    type = models.CharField(max_length=8, blank=True, null=True)
    articleid = models.ForeignKey(Article, models.DO_NOTHING, db_column='articleID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_opera'


class UserOperaComment(models.Model):
    useroperacommentid = models.CharField(db_column='userOperaCommentID', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    commentid = models.ForeignKey(Comment, models.DO_NOTHING, db_column='commentID', blank=True, null=True)  # Field name made lowercase.
    operatype = models.CharField(db_column='operaType', max_length=32, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_opera_comment'


class UserOperaStyle(models.Model):
    userstyleid = models.CharField(db_column='userStyleID', primary_key=True, max_length=36)  # Field name made lowercase.
    userid = models.ForeignKey(User, models.DO_NOTHING, db_column='userID', blank=True, null=True)  # Field name made lowercase.
    bulletinstyleid = models.ForeignKey(BulletinStyleId, models.DO_NOTHING, db_column='bulletinStyleID', blank=True, null=True)  # Field name made lowercase.
    operaid = models.CharField(db_column='operaID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    operatype = models.CharField(db_column='operaType', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user_opera_style'


class Website(models.Model):
    websiteid = models.CharField(db_column='websiteID', primary_key=True, max_length=36)  # Field name made lowercase.
    websitename = models.CharField(db_column='websiteName', max_length=64, blank=True, null=True)  # Field name made lowercase.
    websiteurl = models.CharField(db_column='websiteURL', max_length=64, blank=True, null=True)  # Field name made lowercase.
    containtableid = models.CharField(db_column='containTableID', max_length=36, blank=True, null=True)  # Field name made lowercase.
    websitetypeid = models.CharField(db_column='websiteTypeID', max_length=36, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'website'
