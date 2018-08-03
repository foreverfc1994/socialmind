import pymysql

def dbconnect(dbname):
    db = pymysql.connect('192.168.100.103', 'root', 'root', dbname, port=3306)
    return db
    pass