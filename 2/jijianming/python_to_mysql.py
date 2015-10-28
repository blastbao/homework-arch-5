#!/usr/bin/env python
#_*_coding:utf8_*_
import MySQLdb

db = MySQLdb.connect('127.0.0.1','testuser','test123','testdb')#链接数据库
cursor = db.cursor()#获取游标
cursor.execute('select * from employee where sex=1')#执行查询语句
data = cursor.fetchone()#获取结果
print  data
db.close()