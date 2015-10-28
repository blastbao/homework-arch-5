#!/usr/bin/env python
#conding=utf-8


import MySQLdb

def return_db_handle():
    return MySQLdb.connect("localhost", "root", "123qwe", "mytest")

if __name__ == '__main__':
    db = return_db_handle()
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print "Database version: %s" % data
    db.close()
