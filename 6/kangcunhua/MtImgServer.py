#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-11-15 16:40:02
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-11-19 17:29:15

"""
    第六次作业：将socket实现的通过http协议响应的图片服务器，将响应请求的处理改成多线程。
    已知问题：
        此处涉及到的守护进程继承，并没有起作用；
        如果不拆分成两个类，多重继承的初始化比较复杂；
        而且，起多线程时，针对类启动的多线程，不知会不会多次执行init操作。
"""
import socket
import time
import threading
from daemon import Daemon
html = """HTTP/1.1 200 OK\r\nContent-Type:image/jpeg\r\nConnection:close\r\nContent-length: """
html404 = """HTTP/1.1 404 Not Found\r\nContent-Type:text/html\r\nContent-length:13\r\n\r\n<h1>404</h1>"""


class ImgServerRps(threading.Thread):
    """docstring for ImgServer"""

    def __init__(self, name, listen_fd):
        threading.Thread.__init__(self)
        super(ImgServerRps, self).__init__()
        self.name = name
        self.listen_fd = listen_fd

    def dealwithReponse(self):

        while True:
            print 'thread name is :' + self.name
            conn, addr = self.listen_fd.accept()
            print "coming" + str(conn), str(addr)
            read_data = conn.recv(10000)
            print 'read_data:' + read_data
            try:
                pic_name = read_data.split()[1][1:]
                print pic_name
                with file(pic_name, 'rb') as f:
                    pic_content = f.read()
                    length = len(pic_content)
                    html_resp = html
                    html_resp += "%d\r\n\r\n" % (length)
                    # print html_resp
                    html_resp += pic_content
                    # print pic_content
            except:
                print "404 错误！"
                html_resp = html404

            sent_cnt = conn.send(html_resp)
            # print "sent: " + str(sent_cnt)
            conn.close()

    def run(self):
        self.dealwithReponse()


class agentD(Daemon):
    """
    初始化服务器，绑定服务端口
    """

    def __init__(self, **arg):
        # super(ImgServer, self).__init__()

        # 创建了一个socket对象：
        # type参数代表套接字类型，可为SOCK_STREAM(流套接字)和SOCK_DGRAM(数据报套接字)。
        # AF_INET表示创建的是ip v4的类型
        self.listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_fd.bind(('0.0.0.0', 9000))
        self.listen_fd.listen(10)
        print 'server is start,vis @ http://127.0.0.1:9000/2012.jpg'


if __name__ == '__main__':

    agentd = agentD(pidfile="agentd.pid",
                    stdout="agentd.log", stderr="agentd.log")
    # 初始化一个最大的子线程数
    maxSubThread = 3
    for i in xrange(maxSubThread):
        t1 = ImgServerRps(name='thread' + str(i), listen_fd=agentd.listen_fd)
        t1.start()

# output:
# server is start,vis @ http://127.0.0.1:9000/2012.jpg
# thread name is :thread0
# thread name is :thread1
# thread name is :thread2
# coming<socket._socketobject object at 0x0161CC38> ('127.0.0.1', 62116)
# read_data:GET /2012.jpg HTTP/1.1
# Host: 127.0.0.1:9000
# Connection: keep-alive
# Cache-Control: max-age=0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36
# Accept-Encoding: gzip, deflate, sdch
# Accept-Language: zh-CN,zh;q=0.8


# 2012.jpg
# thread name is :thread0
# coming<socket._socketobject object at 0x0171A998> ('127.0.0.1', 62117)
# read_data:GET /favicon.ico HTTP/1.1
# Host: 127.0.0.1:9000
# Connection: keep-alive
# Pragma: no-cache
# Cache-Control: no-cache
# User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36
# Accept: */*
# Referer: http://127.0.0.1:9000/2012.jpg
# Accept-Encoding: gzip, deflate, sdch
# Accept-Language: zh-CN,zh;q=0.8


# favicon.ico
# 404 occur
# thread name is :thread1
# coming<socket._socketobject object at 0x0171ABC8> ('127.0.0.1', 62125)
# coming<socket._socketobject object at 0x01720F80> ('127.0.0.1', 62126)
# read_data:GET /2012.jpg HTTP/1.1
# Host: 127.0.0.1:9000
# Connection: keep-alive
# Cache-Control: max-age=0
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36
# Accept-Encoding: gzip, deflate, sdch
# Accept-Language: zh-CN,zh;q=0.8


# 2012.jpg
# thread name is :thread2
# read_data:GET /favicon.ico HTTP/1.1
# Host: 127.0.0.1:9000
# Connection: keep-alive
# Pragma: no-cache
# Cache-Control: no-cache
# User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36
# Accept: */*
# Referer: http://127.0.0.1:9000/2012.jpg
# Accept-Encoding: gzip, deflate, sdch
# Accept-Language: zh-CN,zh;q=0.8


# favicon.ico
# 404 occur
# thread name is :thread0
