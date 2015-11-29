#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-11-13 12:01:18
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-11-22 13:39:06
'''
    第五次课作业：
    将MonAgent.py的client改成支持多个work thread，实现多线程同时work，互相分担任务。
    起多个collect，然后还需要协调这几个collect 让他们继续3秒选出一个collect跑一次。
    ====================================>
    PC老师<auxtenwpc@gmail.com> 15:12:12 
    大家加油把作业做了，第一次动手写多线程协作的程序 会有点费脑子。PC老师当年没人指导自己一个坑一个坑爬出来的，大家把作业做了才能真正的掌握
    雪糕(1060987407) 15:12:41 
    这个可是以后混的一个利器
    PC老师<auxtenwpc@gmail.com> 15:15:41 
    不要到时候出去面试 别人问到了再后悔当时没花一小时看看
'''
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
'''
    为了调试方便，改造了MonItems.py runAllGet方法
    在 CollectThead 类的 put_data方法中
    # 打开调试
    data = m.runAllGet(agentTest=True)
    # 关闭调试
    data = m.runAllGet() 
'''
# 把 .. 目录加入import 模块的默认搜索路径中
sys.path.insert(1, os.path.join(sys.path[0], '..'))

# agent 将会向上游的trans模块发送采集到的监控数据，这个是可以用的trans地址的list
trans_l = ['localhost:5000']

# 定义一个发送数据的伪类，实际发送的代码在后续课程完善；


class PorterThead(threading.Thread):
    """docstring for PorterThead"""

    def __init__(self, name,  q, ql=None, interval=None):
        # 初始化一些参数
        threading.Thread.__init__(self)
        self.name = name
        self.q = q  # 任务队列
        self.interval = interval
        # sendData_mh 采取的是长连接，这个list用来保存可用的连接
        self.sock_1 = [None]

    def run(self):
        # 开启sendjson线程，sendjson线程负责从任务队列中取出监控数据
        # 并将数据通过socket发送给trans

        print '      =====发送线程' + self.name + 'start'

        self.get_data()

    def get_data(self):
        while 1:
            if not self.q.empty():
                print '      =====get:Queue size :' + str(self.q.qsize())
                data = self.q.get()
                print '      =====get:' + self.name + str(data)
                # pdb.set_trace() # 调试用的pdb设置断点
                # 发送监控数据
                self.sendData_mh(data)
                print '      =====发送线程' + self.name + ' send data over!'
            else:
                print '      =====发送线程' + self.name + ' wait for data!'
            time.sleep(self.interval)

    def sendData_mh(self, data=None):
        """docstring for sendData_mh"""
        pass


class CollectThead(threading.Thread):
    """docstring for PorterThead"""

    def __init__(self, name,  q, ql=None, interval=None):
        # 初始化一些参数
        threading.Thread.__init__(self)
        self.name = name
        self.q = q  # 任务队列
        self.ql = ql  # 线程锁
        self.interval = interval
        # sendData_mh 采取的是长连接，这个list用来保存可用的连接
        self.sock_1 = [None]
        # 发令队列，每$interval秒放进一个令牌，队列长度1
        self.starter = Queue.Queue(1)

    def setStarter(self):
        time.sleep(self.interval)
        self.starter.put(1)

    def run(self):
        # 开启collect线程，collect进程负责采集本机的监控数据
        self.put_data()

    def put_data(self):
        m = mon()
        atime = int(time.time())
        while 1:
            print '采集线程 ' + self.name + ' try to get lock!'
            if not self.starter.empty():
                取得令牌
                self.starter.get()
                data = m.runAllGet(agentTest=True)  # 打开调试
                # data = m.runAllGet()  # 关闭调试
                self.q.put(data)
                # 计算一下时间，保证采集是 self.interval秒一次的
                print '采集线程 ' + self.name + str(data)
                print '队列大小：' + str(self.q.qsize())

                btime = int(time.time())
                time.sleep(self.interval -
                           ((btime - atime) % self.interval))
                print '采集线程 ' + self.name + ' collect data over!'

                self.ql.release()

            else:
                print '采集线程 ' + self.name + ' 等待令牌!'
            if self.q.full():
                print '采集线程 ' + self.name + ' wait for Queue!'


def startTh():
    # 初始化一个任务队列，队列长度为6，超过6个任务没有被消费，put操作将会阻塞
    q1 = Queue.Queue(6)
    ql1 = threading.Lock()

    # 初始化一个最大的子线程数
    maxSubThread = 3

    for i in xrange(maxSubThread):
        collect = CollectThead('collect' + str(i), q1, ql1, interval=3)
        collect.start()

    time.sleep(0.5)

    sendjson = PorterThead('sendjson0', q1, interval=8)
    # 开启发送线程
    sendjson.start()
    q1.join()
    # 将会在这里阻塞

    # collect.join()
    # sendjson.join()

    print 'main Thread is over'

