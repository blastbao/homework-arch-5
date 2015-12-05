#!/usr/bin/env python
# coding=utf-8

import sys, os 
import MySQLdb as mysql
import json
import hashlib
import time
import conf

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNetFramework import nbNet

alarmStatus = {}
timeList = {}

def ff(d_in):
    """
    [['MemUsage', '>', 1900, 'alarm@qq.com',3], ['LoadAvg', '>', 1.0, 'pc@qq.com',3]]
    {"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
    """
    #print conf.ff_conf
    #print d_in
    serverTime = int(time.time())
    mon_data = json.loads(d_in)
    for rule in conf.ff_conf:
        monKey, operator, value, alarmRecv, num = rule
        monName = monKey + operator + str(value)
        alarmTrig =  alarmStatus.get(monName, 0)
        eval_function = str(mon_data[monKey]) + operator + str(value)
        ff_result = eval(eval_function)
        #print alarmTrig
        if ff_result:
            alarmStatus[monName] = alarmTrig + 1
            operator = '>='
            monTig = str(alarmStatus[monName]) + operator + str(num)
            #print monTig
            alarmStatus[monTig] = True
            #print alarmStatus[monTig]
            if monTig:
                print "Alarm", eval_function, alarmRecv
                
        else:
            if (alarmStatus.get(monName, False)):
                alarmStatus[monName] = False
                alarmStatus[monTig] -= 1
                print "Recover", eval_function, alarmRecv
                
if __name__ == '__main__':
    def logic(d_in):
        ff(d_in)
#        print d_in
        return("OK")

    ffD = nbNet('0.0.0.0', 9013, logic)
    ffD.run()
