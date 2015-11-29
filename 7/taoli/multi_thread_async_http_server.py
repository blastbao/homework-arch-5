#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: multi_thread_async_http_server.py
@time: 2015/11/27 15:09
"""
import socket
import select
import Queue
import new_type
# import pdb
# import threading
# import sys
# sys.setrecursionlimit(1000000)
from multiprocessing.dummy import Pool as ThreadPool
max_read_header =3000
queue = Queue.Queue()
addr = '0.0.0.0'
port = 8080
raw_conn={}
epoll_sock =select.epoll()
http_response = """HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: Close\r\nContent-Length:"""
html404 = """HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 14\r\n\r\n<h1>404 </h1>"""
status={
    'close':1,
    'more':2,
    'complete':3
}
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((addr, port))
sock.listen(1)
sock.setblocking(0)
epoll_sock.register(sock.fileno(), select.EPOLLIN)
class listen_worker():
    def __init__(self, addr, port):
        # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        # sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # sock.bind((addr, port))
        # sock.listen(1)
        # sock.setblocking(0)
        # epoll_sock.register(sock.fileno(), select.EPOLLIN)
        # print epoll_sock.poll()
        while 1:
            for fd,events in epoll_sock.poll():
                if (select.EPOLLERR & events) or (select.EPOLLHUP & events):
                    close(fd)
                elif (select.EPOLLIN & events) and (fd == sock.fileno()):
                    conn, addr = sock.accept()
                    conn.setblocking(0)
                    epoll_sock.register(conn, select.EPOLLIN)
                    raw_conn[conn.fileno()] = conn
                    queue.put(conn)



class multi_therad_worker():
    def work(self):
        while 1:
            if not  queue.empty():
                    raw = queue.get()
                    NT = new_type.new_type(raw,epoll_sock,logic)
                    fd = NT.run()
                    # print 'thread end'
                    # close(fd)


def close(fd):
    try:
        # lock.acquire()
        raw_conn.pop(fd)
        # lock.release()
    except KeyError,msg:
        # print 'close error'
        pass

def type_filter(type):
    if not type:
        lw = listen_worker(addr, port)
    else:
        mt = multi_therad_worker()
        mt.work()

def logic(res):
        try:
            pic_name = res.split(" ")[1][1:]
            with file(pic_name, 'rb') as f:
                res = f.read()
            return http_response + str(len(res)) + '\r\n\r\n' + res
            return response
        except:
            return html404

if __name__ == '__main__':
    # lock = threading.Lock()
    server_work_thread = 6  # max worker thread,
    pool = ThreadPool(server_work_thread)
    init_type = [0]
    init_type.extend(xrange(1, server_work_thread))
    pool.map(type_filter, init_type)
    pool.join()
