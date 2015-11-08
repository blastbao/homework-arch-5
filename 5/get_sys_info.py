#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: thread_monitor_race.py
@time: 2015/11/8 18:55
"""
import json
import urllib
import inspect
import os,time,socket,datetime

userDefine_check_time = 0
useDefine_json = []

class mon:
    def __init__(self):
        self.data = {}

    def getLoadAvg(self):
        with open('/proc/loadavg') as  f:
            a = f.read().split()[:3];
            return  float(a[0])

    def getMemTotal(self):
        with open('/proc/meminfo') as f:
            a = int(f.readline().split()[1])
            return a/1024

    def getHost(self):
        '''
        模拟多台机器，所以使用伪随机函数
        '''
        #return  ['host1','host2','host3'][int(time.time()*1000.0)]
        return socket.gethostname()

    def getTime(self):
        return int(time.time())

    def runAllGet(self,fake_test=False):
        if not fake_test:
            for fun in inspect.getmembers(self,predicate=inspect.ismethod):
                if fun[0] == 'userDefineMon':
                    pass
                elif fun[0][:3] == 'get':
                    self.data[fun[0][3:]] = fun[1]()
            return self.data
        else:
            return datetime.datetime.now().microsecond;

if __name__ == "__main__":
    print mon().runAllGet()