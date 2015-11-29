#!/usr/bin/env python
#coding=utf-8
#疑问：怎么才能按ctrl+c停下来啊？不清楚把KeyboardInterrupt加在哪里

from daemon import Daemon
import time
import socket
import threading

html = '''
HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\nContent-Length:
'''
html404 = '''
HTTP/1.1 404 Not Found\r\nConetent-Type: text/html\r\nContent-Length: 13\r\n\r\n<h1>404 </h1>
'''

class agentD(Daemon):
    def run(self):
        listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_fd.bind(('0.0.0.0', 9000))
        listen_fd.listen(10)
        self.listen_fd = listen_fd

    def req_resp(self):
        while 1:
            conn, addr = self.listen_fd.accept()
            print "coming", conn, addr
            read_data = conn.recv(1024)

            try:
                pic_name = read_data.split(" ")[1][1:]
                print pic_name
                with file(pic_name) as f:
                    pic_content = f.read()
                    length = len(pic_content)
                    html_resp = html
                    html_resp += "%d\r\n\r\n" % (length)
                    print html_resp
                    html_resp += pic_content
            except:
                print html404
                html_resp = html404

            while len(html_resp) > 0:
                sent_cnt = conn.send(html_resp)
                print "sent:", sent_cnt
                html_resp = html_resp[sent_cnt:]
            conn.close()

if __name__ == '__main__':
    agentd = agentD(pidfile="agentd.pid", stdout="agentd.log", stderr="agentd.log")
    agentd.run()

    tlist = []

    #启4个线程
    for i in range(4):
        t = threading.Thread(target=agentd.req_resp,)
        tlist.append(t)

    for t in tlist:
        t.start()

    for t in tlist:
        t.join()
