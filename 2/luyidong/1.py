#!/usr/bin/env python
import MySQLdb
try:
	conn = MySQLdb.connect(host='127.0.0.1',user='reboot',passwd='reboot123',db='falcon')
	cur = conn.cursor()
	cur.execute('select * from stat_0')
	#result = cur.fetchall()
	#result = cur.fetchone()
	result = cur.fetchmany(3)
	
	for line in result:
		print line
	cur.close()
	conn.close()
except MySQLdb.Error,e:
	print 'Mysql Error Msg',e
