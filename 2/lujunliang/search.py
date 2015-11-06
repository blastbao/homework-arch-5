#!/usr/bin/env python
#coding=utf-8

from connect import return_db_handle

db = return_db_handle()
cursor = db.cursor()

sql = "SELECT * FROM EMPLOYEE WHERE INCOME > '%d'" % (1000)

try:
    cursor.execute(sql)
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print "fname:%s, lname:%s, age:%s, sex:%s, income:%s" % \
                (fname, lname, age, sex, income)

except:
    print "Error:unable to fetch data"
db.close()