if __name__ == '__main__':
    startTh()
# output： if collect interval = 3 && sendjson interval = 1
# 采集线程collect0 try to get lock!
# 采集线程collect0{'fun': 1447393347.074}
# 采集线程collect1 try to get lock!
# 采集线程collect2 try to get lock!
#       =====发送线程sendjson0start
#       =====get:sendjson0{'fun': 1447393347.074}
#       =====发送线程sendjson0 send data over!
#       =====发送线程sendjson0 wait for data!
#       =====发送线程sendjson0 wait for data!
# 采集线程collect1{'fun': 1447393350.074}
# 采集线程collect0collect data over!

#       =====get:sendjson0{'fun': 1447393350.074}
#       =====发送线程sendjson0 send data over!
#       =====发送线程sendjson0 wait for data!
#       =====发送线程sendjson0 wait for data!
# 采集线程collect2{'fun': 1447393353.074}
# 采集线程collect1collect data over!

#       =====get:sendjson0{'fun': 1447393353.074}
#       =====发送线程sendjson0 send data over!
#       =====发送线程sendjson0 wait for data!
#       =====发送线程sendjson0 wait for data!

# output： if collect interval = 1 && sendjson interval = 10
# 采集线程collect0 try to get lock!
# 采集线程collect0{'fun': 1447399740.436}
# 队列大小：1
# 采集线程collect1 try to get lock!
# 采集线程collect2 try to get lock!
#       =====发送线程sendjson0start
#       =====get:Queue size :1
#       =====get:sendjson0{'fun': 1447399740.436}
#       =====发送线程sendjson0 send data over!
# 采集线程collect0 collect data over!
# 采集线程collect1{'fun': 1447399741.436}
# 队列大小：1
# 采集线程collect0 try to get lock!
# 采集线程collect1 collect data over!
# 采集线程collect1 try to get lock!
# 采集线程collect2{'fun': 1447399742.436}
# 队列大小：2
# 采集线程collect2 collect data over!
# 采集线程collect0{'fun': 1447399743.436}
# 队列大小：3
# 采集线程collect2 try to get lock!
# 采集线程collect0 collect data over!
# 采集线程collect1{'fun': 1447399744.436}
# 队列大小：4
# 采集线程collect0 try to get lock!
# 采集线程collect1 collect data over!
# 采集线程collect1 try to get lock!
# 采集线程collect2{'fun': 1447399745.436}
# 队列大小：5
# 采集线程collect2 collect data over!
# 采集线程collect0{'fun': 1447399746.436}
# 队列大小：6
# 采集线程collect2 wait for Queue!
# 采集线程collect2 try to get lock!
# 采集线程collect0 collect data over!
# 采集线程collect0 wait for Queue!
# 采集线程collect0 try to get lock!
#       =====get:Queue size :6
# 采集线程collect1{'fun': 1447399747.437}
# 队列大小：6
#       =====get:sendjson0{'fun': 1447399747.437}
#       =====发送线程sendjson0 send data over!
# 采集线程collect1 collect data over!
# 采集线程collect1 wait for Queue!
# 采集线程collect1 try to get lock!

