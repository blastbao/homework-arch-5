#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-11-30 18:53:31
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-12-06 10:57:18
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
    update:成功实现：
    1.累计M次才报警；
    2.单位时间内报警次数小于N
    3.M，N可在参数文件conf.py中配置
"""


class Funfilter(object):
    """docstring for Funfilter"""

    def __init__(self):
        super(Funfilter, self).__init__()

        self.alarmStatus = {}
        # self.alarmTotal = 0
        for rule in conf.ff_conf:
            monKey, operator, value, alarmRecv, alarmNum, maxAlarmNumPerinterval, interval = rule
            monName = monKey + operator + str(value)
            # 描述：{'监控条件':[触发报警次数,触发阀值几次,第一次报警时间,距离第一次报警时间（单位：秒）]}
            self.alarmStatus[monName] = [0, 0, 0, 0]
        print '========init:', self.alarmStatus

    def ff(self, d_in):
        """
        描述：[监控项,操作符,阀值,邮件,累计N次就报警，间隔时间内最多报警M次, 间隔时间]
        配置：[['MemUsage', '>', 1863, 'alarm@qq.com', 3, 3, 60], ['LoadAvg', '>', 0.2, 'pc@qq.com', 1, 2, 20]]

        正常1：00115{"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
        异常1：00115{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246805}
        异常2：00115{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246815}
        异常3：00115{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246825}
        异常4：00115{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246835}
        异常5：00115{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246875}
        正常2：00115{"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246885}
        描述：{'监控条件':[触发报警次数,触发阀值几次,第一次报警时间,距离第一次报警时间（单位：秒）]}
        alarmStatus={'wd':[0,3,1434246795,60],'pc':[0,5,1434246795,300],'woniu':[0,2,1434246795,10]}
        """

        # print conf.ff_conf
        # print d_in
        mon_data = json.loads(d_in)

        for rule in conf.ff_conf:
            monKey, operator, value, alarmRecv, alarmNum, maxAlarmNum, interval = rule
            monName = monKey + operator + str(value)
            eval_function = str(mon_data[monKey]) + operator + str(value)
            ff_result = eval(eval_function)

            print '========befor alarm:', self.alarmStatus
            if ff_result:  # 如果触发 阀值

                if self.alarmStatus[monName][1] == 0:  # 第一次触发
                    self.alarmStatus[monName][
                        2] = mon_data['Time']  # 记录触发时间
                else:
                    self.alarmStatus[monName][3] = mon_data[
                        'Time'] - self.alarmStatus[monName][2]  # 第二次起，计算距离上一次触发过了多少秒
                self.alarmStatus[monName][1] += 1  # 触发次数+1

                # 触发次数大于 配置的单位阀值 而且 触发间隔小于 配置的单位时间 而且 单位时间内触发报警次数小于 配置，报警
                if self.alarmStatus[monName][1] >= alarmNum and self.alarmStatus[monName][3] < interval and self.alarmStatus[monName][0] <= maxAlarmNum:
                    self.alarmStatus[monName][0] += 1  # 记录触发报警次数
                    print "!!!Alarm", eval_function, alarmRecv
                else:
                    print '========未达到报警条件:', self.alarmStatus
                    print '========? interval and self.alarmStatus[monName][1] <= maxAlarmNum:', self.alarmStatus[monName][1], 'VS', maxAlarmNum
                # 如果超出单位间隔时间，重置触发报警次数为1，累计触发阀值为1，初始化当前 数据时间为第一次报警时间，初始化距离上次报警时间为0
                if self.alarmStatus[monName][3] > interval:
                    self.alarmStatus[monName] = [1, 1, mon_data['Time'], 0]
                    print '========超出单位间隔时间：重置报警状态', self.alarmStatus[monName][0], 'VS', maxAlarmNum
            elif (self.alarmStatus.get(monName, [0, 0, 0, 0]) and self.alarmStatus[monName][0] >= 1):
                self.alarmStatus[monName] = [0, 0, 0, 0]
                print "!!!Recover", eval_function, alarmRecv
            print '========after alarm:', self.alarmStatus


if __name__ == '__main__':
    myff = Funfilter()

    def logic(d_in):
        myff.ff(d_in)
        print '========input:', d_in
        return("OK")

    ffD = nbNet('0.0.0.0', 50002, logic)
    ffD.run()

# 输入正常监控数据，查看处理结果不报警
# >>study:/home/kang/arch-5/lession08>telnet 127.0.0.1 50002
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# 00115{"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
# 00002OK

# 输入第1次异常数据，不触发报警
# >>study:/home/kang>telnet 127.0.0.1 50002
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# 00115{"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
# 00002OK

# 输入第2次异常数据，不触发报警
# >>study:/home/kang>telnet 127.0.0.1 50002
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# 00115{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246815}
# 00002OK

# 输入第3次异常数据，触发报警
# >>study:/home/kang>telnet 127.0.0.1 50002
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# 00115{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246825}
# 00002OK

# 输入第4次异常数据，超过单位时间报警次数，不再报警
# >>study:/home/kang>telnet 127.0.0.1 50002
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# 00115{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246835}
# 00002OK

# 输入第5次异常数据，超过单位时间，重置报警状态
# >>study:/home/kang>telnet 127.0.0.1 50002
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# 00115{"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246875}
# 00002OK


# 再次输入正常监控数据，查看处理结果已恢复正常Recover
# >>study:/home/kang/arch-5/lession08>telnet 127.0.0.1 50002
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# 00115{"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246885}
# 00002OK


# >>study:/home/kang/arch-5/lession08/ff_homework>python ff_total3_2alarm_v3.py
# ========init: {'MemUsage>1863': [False, 0, 0, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========befor alarm: {'MemUsage>1863': [False, 0, 0, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========after alarm: {'MemUsage>1863': [False, 0, 0, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========befor alarm: {'MemUsage>1863': [False, 0, 0, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========after alarm: {'MemUsage>1863': [False, 0, 0, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========input: {"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246795}
# ========befor alarm: {'MemUsage>1863': [False, 0, 0, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========未达到报警条件: {'MemUsage>1863': [False, 1, 1434246805, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========? interval and self.alarmStatus[monName][1] <= maxAlarmNum: 1 VS 3
# ========after alarm: {'MemUsage>1863': [False, 1, 1434246805, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========befor alarm: {'MemUsage>1863': [False, 1, 1434246805, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========after alarm: {'MemUsage>1863': [False, 1, 1434246805, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========input: {"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246805}
# ========befor alarm: {'MemUsage>1863': [False, 1, 1434246805, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========未达到报警条件: {'MemUsage>1863': [False, 2, 1434246805, 10], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========? interval and self.alarmStatus[monName][1] <= maxAlarmNum: 2 VS 3
# ========after alarm: {'MemUsage>1863': [False, 2, 1434246805, 10], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========befor alarm: {'MemUsage>1863': [False, 2, 1434246805, 10], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========after alarm: {'MemUsage>1863': [False, 2, 1434246805, 10], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========input: {"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246815}
# ========befor alarm: {'MemUsage>1863': [False, 2, 1434246805, 10], 'LoadAvg>0.2': [False, 0, 0, 0]}
# !!!Alarm 1904>1863 alarm@qq.com
# ========after alarm: {'MemUsage>1863': [True, 3, 1434246805, 20], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========befor alarm: {'MemUsage>1863': [True, 3, 1434246805, 20], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========after alarm: {'MemUsage>1863': [True, 3, 1434246805, 20], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========input: {"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246825}
# ========befor alarm: {'MemUsage>1863': [True, 3, 1434246805, 20], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========未达到报警条件: {'MemUsage>1863': [True, 4, 1434246805, 30], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========? interval and self.alarmStatus[monName][1] <= maxAlarmNum: 4 VS 3
# ========after alarm: {'MemUsage>1863': [True, 4, 1434246805, 30], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========befor alarm: {'MemUsage>1863': [True, 4, 1434246805, 30], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========after alarm: {'MemUsage>1863': [True, 4, 1434246805, 30], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========input: {"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246835}
# ========befor alarm: {'MemUsage>1863': [True, 5, 1434246805, 30], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========未达到报警条件: {'MemUsage>1863': [True, 6, 1434246805, 70], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========? interval and self.alarmStatus[monName][1] <= maxAlarmNum: 6 VS 3
# ========超出单位间隔时间：重置报警状态 1 VS 3
# ========after alarm: {'MemUsage>1863': [False, 1, 1434246875, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========befor alarm: {'MemUsage>1863': [False, 1, 1434246875, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========after alarm: {'MemUsage>1863': [False, 1, 1434246875, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========input: {"MemTotal": 15888, "MemUsage": 1904, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246875}
# ========befor alarm: {'MemUsage>1863': [False, 1, 1434246875, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# !!!Recover 1804>1863 alarm@qq.com
# ========after alarm: {'MemUsage>1863': [False, 0, 0, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========befor alarm: {'MemUsage>1863': [False, 0, 0, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========after alarm: {'MemUsage>1863': [False, 0, 0, 0], 'LoadAvg>0.2': [False, 0, 0, 0]}
# ========input: {"MemTotal": 15888, "MemUsage": 1804, "MemFree": 14083, "Host": "teach.works", "LoadAvg": 0.15, "Time": 1434246885}
