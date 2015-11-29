#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-11-12 14:52:03
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-11-12 17:45:30
import Queue
import threading
import time
import json
import urllib2
import socket
import commands
import pdb  # 调试用

from MonItems import mon  # 这部分代码参见我们上面几章完成的监控项采集类

import sys
import os
# 把 .. 目录加入import 模块的默认搜索路径中
sys.path.insert(1, os.path.join(sys.path[0], '..'))

# agent 将会向上游的trans模块发送采集到的监控数据，这个是可以用的trans地址的list
trans_l = ['localhost:5000']

# 定义一个发送数据的伪类，实际发送的代码在后续课程完善；


class PorterThead(threading.Thread):
    """docstring for PorterThead"""

    def __init__(self, name,  q, q1=None, interval=None):
        # 初始化一些参数
        threading.Thread.__init__(self)
        self.name = name
        self.q = q  # 任务队列
        self.interval = interval
        # sendData_mh 采取的是长连接，这个list用来保存可用的连接
        self.sock_1 = [None]

    def run(self):
        # 开启collect线程或者是sendjson线程
        # 根据self.name来决定，collect进程负责采集本机的监控数据
        # 将数据放在任务队列中，sendjson线程负责从任务队列中取出监控数据
        # 并将数据通过socket发送给trans
        if self.name == 'collect':
            self.put_data()

        elif self.name == ('sendjson'):

            self.get_data()

    def put_data(self):
        m = mon()
        atime = int(time.time())
        while 1:

            # data = m.runAllGet(agentTest=True)  # 这里是我们上一章写好的函数
            data = m.runAllGet()  # 开启调试
            self.q.put(data)
            # 计算一下时间，保证采集是 self.interval秒一次的
            btime = int(time.time())
            time.sleep(self.interval - ((btime - atime) % self.interval))

    def get_data(self):
        while 1:
            print 'get'
            if not self.q.empty():
                data = self.q.get()
                print data
                # pdb.set_trace() # 调试用的pdb设置断点
                # 发送监控数据
                self.sendData(data)

            time.sleep(self.interval)

    def sendData(self, data=None):
        """docstring for SendData"""
        print 'send data:', str(data)


def startTh():
    # 初始化一个任务队列，队列长度为10，超过10个任务没有被消费，put操作将会阻塞
    q1 = Queue.Queue(10)
    ql1 = threading.Lock()

    collect = PorterThead('collect', q1, ql1, interval=3)
    # 开启采集线程
    collect.start()

    time.sleep(0.5)

    sendjson = PorterThead('sendjson', q1, ql1, interval=3)
    # 开启发送线程
    sendjson.start()

    # 将会在这里阻塞，直至两个线程退出
    collect.join()
    sendjson.join()

    print 'main Thread is over'

if __name__ == '__main__':
    startTh()
