#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-23 17:51:36
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import MySQLdb
# 打开数据库
db = MySQLdb.Connect("localhost", "testuser", "test123", "TESTDB")

# 使用cursor()方法获取操作游标
cursor = db.cursor()


# 创建插入的SQL语句
sql = "UPDATE EMPLOYEE SET AGE = AGE +1 \
         WHERE  SEX = '%c'" % ('M')

try:
    data = cursor.execute(sql)

    # 提交到数据库执行
    db.commit()

    if data:
        print 'update successed!'
    else:
        print "update failed!"


except Exception, e:
    db.rollback()
    print "update failed，db rollback!", e
finally:
    # 关闭数据库
    db.close()


# Output:
# update successed!
# [Finished in 0.6s]


# 同步登录MySQL验证：
# Microsoft Windows [版本 6.1.7600]
# 版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

# C:\Users\Kang.Cunhua>mysql -uroot
# Welcome to the MySQL monitor.  Commands end with ; or \g.
# Your MySQL connection id is 19
# Server version: 5.1.33-community MySQL Community Server (GPL)

# Type 'help;' or '\h' for help. Type '\c' to clear the buffer.

# mysql> use testdb
# Database changed
# mysql> show tables;
# +------------------+
# | Tables_in_testdb |
# +------------------+
# | employee         |
# +------------------+
# 1 row in set (0.00 sec)

# mysql> select * from employee;
# +------------+-----------+------+------+--------+
# | FIRST_NAME | LAST_NAME | AGE  | SEX  | INCOME |
# +------------+-----------+------+------+--------+
# | Mac        | Mohan     |   20 | M    |   2000 |
# | Mac        | Mohan     |   20 | M    |   2000 |
# | Mac        | Mohan     |   20 | M    |   2000 |
# | Mac        | Mohan     |   20 | M    |   2000 |
# | Mac        | Mohan     |   20 | M    |   2000 |
# +------------+-----------+------+------+--------+
# 5 rows in set (0.00 sec)

# mysql> select * from employee;
# +------------+-----------+------+------+--------+
# | FIRST_NAME | LAST_NAME | AGE  | SEX  | INCOME |
# +------------+-----------+------+------+--------+
# | Mac        | Mohan     |   21 | M    |   2000 |
# | Mac        | Mohan     |   21 | M    |   2000 |
# | Mac        | Mohan     |   21 | M    |   2000 |
# | Mac        | Mohan     |   21 | M    |   2000 |
# | Mac        | Mohan     |   21 | M    |   2000 |
# +------------+-----------+------+------+--------+
# 5 rows in set (0.00 sec)
