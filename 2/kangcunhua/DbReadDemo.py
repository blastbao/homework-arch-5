#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-23 17:32:40
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import MySQLdb
# 打开数据库
db = MySQLdb.Connect("localhost", "testuser", "test123", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()


# 创建插入的SQL语句
sql = "SELECT * FROM EMPLOYEE \
         WHERE  INCOME > '%d'" % (1000)

try:
    data = cursor.execute(sql)

    if data:
        print 'select successed!'
    else:
        print "select failed!"

    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        # 打印结果
        print "fname=%s,lname=%s,age=%d,sex=%s,income=%d" % \
              (fname, lname, age, sex, income)
except Exception, e:
    print "Error: unable to fetch data!", e
finally:
    # 关闭数据库
    db.close()


# Output:
# select successed!
# fname=Mac,lname=Mohan,age=20,sex=M,income=2000
# fname=Mac,lname=Mohan,age=20,sex=M,income=2000
# fname=Mac,lname=Mohan,age=20,sex=M,income=2000
# fname=Mac,lname=Mohan,age=20,sex=M,income=2000
# fname=Mac,lname=Mohan,age=20,sex=M,income=2000
# [Finished in 0.7s]
