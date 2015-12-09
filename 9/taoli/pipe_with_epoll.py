#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: pipe_with_epoll.py
@time: 2015/12/7 15:09
"""
import socket
import select
import Queue
import new_type


from multiprocessing.dummy import Pool as ThreadPool
max_read_header =50
queue = Queue.Queue()
addr = '0.0.0.0'
port = 8080
raw_conn={}
epoll_sock =select.epoll()

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
                    NT = new_type.new_type(raw,epoll_sock)
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



if __name__ == '__main__':
    server_work_thread = 6  # max worker thread,
    pool = ThreadPool(server_work_thread)
    init_type = [0]
    init_type.extend(xrange(1, server_work_thread))
    pool.map(type_filter, init_type)
    pool.join()

'''
Running Result:

echo 'sleep 3 && date'|nc localhost 8080

Wed Dec  9 10:51:03 CST 2015

'''