#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-11-29 17:17:54
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-11-30 19:04:56
import sys
import os
import MySQLdb as mysql
import json
import hashlib

import conf

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet import nbNet
"""
    作业：改造ff.py,要求累计三次才报警
    已知问题：无差别累计三次报警。或许需要改造成按类别各累计三次才报警；
    update:抽象改造成类，规避强制global声明作用范围；
"""


class Funfilter(object):
    """docstring for Funfilter"""

    def __init__(self):
        super(Funfilter, self).__init__()

        self.alarmStatus = {}
        self.alarmTotal = 0

    def ff(self, d_in):
        """
        [['MemUsage', '>', 1900, 'alarm@qq.com'], ['LoadAvg', '>', 1.0, 'pc@qq.com']]
        {"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083,"Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
        发送：
        00115{"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
        00115{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
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

                self.alarmTotal += 1
                print 'alarmTotal = ', self.alarmTotal
                if self.alarmTotal >= 3:
                    self.alarmStatus[monName] = True
                    print "Alarm", eval_function, alarmRecv
            else:
                print 'alarmTotal = ', self.alarmTotal
                if (self.alarmStatus.get(monName, False)):
                    self.alarmStatus[monName] = False
                    self.alarmTotal = 0
                    print "Recover", eval_function, alarmRecv


if __name__ == '__main__':
    myff = Funfilter()

    def logic(d_in):
        myff.ff(d_in)
        print d_in
        return("OK")

    ffD = nbNet('0.0.0.0', 50002, logic)
    ffD.run()


# 正常：不报警的数据发送
# >>study:/home/kang>telnet 127.0.0.1 50002
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# 00115{"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
# 00002OK

# 报警：启动三个SSH，连发三次超阀值数据
# >>study:/home/kang/arch-5/lession08>telnet 127.0.0.1 50002
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# 00115{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
# 00002OK

# >>study:/home/kang/arch-5/lession08/ff_homework>python ff_total3_2alarm.py
# alarmTotal =  1
# alarmTotal =  1
# {"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
# alarmTotal =  2
# alarmTotal =  2
# {"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
# alarmTotal =  3
# Alarm 1904>1863 alarm@qq.com
# alarmTotal =  3
# {"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
