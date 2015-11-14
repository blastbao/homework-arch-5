#!/usr/bin/python
import Queue
import threading
import time
import json
import urllib2
import socket
import commands
import pdb
from moniItems import mon

import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet.nbNetFramework import sendData_mh

trans_l = ['localhost:50000']

gettime = 0
class porterThread (threading.Thread):
    def __init__(self, name, q, ql=None, interval=None):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
        self.interval = interval
        self.sock_l = [None]

    def run(self):
        if self.name == 'collect1':
            self.put_data()
        elif self.name == 'collect2':
            self.bak_put()
        elif self.name == 'sendjson':
            self.get_data()

    def put_data(self):
        m = mon()
        atime=int(time.time())
        while 1:
            global gettime
            gettime = int(time.time())
            print '1 is running'
            data = m.runAllGet()
            self.q.put(data)
            btime=int(time.time())
            time.sleep(self.interval-((btime-atime)%self.interval))
    def bak_put(self):
        m = mon()
        atime = int(time.time())
        while 1:
            baktime = int(time.time())
            timeout = baktime - gettime
            if timeout > self.interval:
                print '2 is running'
                data = m.runAllGet()
                self.q.put(data)
                btime = int(time.time())
                time.sleep(self.interval-((btime-atime)%self.interval))

    def get_data(self):
        while 1:
            if not self.q.empty():
                data = self.q.get()
                sendData_mh(self.sock_l, trans_l, json.dumps(data))
            time.sleep(self.interval)

def startTh():
    q1 = Queue.Queue(10)
    ql1 = threading.Lock()
    collectPut = porterThread('collect1', q1, ql1, interval=3)
    collectPut.start()
    collectBak = porterThread('collect2', q1, ql1, interval=3)
    collectBak.start()
    time.sleep(0.5)
    sendjson = porterThread('sendjson', q1, ql1, interval=3)
    sendjson.start()
    collectPut.join()
    collectBak.join()
    sendjson.join()
if __name__ == "__main__":
    startTh()


