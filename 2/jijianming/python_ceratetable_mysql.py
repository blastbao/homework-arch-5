#!/usr/bin/env python
#_*_coding:utf8_*_
import MySQLdb

db = MySQLdb.connect('127.0.0.1','testuser','test123','testdb')
cursor = db.cursor()
cursor.execute("drop table if exists reboot2")
sql = '''create table reboot2(
        first_name char(20) NOT NULL,
        last_name char(20),
        age int,
        sex char(1)
        )'''
cursor.execute(sql)
db.close()