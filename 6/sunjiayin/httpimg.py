#!/usr/bin/env python
import Queue
import threading
import time
import socket
from daemon import Daemon
html = """HTTP/1.1 200 OK\r\nContent-Type:image/jpeg\r\nContent-Type:close\r\nContent-length: """
html404 = """HTTP/1.1 404 Not Found\r\nContent-Type:text/html\r\nContent-length:12\r\n\r\n<h1>404</h1>"""

class agentD(Daemon):
	def startTH(self):
		q1 = Queue.Queue(10)
		httpser = ThreadAD("httpser", q1)
		httpser.start()
		for x in xrange(4):
			httpres = ThreadAD("httpres", q1)
			httpres.start()
		httpser.join()
		httpres.join()
class ThreadAD(threading.Thread):
	def __init__(self, name, qu):
		threading.Thread.__init__(self)
		self.name = name
		self.qu = qu
	def run(self):
		if self.name == "httpser" :
			self.httpser()
		elif self.name == "httpres":
			self.httpresp()
	def httpser(self):
		listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
		listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
		listen_fd.bind(('0.0.0.0', 9990))
		listen_fd.listen(10)
		while True:
			conn, addr = listen_fd.accept()
			#read_data = conn.recv(1000)
			#pic_name = read_data.split(" ")[1][1:]
			#print pic_name
			self.qu.put((conn,addr))
	def httpresp(self):
		while True:
			try:
				conn, addr = self.qu.get()
				read_data = conn.recv(1000)
				pic_name = read_data.split(" ")[1][1:]
				print pic_name
				with file(pic_name) as f:
					pic_content = f.read()
					length = len(pic_content)
					html_resp = html + "%d\r\n\r\n" % (length)
					print html_resp
					html_resp += pic_content
			except Exception, e:
				html_resp = html404
			sent_cnt = conn.send(html_resp)	
			conn.close()
if __name__ == "__main__":
	agentd = agentD(pidfile="agentd.pid", stdout="agentd.log", stderr="agentd.log")
	agentd.startTH()
