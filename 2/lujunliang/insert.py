#!/usr/bin/env python
#coding=utf-8


from connect import return_db_handle

db = return_db_handle()
cursor = db.cursor()

sql = """INSERT INTO EMPLOYEE(
            FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)
            VALUES ('susan', 'li', 20, 'W', 3000)"""

try:
    cursor.execute(sql)
    db.commit()
except:
    db.rollback()
db.close()
