#!/usr/bin/env python
# coding=utf-8

import sys, os
import MySQLdb as mysql
import json
import hashlib

import conf
from nbNet import nbNet

alarmStatus = {}
alarmNum = {}
def ff(d_in):
    mon_data = json.loads(d_in)
    for rule in conf.ff_conf:
        monKey, operator, value, alarmRecv, num = rule
        monName = monKey + operator + str(value)
        eval_function = str(mon_data[monKey]) + operator + str(value)
        ff_result = eval(eval_function)
        if ff_result:
            if monName in alarmNum:
                alarmNum[monName] += 1
            else:
                alarmNum[monName] = 1
            if alarmNum[monName] >= num:
                alarmStatus[monName] = True
                print "Alarm" , eval_function, alarmRecv, alarmNum[monName]
        else:
            if (alarmStatus.get(monName, False)):
                alarmStatus[monName] = False
                alarmNum[monName] = 0
                print "Recover", eval_function, alarmRecv
        print alarmStatus
if __name__ == '__main__':
    def logic(d_in):
        ff(d_in)
        return "ok"
    ffD = nbNet('0.0.0.0', 40000, logic)
    ffD.run()