# output: 在centos上运行，关闭调试开关：
# >>study:/home/kang/arch-5/lession05>python MonAgentMultiCollecter.py
# 采集线程 collect0 try to get lock!
# 采集线程 collect1 try to get lock!
# 采集线程 collect2 try to get lock!
# 采集线程 collect0{'MemTotal': 15888, 'MemUseage': 2869, 'MemFree': 13018, 'Host': 'host3', 'LoadAvg': 0.0, 'Time': 1447402241}
# 队列大小：1
#       =====发送线程sendjson0start
#       =====get:Queue size :1
#       =====get:sendjson0{'MemTotal': 15888, 'MemUseage': 2869, 'MemFree': 13018, 'Host': 'host3', 'LoadAvg': 0.0, 'Time': 1447402241}
#       =====发送线程sendjson0 send data over!
# 采集线程 collect0 collect data over!
# 采集线程 collect0 try to get lock!
# 采集线程 collect0{'MemTotal': 15888, 'MemUseage': 2870, 'MemFree': 13017, 'Host': 'host5', 'LoadAvg': 0.0, 'Time': 1447402244}
# 队列大小：1
# 采集线程 collect0 collect data over!
# 采集线程 collect0 try to get lock!
# 采集线程 collect0{'MemTotal': 15888, 'MemUseage': 2870, 'MemFree': 13017, 'Host': 'host3', 'LoadAvg': 0.0, 'Time': 1447402247}
# 队列大小：2
#       =====get:Queue size :2
#       =====get:sendjson0{'MemTotal': 15888, 'MemUseage': 2870, 'MemFree': 13017, 'Host': 'host3', 'LoadAvg': 0.0, 'Time': 1447402247}
#       =====发送线程sendjson0 send data over!
# 采集线程 collect0 collect data over!
# 采集线程 collect0 try to get lock!
# 采集线程 collect0{'MemTotal': 15888, 'MemUseage': 2869, 'MemFree': 13018, 'Host': 'host2', 'LoadAvg': 0.0, 'Time': 1447402250}
# 队列大小：2
# 采集线程 collect0 collect data over!
# 采集线程 collect0 try to get lock!
# 采集线程 collect2{'MemTotal': 15888, 'MemUseage': 2869, 'MemFree': 13018, 'Host': 'host5', 'LoadAvg': 0.0, 'Time': 1447402253}
# 队列大小：3
# 采集线程 collect2 collect data over!
# 采集线程 collect2 try to get lock!
# 采集线程 collect2{'MemTotal': 15888, 'MemUseage': 2869, 'MemFree': 13018, 'Host': 'host4', 'LoadAvg': 0.08, 'Time': 1447402256}
# 队列大小：4
#       =====get:Queue size :4
#       =====get:sendjson0{'MemTotal': 15888, 'MemUseage': 2869, 'MemFree': 13018, 'Host': 'host2', 'LoadAvg': 0.0, 'Time': 1447402250}
#       =====发送线程sendjson0 send data over!
# 采集线程 collect2 collect data over!
# 采集线程 collect2 try to get lock!
# 采集线程 collect2{'MemTotal': 15888, 'MemUseage': 2869, 'MemFree': 13018, 'Host': 'host2', 'LoadAvg': 0.08, 'Time': 1447402259}
# 队列大小：4
# 采集线程 collect2 collect data over!
# 采集线程 collect2 try to get lock!
# 采集线程 collect2{'MemTotal': 15888, 'MemUseage': 2869, 'MemFree': 13018, 'Host': 'host1', 'LoadAvg': 0.07, 'Time': 1447402262}
# 队列大小：5
# 采集线程 collect2 collect data over!
# 采集线程 collect2 try to get lock!
# 采集线程 collect2{'MemTotal': 15888, 'MemUseage': 2869, 'MemFree': 13018, 'Host': 'host4', 'LoadAvg': 0.07, 'Time': 1447402265}
# 队列大小：6
#       =====get:Queue size :6
#       =====get:sendjson0{'MemTotal': 15888, 'MemUseage': 2869, 'MemFree': 13018, 'Host': 'host2', 'LoadAvg': 0.0, 'Time': 1447402250}
#       =====发送线程sendjson0 send data over!
# 采集线程 collect2 collect data over!
# 采集线程 collect2 try to get lock!
# 采集线程 collect2{'MemTotal': 15888, 'MemUseage': 2869, 'MemFree': 13018, 'Host': 'host3', 'LoadAvg': 0.07, 'Time': 1447402268}
# 队列大小：6
# 采集线程 collect2 collect data over!
# 采集线程 collect2 wait for Queue!
# 采集线程 collect2 try to get lock!
#       =====get:Queue size :6
#       =====get:sendjson0{'MemTotal': 15888, 'MemUseage': 2869, 'MemFree': 13018, 'Host': 'host2', 'LoadAvg': 0.06, 'Time': 1447402271}
#       =====发送线程sendjson0 send data over!
#  采集线程 collect2{'MemTotal': 15888, 'MemUseage': 2869, 'MemFree': 13018, 'Host': 'host2', 'LoadAvg': 0.06, 'Time': 1447402271}
# 队列大小：6
# 采集线程 collect2 collect data over!
# 采集线程 collect2 wait for Queue!
# 采集线程 collect2 try to get lock!
#       =====get:Queue size :6
#       =====get:sendjson0{'MemTotal': 15888, 'MemUseage': 2870, 'MemFree': 13017, 'Host': 'host3', 'LoadAvg': 0.06, 'Time': 1447402274}
#       =====发送线程sendjson0 send data over!
# 采集线程 collect2{'MemTotal': 15888, 'MemUseage': 2870, 'MemFree': 13017, 'Host': 'host3', 'LoadAvg': 0.06, 'Time': 1447402274}
# 队列大小：6
# 采集线程 collect2 collect data over!
# 采集线程 collect2 wait for Queue!
# 采集线程 collect2 try to get lock!
# ^\Quit (core dumped)
