#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
sql = """INSERT INTO EMPLOYEE (
         FIRST_NAME, LAST_NAME, AGE,SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000)"""

try:
    data = cursor.execute(sql)
    # 提交到数据库执行
    db.commit()
except Exception, e:
    db.rollback()

finally:
    # 关闭数据库
    db.close()

if data:
    print 'insert successed!'
else:
    print "insert failed!"


# Output:
# Database TESTDB's TABLE EMPLOYEE is created!
# [Finished in 0.6s]
