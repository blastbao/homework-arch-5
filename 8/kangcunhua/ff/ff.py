#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-11-30 13:31:12
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-11-30 13:32:41
import sys
import os
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
    # print conf.ff_conf
    # print d_in
    mon_data = json.loads(d_in)
    for rule in conf.ff_conf:
        monKey, operator, value, alarmRecv = rule
        monName = monKey + operator + str(value)
        eval_function = str(mon_data[monKey]) + operator + str(value)
        ff_result = eval(eval_function)
        if ff_result:
            alarmStatus[monName] = True
            print "Alarm", eval_function, alarmRecv
        else:
            if (alarmStatus.get(monName, False)):
                alarmStatus[monName] = False
                print "Recover", eval_function, alarmRecv


if __name__ == '__main__':
    def logic(d_in):
        ff(d_in)
#        print d_in
        return("OK")

    ffD = nbNet('0.0.0.0', 50002, logic)
    ffD.run()
