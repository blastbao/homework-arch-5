#!/usr/bin/env python
#coding:utf-8
import sys, os
import MySQLdb as mysql
import json
import hashlib
import conf
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet.nbNetFramework import nbNet
import time
alarmStatus = {}
countime  = {}

def ff(d_in):
    mon_data = d_in
    for rule in conf.ff_conf:
        monKey, operator, value, alarmRecv ,monCount = rule
        monName = monKey + operator + str(value)
        evel_function = str(mon_data[monKey]) + operator + str(value)
        ff_result = eval(evel_function)
        if ff_result:
            if alarmStatus.get(monName, 0) >= int(monCount) - 1: 
                print "Alarm", evel_function, alarmRecv
            else:
                alarmStatus[monName] = alarmStatus.get(monName, 0) + 1
                countime[monName] = time.time()
        else:
            if (alarmStatus.get(monName, 0)) and int(time.time()) - int(countime[monName]) >= 3 :
                alarmStatus[monName] = 0
                print "Recover", evel_function, alarmRecv
if __name__ =="__main__":
    def logic(d_in):
        ff(d_in)
        return "ok"
    logic({"test":"30"})
    logic({"test":"10"})
    logic({"test":"30"})
    logic({"test":"30"})
    #ffD = nbNet('0.0.0.0', 30001, logic)
    #ffD.run
