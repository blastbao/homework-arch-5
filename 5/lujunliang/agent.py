#!/usr/bin/python
import Queue
import time
import json
import threading
import urllib2
import socket
import commands
import pdb
import sys, os
from getSystemItems import getItems
from nbNetUtils import sendData_mh

sys.path.insert(1, os.path.join(sys.path[0], '..'))

trans_l = ['localhost:5000']

class porterThread(threading.Thread):
    def __init__(self, name, q, ql = None, interval = None):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
        self.lock = ql
        self. interval = interval
        self.sock_l = [None]

    def run(self):
        if self.name.find('collect') != -1:
            self.put_data()
        if self.name == 'sendjson':
            self.get_data()

    def put_data(self):
        m = getItems()
        #atime = int(time.time())
        while 1:
            print "This is worker %s" % self.name
            self.lock.acquire()
            data = m.runAllGet()
            print "collected data: %s" % data
            self.q.put(data)
            self.lock.release()
            time.sleep(self.interval)
            #btime = int(time.time())
            #time.sleep(self.interval - ((btime - atime)%self.interval))

    def get_data(self):
        while 1:
            print "get"
            if not self.q.empty():
                data = self.q.get()
                print data
                #sendData_mh(self.sock_l, trans_l, json.dumps(data))
            time.sleep(self.interval)

def startTh():
    q1 = Queue.Queue(10)
    q11 = threading.Lock()
    for i in range(2):
        collect = porterThread('collect' + str(i), q1, q11, interval = 3)
        collect.start()
        time.sleep(3)
    time.sleep(0.5)
    sendjson = porterThread('sendjson', q1, q11, interval = 3)
    sendjson.start()
    #q2.Queue.Queue(10)
    print "start"
    collect.join()
    sendjson.join()
if __name__ == '__main__':
    startTh()
