#!/usr/bin/env python
#coding=utf-8

import Queue
import threading
import time
import json 
import urllib2
import socket
import commands
import pdb 
from moniItems import mon 

import sys,os

#把'..'目录加入import模块的默认搜索路径中
sys.path.insert(1,os.path.join(sys.path[0],'..'))
#import 发送数据的函数
#from simpleNet.nbNetFramework import senddata_mh

#agent 将会向上游的trans模块发送采集到的监控数据,这个是可以用的trans 地址是list
trans_list01=['localhost:50000']

class porterThread(threading.Thread):
    def __init__(self,name,q,que_lock=None,interval=None):
        """init data """
        threading.Thread.__init__(self)
        self.name=name 
        self.q=q 
        self.interval=interval
        self.sock_l=[None]
    
    def run(self):
        """name to function 
        collect local monotor data and put data in queue.
        sendjson get data from queque and send to trans by socket.
        """
        print self.name
        if self.name == 'collect':
            self.put_data()
        elif self.name == 'sendjson':
            self.get_data()
    
    def put_data(self):
        """ main function of collect data"""
        m=mon()
        atime=int(time.time())
        while 1 :
            #data=m.runAllGet()
            data="memory:16G"
            self.q.put(data)
            #处理时间间隔的频率问题
            btime=int(time.time())
            print "get monitor data %s " %(data)
            time.sleep(self.interval-( (btime-atime)%self.interval ))
    
    
    def get_data(self):
        while 1:
            #print "get"
            if not self.q.empty():
                data=self.q.get()
                print "send data ... %s " %(data) 
                #debug 
                #pdb.set_trace()
                
                #send monitor data 
                #sendData_mh()
                
            time.sleep(self.interval)
    
def startTh():
    #init 10 queue ,超过10个队列没有被消费,put操作会阻塞
    que=Queue.Queue(10)
    que_lock=threading.Lock()
    collect=porterThread('collect',que,que_lock,interval=3)
    #start collected thread 
    collect.start()
    
    time.sleep(0.5)
    sendjson=porterThread('sendjson',que,que_lock,interval=3)
    #start send data
    sendjson.start()
    
    collect.join()
    sendjson.join()


if __name__=="__main__":
    startTh()



