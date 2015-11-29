#!/usr/bin/env python
#coding=utf-8

from daemon import Daemon
import socket
import time
from multiprocessing.dummy import Pool
import Queue
import threading

html = """HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\nContent-Length: """
html404 = """HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 13\r\n\r\n<h1>404 </h1>"""
queue = Queue.Queue(20)

class agentD(Daemon):
    def run(self):
        #socket注册
        listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_fd.bind(("0.0.0.0", 9000))
        listen_fd.listen(10)
        while True:
            conn, addr = listen_fd.accept()
            print "coming", conn, addr
            #将socket连接对象放入队列中，方便线程间的通信
            raw = {
                'conn':conn,
                'addr':addr
                }
            try:
                queue.put(raw)
            except Exception as e:
                print e


def worker(name):
    while True:
        #如果队列长度大于0，则开始处理队列中的信息
        if queue.qsize() > 0:
            raw = queue.get()
            conn = raw['conn']
            addr = raw['addr']
            read_data = conn.recv(1000)
            #提取请求的图片名称
            pic_name = read_data.split(" ")[1][1:]
            print pic_name
            try:
                with file(pic_name) as f:
                    #将图片内容读到pic_content中
                    pic_content = f.read()
                    length = len(pic_content)
                    html_resp = html
                    html_resp += "%d\r\n\r\n" % length
                    print html_resp
                    html_resp += pic_content
            except Exception as e:
                #读取图片出现问题则报404
                print "404"
                print e
                html_resp = html404

            while len(html_resp) > 0:
                #将图片内容返回给浏览器
                sent_cnt = conn.send(html_resp)
                print "send: ", sent_cnt
                html_resp = html[sent_cnt:]
            conn.close()
def init_agent(flag):
    if not flag:
        agented = agentD()
        agented.run()
    else:
        worker(flag)

if __name__ == '__main__':
    #agented = agentD(pidfile = "agentd.pid", stdout = "agentd.log", stderr = "agentd.log")
    #agented.run()
    #queue = Queue()
    #q = Queue.Queue(20)
    max_threads = 100
    #创建线程池
    pool = Pool(max_threads)
    task_list = list(range(max_threads + 1))
    pool.map(init_agent, task_list)

    pool.close()
    pool.join()
