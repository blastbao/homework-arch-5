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

trans_l = ['localhost:50000']
class producerThread (threading.Thread):
    def __init__(self, name, q, ql=None, interval=None):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
        self.queueLock = ql
        self.interval = interval
        self.sock_l = [None]

    def run(self):
        #self.name == 'collect':
        self.put_data()


#    def put_data(self):
#        m = mon()
#        #atime=int(time.time())
#        while 1:
#            print "Starting " + self.getName()
#            #print data 
#            self.queueLock.acquire()
#            data = m.runAllGet()
#            self.q.put(data)
#            self.queueLock.release()
#            time.sleep(self.interval)
            #btime=int(time.time())
            #print '%s  %s' % (str(data), self.interval-((btime-atime)%30))
            #time.sleep(self.interval-((btime-atime)%self.interval))
            
    def  put_data(self):
         atime=int(time.time())
         m = mon()
         while 1:
            print "Starting " + self.getName()
            #self.queueLock.acquire()
            #if not self.q.empty():
            if self.queueLock.acquire():
                data = m.runAllGet()
                print data
                self.q.put(data)
               # self.queueLock.release()
            else:
                pass
                #self.queueLock.release()
            time.sleep(self.interval)

            #btime=int(time.time())
            #time.sleep(self.interval-((btime-atime)%self.interval))



class consumerThread (threading.Thread):
    def __init__(self, name, q, ql=None, interval=None):
        threading.Thread.__init__(self)
        self.name = name
        self.q = q
        #self.queueLock = ql
        self.interval = interval
        self.sock_l = [None]

    def run(self):
        self.get_data()

    def get_data(self):
        while 1:
            #print "get " + self.getName()
            #self.queueLock.acquire()
            if not self.q.empty():
                data = self.q.get()
                print data
                #pdb.set_trace()
                #sendData_mh(self.sock_l, trans_l, json.dumps(data))
            #self.queueLock.release()
            time.sleep(self.interval)

def startTh():
    q1 = Queue.Queue(3)
    ql1 = threading.Lock()
    for i in xrange(thread_count):
        collect = producerThread('collect ' +str(i), q1, ql1, interval=3)
        collect.start()
    time.sleep(0.5)
    sendjson = consumerThread('sendjson', q1, ql1, interval=3)
    sendjson.start()
    q2 = Queue.Queue(9)
    collect.join()
    sendjson.join()
if __name__ == "__main__":
    thread_count = 3
    startTh()

