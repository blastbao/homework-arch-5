#!/usr/bin/env python
#conding=utf-8

from connect import return_db_handle

db = return_db_handle()

cursor = db.cursor()

sql = "UPDATE EMPLOYEE SET AGE = AGE + 1 \
                        WHERE SEX = '%c'" % ('M')

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()

