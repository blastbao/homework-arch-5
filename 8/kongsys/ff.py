#!/usr/bin/env python
# coding=utf-8

import sys, os 
import MySQLdb as mysql
import json
import hashlib

import conf

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet.nbNetFramework import nbNet

alarmStatus = {}

def ff(d_in):
    """
    [['MemUsage', '>', 1900, 'alarm@qq.com'], ['LoadAvg', '>', 1.0, 'pc@qq.com']]
    {"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
    """
    #print conf.ff_conf
    #print d_in
    mon_data = json.loads(d_in)
    for rule in conf.ff_conf:
        rule_index = conf.ff_conf.index(rule)
        monKey, operator, value, alarmRecv, count = rule
        monName = monKey + operator + str(value)
        eval_function = str(mon_data[monKey]) + operator + str(value)
        ff_result = eval(eval_function)
        if ff_result:
            if conf.ff_conf[rule_index][-1] == 1:
                alarmStatus[monName] = True
                print "Alarm", eval_function, alarmRecv
            else:
                conf.ff_conf[rule_index][-1] = conf.ff_conf[rule_index][-1] - 1
                
        else:
            if (alarmStatus.get(monName, False)):
                conf.ff_conf[rule_index][-1] = 3
                alarmStatus[monName] = False
                print "Recover", eval_function, alarmRecv
                



if __name__ == '__main__':
    def logic(d_in):
        ff(d_in)
#        print d_in
        return("OK")

    ffD = nbNet('0.0.0.0', 50002, logic)
    ffD.run()


