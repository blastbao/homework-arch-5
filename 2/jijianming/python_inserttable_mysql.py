#!/usr/bin/env python
#_*_coding:utf8_*_
import MySQLdb

db = MySQLdb.connect('127.0.0.1','testuser','test123','testdb')
cursor = db.cursor()
sql="insert into reboot2(first_name,last_name,age,sex) values('mac','mohan',20,1)"
try:
    cursor.execute(sql)
    db.commit()#插入数据后要提交下。
except:
    db.rollback()#如果失败的话就回退。

db.close()