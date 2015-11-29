#!/usr/bin/python
from Queue import Queue
from threading import Thread
import time
import json
import urllib2
import socket
import commands
import pdb
from moniItems import mon
import inspect
import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
#from nbNet.nbNetFramework import sendData_mh

trans_l = ['localhost:50000']

data = {}

'''Get collect methods dict'''
class get_mothod_dict(mon):
    def __init__(self):
        self.method_dict = {}
        mon.__init__(self)
    def runAllGet(self):
        for fun in inspect.getmembers(self,predicate=inspect.ismethod):
            if fun[0] == 'userDefineMon':
                self.method_dict['userDefineMon'] = fun[1]
            elif fun[0][:3] == 'get':
                self.method_dict[fun[0][3:]]=fun[1]
        return self.method_dict

'''Handle data'''
class porterThread:
    def __init__(self,interval,collect_queue,method_dict,thread_num,handle_queue):
        self.interval = interval
        self.collect_queue = collect_queue
        self.handle_queue = handle_queue
        self.method_dict = method_dict
        self.thread_num = thread_num
    

    '''Get the data collected '''
    def  get_data_put(self,i):
        while True:
            method_name = self.collect_queue.get()
            if method_name == 'userDefineMon':
                data.update(self.method_dict['userDefineMon']()) 
            else:
                data[method_name] = self.method_dict[method_name]()
            print "Thread-%d: "%i+method_name
            self.collect_queue.task_done()
    "multi Thread collection and one sending thread "
    def multi_collect_send(self):
        while True:
            for i in xrange(self.thread_num):
                worker = Thread(target=self.get_data_put,args=(i,))
                worker.setDaemon(True)
                worker.start()
            for method_name in self.method_dict:
                self.collect_queue.put(method_name)
            self.handle_queue.put(data)
            #self.collect_queue.join()
            #print "data"+str(data)
            time.sleep(self.interval)
            send_worker = Thread(target=self.getdata_from_queue)
            send_worker.start()
    "Get data from handle_queue"
    def getdata_from_queue(self):
        while True:
            if not self.handle_queue.empty():
                send_data = self.handle_queue.get()
                if 'Time' in send_data:
                    print "send_data:"+str(send_data)
                  # sendData_mh(self.sock_l, trans_l, json.dumps(data))
            time.sleep(self.interval)
    

def startTh():
    method_dict = get_mothod_dict().runAllGet()
    collect_queue = Queue()
    handle_queue = Queue(10)
    handle = porterThread(interval=3,collect_queue=collect_queue,method_dict=method_dict,thread_num=3,handle_queue=handle_queue)
    handle.multi_collect_send()

if __name__ == "__main__":
    startTh()
