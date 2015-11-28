#!/usr/bin/env python
import Queue
import threading
import time
import commands
import pdb
import sys, os
list_time = [0]*2
list_c = [0]*2

class porterThread (threading.Thread):
	def __init__(self, name, q, ql=None, interval=None):
		threading.Thread.__init__(self)
		self.name = name
		self.q = q
		self.queueLock = ql
		self.interval = interval
		self.sock_l = [None]
	def run(self):
		if self.name[:-1] == 'collect':
			self.put_data()
		if self.name == 'sendjson':
			self.get_data()
	def put_data(self):
		atime = int(time.time())
		number = int(self.name[-1]) - 1
		list_c[number] = 1
		list_time[number] = atime
		time.sleep(1)
		#self.q.put(int(time.time()))
		strtime = "This time " + str(list_time[number]) + " " + self.name + " " +str(number) + " "+str(list_c[number])
 		self.q.put(strtime)
		#print strtime
		btime = int(time.time())
		list_c[number] = 0
	def get_data(self):
		while 1:
			print "get"
			if not self.q.empty():
				data = self.q.get()
				print data
			time.sleep(self.interval)
def startTh():
	q1 = Queue.Queue(10)
	ql1 = threading.Lock()
	list_time[0]=int(time.time())
	list_time[1]=int(time.time())
	sendjson = porterThread('sendjson', q1, ql1, interval=3)
	sendjson.start()
	while True :
		collect1 = porterThread("collect1", q1, ql1, interval=3)
		collect2 = porterThread("collect2", q1, ql1, interval=3)
		print "now " + str(time.time())
		#print max(list_c)
		if int(time.time()) - int(list_time[0]) >= 3 and list_c[0] == 1 and list_c[1] != 1 :
			collect2.start()
		elif int(time.time()) - int(list_time[1]) >= 3 and list_c[1] == 1 and list_c[0] != 1:
			collect1.start()
		elif max(list_c) == 0 and int(time.time()) - int(list_time[0]) >= 3 :
			collect1.start()
		time.sleep(1)
	collect1.join()
	collect2.join()
if __name__ == "__main__":
	startTh()
