from __future__ import absolute_import
from __future__ import unicode_literals
import os
import uuid
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socialmind.settings")  # NoQA
from manager.scripts.dboperate import *
import django
django.setup()
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "socialmind.settings")  # NoQA
from visitor.models import Author,Website,Article
import time
def insertauthor():
    db = dbconnect('blog163')
    cur = db.cursor()
    sql = "select * from blog_163_author where category='人生杂谈'"
    cur.execute(sql)
    results = cur.fetchall()
    count = 1
    for result in results:
        try:
            newauthor = Author()
            newauthor.authorid = uuid.uuid4()
            newauthor.name = result[2]
            newauthor.realname = result[3]
            newauthor.sex = result[4]
            newauthor.birthday = result[5]
            newauthor.address = result[7]
            newauthor.introduction = result[8]
            newauthor.score = result[11]
            newauthor.career = result[17]
            newauthor.websiteid = Website.objects.get(websiteid='22')
            newauthor.save()
        except:
            print(count)
            count =count+1
    # result = results[1]
    # newauthor = Author()
    # newauthor.authorid = uuid.uuid4()
    # newauthor.name = result[2]
    # newauthor.realname = result[3]
    # newauthor.sex = result[4]
    # newauthor.birthday = result[5]
    # newauthor.address = result[7]
    # newauthor.introduction = result[8]
    # newauthor.score = result[11]
    # newauthor.career =result[17]
    # newauthor.websiteid = Website.objects.get(websiteid='22')
    # newauthor.save()
    db.close()
def insertarticle():
    db = dbconnect('blog163')
    cur = db.cursor()
    sql = "select * from blog_163_post"
    cur.execute(sql)
    results = cur.fetchall()
    # count = 0
    # for result in results:
    #     count = count+1
    #     # print(len(result))
    #     # newarticle = Article()
    #     # newarticle.articleid = uuid.uuid4()
    #     # newarticle.title = result[2]
    #     # newarticle.posttime = result[3]
    #     # newarticle.keywords = result[5]
    #     # newarticle.content = result[9]
    #     # newarticle.scannumber = result[13]
    #     # newarticle.commentnumber = result[14]
    #     # author = Author.objects.filter(name=str(result[6]))[0]
    #     # if author:
    #     #     newarticle.authorid = author
    #     # else:
    #     #     pass
    #     # newarticle.websiteid = Website.objects.get(websiteid='22')
    #     # newarticle.save()
    #     try:
    #         pass
    #
    #         newarticle = Article()
    #         newarticle.articleid = uuid.uuid4()
    #         newarticle.title = result[2]
    #         newarticle.posttime = result[3]
    #         newarticle.keywords = result[5]
    #         newarticle.content = result[9]
    #         newarticle.scannumber = result[13]
    #         newarticle.commentnumber = result[14]
    #         author = Author.objects.filter(name=str(result[6])).distinct()[1]
    #         if author:
    #             newarticle.authorid = author
    #         else:
    #             pass
    #         newarticle.websiteid = Website.objects.get(websiteid='22')
    #         newarticle.save()
    #
    #     except Exception as e:
    #         print(count,e)
    #         pass
    db.connect()

def selectarcticle():
    db = pymysql.connect('localhost', 'root', 'root', 'socialmind', port=3306)
    cur = db.cursor()
    sql = "select scanNumber from article"
    cur.execute(sql)
    results = cur.fetchall()
    print(len(results))
    db.close()
time_start = time.time()
# insertauthor()
selectarcticle()
# insertarticle()
# a = Article.objects.all()

time_end = time.time()
print(time_end-time_start)

