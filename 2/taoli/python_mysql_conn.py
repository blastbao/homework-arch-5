#!/usr/bin/env python
import MySQLdb
db=MySQLdb.connect("127.0.0.1","reboot","reboot123","taoli")
cursor=db.cursor()
cursor.execute("insert into user (name,age) values("taoli",888)")
cursor.execute("SELECT * FROM user where age <=30")
data=cursor.fetchone()
print data
db.close()