#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-23 15:34:35
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import MySQLdb
# 打开数据库
db = MySQLdb.Connect("localhost", "testuser", "test123", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 如果数据表已经存在，使用execute()方法删除
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL语句
sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME CHAR(20) NOT NULL,
         LAST_NAME CHAR(20),
         AGE INT,
         SEX CHAR(1),
         INCOME FLOAT )"""

cursor.execute(sql)
print "Database TESTDB's TABLE EMPLOYEE is created!"

# 关闭数据库
db.close()


# Output:
# Database TESTDB's TABLE EMPLOYEE is created!
# [Finished in 0.6s]
