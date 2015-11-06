#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Summary

description:
    实例，
    以下代码使用变量向SQL语句传递参数：
    user_id = "test123"
    password = "password"
    con.execute('insert into Login values ("%s","%s") % \ (user_id,password))
"""
# @Date    : 2015-10-23 16:27:42
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import MySQLdb
# 打开数据库
db = MySQLdb.Connect("localhost", "testuser", "test123", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()


# 创建插入的SQL语句
sql = "INSERT INTO EMPLOYEE ( \
         FIRST_NAME, LAST_NAME, AGE,SEX, INCOME) \
         VALUES ('%s','%s','%d','%c','%d')" % \
    ('Mac', 'Mohan', 20, 'M', 2000)

try:
    data = cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
    if data:
        print 'insert successed!'
    else:
        print "insert failed!"
except Exception, e:
    db.rollback()
    print "insert failed，db rollback!", e
finally:
    # 关闭数据库
    db.close()


# Output:
# insert successed!
# [Finished in 0.9s]
