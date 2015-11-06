#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-23 11:14:50
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import MySQLdb
# 打开数据库
db = MySQLdb.Connect("localhost", "testuser", "test123", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行SQL语句
cursor.execute("SELECT VERSION()")

# 使用fetchone()方法获取一条数据库
data = cursor.fetchone()

print "Database version: %s " % data

# 关闭数据库
db.close()


# Output:
# Database version: 5.1.33-community
# [Finished in 0.5s]
