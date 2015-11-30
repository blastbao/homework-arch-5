#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.1
@author: Mark Tao
@contact: urtop@qq.com
@file: multi_thread_monitor.py
@time: 2015/11/8 18:13
"""

import threading, Queue, time
import get_sys_info

lock = threading.Lock()
max_num_per_wokrer = 3  # max num for worker thread
syn_list = [0] * max_num_per_wokrer

class Thread_data_handel_worker(threading.Thread):
    def __init__(self, name, queue, interval=3):
        threading.Thread.__init__(self)
        self.interval = interval
        self.q = queue
        self.name = name

    def run(self):
        while (1):  # get data from Queue if not empty
            if ( self.q.qsize() > 0 ):
                print "Handel worker " + self.name + ' start  data push \n'
                fake_client_sender.send(self.q.get())  # send to remote server
                self.q.task_done()
                print "Handel worker " + self.name + ' get work done \n'
                time.sleep(self.interval)


class Thread_data_pusher_worker(threading.Thread):
    def __init__(self, name, queue, interval=1):
        threading.Thread.__init__(self)
        self.q = queue
        self.interval = interval
        self.name = name

    def run(self):
        while 1:
            res = lock.acquire()                                                         # get locked and get status of the lock
            if (syn_list[int(self.name)] == min(syn_list) and res ):  # reschedule the syn_list
                syn_list[int(self.name)] += 1
                lock.release()
                print "Pusher worker " + self.name + ' start --- \n'
                start_time = int(time.time())
                mon = get_sys_info.mon()
                self.q.put(mon.runAllGet(True))  # push data to Queue from  get_sys_info  class
                end_time = int(time.time())
                print "Pusher worker " + self.name + ' finish  \n'
                time.sleep(self.interval - ((start_time - end_time) % self.interval))


            else:
                lock.release()
                print "Pusher worker " + self.name + ' waiting=====>  \n'
                time.sleep(0.5)


class fake_client_sender():  # TBD

    def __init__(self):
        pass

    @staticmethod
    def send(data):
        print 'Get_data: ' + str(data) + '\n'
        pass


if __name__ == '__main__':
    q = Queue.Queue()
    for i in xrange(max_num_per_wokrer):  # use 6 total threads for both 2 workers
        t1 = Thread_data_pusher_worker(i, q, 2)
        t1.start()
        t2 = Thread_data_handel_worker(i, q, 3)
        t2.start()
    q.join()

'''
Running result:
Pusher worker 0 start ---

Pusher worker 0 finish

Handel worker 0 start  data push

Get_data: 6

Pusher worker 1 start ---
Handel worker 0 get work done


Pusher worker 1 finish

Handel worker 1 start  data push

Get_data: 7

Handel worker 1 get work done



'''