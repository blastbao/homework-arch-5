#!/usr/bin/env python
# -*- coding: utf-8 -*-
from daemon import Daemon
import socket
import time
import Queue
import threading

html = """HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\nContent-Length: """
html404 = """HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 13\r\n\r\n<h1>404 </h1>"""
class handler(threading.Thread):
    def __init__(self, connQueue):
        threading.Thread.__init__(self)
        self.connQueue = connQueue
    def run(self, ):
        while True:
            conn = self.connQueue.get()
            read_data = conn.recv(10000)
            try:
                pic_name = read_data.split(" ")[1][1:]
                with file(pic_name) as f:
                    pic_content = f.read()
                    length = len(pic_content)
                    html_resp = html
                    html_resp += "%d\r\n\r\n" % (length)
                    html_resp += pic_content
            except:
                html_resp = html404
            
            while len(html_resp) > 0:
                sent_count = conn.send(html_resp)
    #            print "sent:", sent_count
                html_resp = html_resp[sent_count:]
            conn.close()
    
class agentD(Daemon):
    def run(self):
        listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_fd.bind(("0.0.0.0", 9000))
        listen_fd.listen(10)
        connQueue = Queue.Queue(20)
        for i in range(4):
            a = handler(connQueue)
            a.start()
        while True:
            conn, addr = listen_fd.accept()
            connQueue.put(conn)
#            print "coming", conn, addr

if __name__ == '__main__':
    agentd = agentD(pidfile="agentd.pid", stdout="agentd.log", stderr="agentd.log")
    agentd.run()
