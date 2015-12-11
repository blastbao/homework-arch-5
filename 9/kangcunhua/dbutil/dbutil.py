#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-12-06 14:19:45
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-12-06 14:20:19
import json
import time
import random
import datetime
import MySQLdb


class DB:
    conn = None
    db = None
    host = None

    def __init__(self, host, mysql_user, mysql_pass, mysql_db):
        self.host = host
        self.mysql_user = mysql_user
        self.mysql_pass = mysql_pass
        self.mysql_db = mysql_db

    def connect(self):
        self.conn = MySQLdb.connect(host=self.host, user=self.mysql_user, passwd=self.mysql_pass,
                                    db=self.mysql_db, charset="utf8", connect_timeout=600, compress=True)
        self.conn.autocommit(True)

    def execute(self, sql):
        try:
            cursor = self.conn.cursor()
            cursor.execute(sql)
        except (AttributeError, MySQLdb.OperationalError):
            try:
                cursor.close()
                self.conn.close()
            except:
                pass
            time.sleep(1)
            try:
                self.connect()
                print "reconnect DB"
                cursor = self.conn.cursor()
                cursor.execute(sql)
            except (AttributeError, MySQLdb.OperationalError):
                time.sleep(2)
                self.connect()
                print "reconnect DB"
                cursor = self.conn.cursor()
                cursor.execute(sql)

        return cursor
