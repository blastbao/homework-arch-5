#!/usr/bin/env python

import MySQLdb
db=MySQLdb.connect("127.0.0.1","reboot123","reboot123","qidunhu")
cursor=db.cursor()
cursor.execute("SELECT * FROM user where age > 10")
data=cursor.fetchone()
print data
db.close()
