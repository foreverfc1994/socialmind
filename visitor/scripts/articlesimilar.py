from jieba import analyse
import pymysql
import numpy as np
import jieba
from gensim import corpora,models,similarities
def jiebafenci(text):

    keys =[]
    for x, w in analyse.extract_tags(text, withWeight=True):
        keys.append(x)
        # print('%s %s' % (x, w))
    # keys = sorted(values.items(), key=lambda x: x[1], reverse=True)

    return keys if len(keys)<10 else keys[:10]
def dbinsert(id,keys):
    db = pymysql.connect('localhost','root','root','entity',port=3306)
    cur =db.cursor()
    sql = 'insert into similarAA(articleID,keywords) values (\'%s\',\'%s\')'%(id.replace('\'',''),str(keys).replace('\'',''))
    # print(sql)
    cur.execute(sql)
    db.commit()
    db.close()
def cut(sentence):
    generator = jieba.cut(sentence)
    return [word for word in generator]
def insertsimilar(id,similar):
    db = pymysql.connect('localhost', 'root', 'root', 'entity', port=3306)
    cur = db.cursor()
    sql ='update similarAA set similararticle=\'%s\' where articleID =\'%s\''%(str(similar).replace('\'', ''),id.replace('\'', ''))
    # sql = 'insert into similarAA(articleID,similararticle) values (\'%s\',\'%s\')' % (id.replace('\'', ''), str(similar).replace('\'', ''))
    print(sql)
    cur.execute(sql)
    db.commit()
    db.close()
def dbconnect():
    db = pymysql.connect('192.168.100.103','root','root','ifeng',port=3306)
    cur =db.cursor()
    sql = 'select * from ifeng_news'
    cur.execute(sql)
    results = cur.fetchall()
    count = 0
    i = 0
    texts = []
    indexs =0
    for result in results:
        text = result[12]
        texts.append(text)

    texts = [cut(text) for text in texts]
    dictionary = corpora.Dictionary(texts)
    feature_cnt = len(dictionary.token2id.keys())
    corpus = [dictionary.doc2bow(text) for text in texts]
    tfidf = models.TfidfModel(corpus)
    index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=feature_cnt)
    indexs =0
    for result in results:
        key = result[12]
        key_vector = dictionary.doc2bow(cut(key))
        sim = index[tfidf[key_vector]]
        aa = sorted(enumerate(sim), key=lambda item: -item[1])
        list = []
        while i < 10:
            i = i + 1
            list.append(aa[i][0])
        i = 0
        articles = []
        for l in list:
            articles.append(results[l][0])
        print('文章%s'%results[count][0]+'相似度最高的10篇文章是：'+str(articles))
        insertsimilar(results[count][0],articles)
        print('文章%s'%count+'相似度最高的10篇文章是：'+str(list))

        count = count + 1

    db.close()

dbconnect()