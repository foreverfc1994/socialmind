import pymysql
from test import *
import jieba
import fool
from gensim import corpora,models,similarities
count = 0
db = pymysql.connect('192.168.100.103','root','root','ifeng',port=3306)
cur = db.cursor()
sql = 'select * from ifeng_news'
cur.execute(sql)
results = cur.fetchall()
entity = []
for result in results:
    count =count+1
    text = result[12]
    print(count)
    words, ners = fool.analysis(text)
    # print(ners[0])
    for i in ners[0]:
        entity.append((i[2],i[3]))
aa = set(entity)

db.close()
db1 = pymysql.connect('localhost','root','root','entity',port=3306)
cur1 = db1.cursor()
sql = 'insert into '
for a in aa:
    try:
       sql = 'insert into entity(name,type) values (\'%s\',\'%s\')'%(a[1],a[0])
       cur1.execute(sql)
       db1.commit()
       print('sucess')
    except:
        print('error')
    pass
db1.close()



db = pymysql.connect('192.168.100.103','root','root','ifeng',port=3306)
cur = db.cursor()
sql = 'select * from ifeng_news'
cur.execute(sql)
results = cur.fetchall()
entity = []
for result in results:
    text = result[12]
    articleid = result[0]
    words, ners = fool.analysis(text)
    # print(ners[0])
    for i in ners[0]:
        try:
            name = i[3]
            type = i[2]
            db11 = pymysql.connect('localhost', 'root', 'root', 'entity', port=3306)
            cur11 = db11.cursor()
            sql = 'select articlelist from entity where name=\'%s\' and type=\'%s\'' % (name, type)

            cur11.execute(sql)
            result = cur11.fetchall()

            try:
                list1 = result[0][0]
            except Exception as e:

                list1 = ''

            if list1:
                if list1.find(articleid) != -1:
                    pass
                else:
                    list1 = list1 + ',' + articleid
            else:
                list1 = articleid


            sql = 'update entity set articlelist = \'%s\' where name=\'%s\' and type=\'%s\'' % (
            str(list1).replace('\'', ''), name, type)
            print('update sucess')
            cur11.execute(sql)
            db11.commit()
            db11.close()
        except:
            print('update error')


db.close()
