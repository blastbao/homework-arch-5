#!/usr/bin/env python
# coding=utf-8

from daemon import Daemon
import socket
import time
import thread
import threading
import threadpool
import Queue

html = """HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\nContent-Length: """ #正常返回的头
html404 = """HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 13\r\n\r\n<h1>404 </h1>""" #404返回

class agentD(Daemon):
    def __init__(self, q1, pidfile, stdout, stderr):
        Daemon.__init__(self)
        self.q1 = q1
    def run(self):
        listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #定义socket，使用TCP/IP协议
        listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) #
        listen_fd.bind(("0.0.0.0", 9000)) #绑定9000端口
        listen_fd.listen(10) #开始监听，最多10个请求排队
        def acceptConn(name):
            print name
            while True:
                conn, addr = listen_fd.accept() #允许建立连接
                self.q1.put((conn,addr))
        def returnPic():
            while 1:
                if not self.q1.empty():
                    (conn, addr) = q1.get()
                    print "coming", conn, addr
                    read_data = conn.recv(10000) #读取受到的请求
                    print read_data
                    pic_name = read_data.split(" ")[1][1:] #解析GET请求的文件
                    print pic_name
                    try:
                        with file(pic_name) as f: #打开图片文件
                            pic_content = f.read() #读取文件
                            length = len(pic_content) #测量文件长度
                            html_resp = html
                            html_resp += "%d\r\n\r\n" % (length) #拼接返回的内容长度
                            print html_resp
                            html_resp += pic_content #拼接返回内容
                    except:
                        html_resp = html404 #如果出错则返回数据为404
                    conn.send(html_resp) #发送数据
                    conn.close() #关闭连接
        thread.start_new_thread(acceptConn, ("accept connection thread started",))
        for i in xrange(10):
            t1 = threading.Thread(target=returnPic, )
            t1.start()

if __name__ == "__main__":
    q1 = Queue.Queue(10)
    agentd = agentD(q1, pidfile="agentd.pid", stdout="agentd.log", stderr="agentd.log")
    agentd.run()