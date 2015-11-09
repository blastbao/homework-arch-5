#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: multi_thread_monitor.py
@time: 2015/11/8 18:13
"""

import threading,Queue,time
import get_sys_info

class Thread_data_handel_worker(threading.Thread):

    def __init__(self, name, queue,  interval=3):
        threading.Thread.__init__(self)
        self.interval = interval
        self.q = queue
        self.name = name

    def run(self):
        while (1):                           # get data from Queue if not empty
            if ( self.q.qsize() >0 ):
                print "Handel worker "+self.name+' start  data push \n'
                fake_client_sender.send(self.q.get())   #send to remote server
                self.q.task_done()
                print "Handel worker "+self.name+' get work done \n'
                time.sleep(self.interval)


class Thread_data_pusher_worker(threading.Thread):

    def __init__(self, name, queue, interval=1):
        threading.Thread.__init__(self)
        self.q = queue
        self.interval = interval
        self.name = name

    def run(self):
        while 1:
            print "Pusher worker "+self.name+' start --- \n'
            start_time = int(time.time())
            mon = get_sys_info.mon()
            self.q.put(mon.runAllGet(True))    #push data to Queue from  get_sys_info  class
            end_time = int(time.time())
            print "Pusher worker "+ self.name+' finish  \n'
            time.sleep(self.interval - ((start_time-end_time) % self.interval))



class fake_client_sender():       # TBD

    def __init__(self):
        pass

    @staticmethod
    def send(data):
        print 'Get_data: '+str(data)+'\n'


if __name__ == '__main__':
    q = Queue.Queue()
    max_num_per_wokrer = 6
    for i in xrange(max_num_per_wokrer):    #use 6 total threads for both 2 workers
        t1 =Thread_data_pusher_worker(i, q,2)
        t1.start()
        t2 = Thread_data_handel_worker(i, q , 3)
        t2.start()
    q.join()

'''Running Result :

Pusher worker 0 start ---

Pusher worker 0 finish

Handel worker 0 start  data push

Get_data: 449000

Handel worker 0 get work done

Pusher worker 1 start ---

Pusher worker 1 finish

Handel worker 1 start  data push

Get_data: 449000

Handel worker 1 get work done

Pusher worker 2 start ---

Pusher worker 2 finish

Handel worker 2 start  data push

Get_data: 450000

Handel worker 2 get work done

Pusher worker 3 start ---

Pusher worker 3 finish

Handel worker 3 start  data push

Get_data: 450000


'''