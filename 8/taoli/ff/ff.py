#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: ff.py
@time: 2015/11/29 18:34
"""
import sys
import os
import json
import time

import conf

sys.path.insert(1, os.path.join(sys.path[0], '..'))

alarmStatus = {}
threshold = 3


def ff(d_in):
    mon_data = json.loads(d_in)
    for rule in conf.ff_conf:
        monKey, operator, value, email = rule
        monName = monKey + operator + str(value)  #内容是具体的监控条件MemUsage>1863 这样的，然后做为字典的key
        eval_function = str(mon_data[monKey]) + operator + str(value)
        ff_result = eval(eval_function)
        res = alarmStatus.get(monName, 0)
        print monName
        if ff_result:
            alarmStatus[monName] = res + 1
            if (alarmStatus[monName] >= threshold):
                print 'Alarm: ', eval_function, email
        else:
            if res >= 1:
                alarmStatus[monName] -= 1
                print 'Recover', eval_function, email


if __name__ == '__main__':
    # def logic(d_in):
    #     ff(d_in)
    #     return ('OK')
    # ffd = nbNet('0.0.0.0',5002,logic)
    # ffd.run()
    while 1:
        print '1111'
        # fake = {"MemUsage": 1999}
        fake = '{"MemTotal": 15888, "MemUsage": 1999, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}'
        ff(fake)
        time.sleep(1)
