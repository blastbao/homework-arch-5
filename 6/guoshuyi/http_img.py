#!/usr/bin/env python
# coding=utf-8

from daemon import Daemon
import threading
import socket
import time

html = """HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nContent-Length: """
html404 = """HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 13\r\n\r\n<h1>404 </h1>"""

class agentD(Daemon):
    def run(self):
        #打开一个socket，第一个参数ip协议，第二个tcp协议
        listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        #设置socket端口reuse
        listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #绑定监听端口
        listen_fd.bind(("0.0.0.0", 40000))
        #设置socket等待队列
        listen_fd.listen(10)
        taskList = []
        for i in range(8):
            th = Th(i, listen_fd)
            taskList.append(th)
            th.start()
        for i in taskList:
            i.join()

class Th(threading.Thread):
    def __init__(self, name, fd):
        threading.Thread.__init__(self)
        self.name = name
        self.fd = fd

    def run(self):
        print "%s running" % self.name
        listen_fd = self.fd
        while True:
            #接受一个连接
            conn, addr = listen_fd.accept()
            print "coming ",conn,addr
            #读取连接的数据
            read_data = conn.recv(1024)
            print read_data
            #处理http协议，取出img的文件名
            pic_name = read_data.split()[1][1:]
            print pic_name
            try:
                #打开文件
                with file(pic_name) as f:
                    #读取文件
                    pic_content = f.read()
                    #计算文件Bytes
                    length = len(pic_content)
                    #使用http头
                    html_resp = html
                    #拼接Content-Length
                    html_resp += "%d\r\n\r\n" % (length)
                    print html_resp
                    #拼接data
                    html_resp += pic_content
            except:
                print "404 occur"
                html_resp = html404

            sent_cnt = conn.send(html_resp)
            print "sent: ",sent_cnt
            conn.close()

if __name__ == "__main__":
    agentd = agentD(pidfile="agentd.pid", stdout="agentd.log", stderr="agentd.log")
    agentd.run()
