#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: simple_multi_thread_serever
@time: 2015/11/15 17:24
"""
import socket
import time,Queue,gzip
from multiprocessing.dummy import Pool as ThreadPool
from cStringIO import StringIO

html = """HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nContent-Length: """
html404 = """HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 14\r\n\r\n<h1>404 </h1>"""
queue = Queue.Queue()

class agentD():
    def run(self):
        print 'Server Running...'
        listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_fd.bind(("0.0.0.0", 80))
        listen_fd.listen(10)
        while True:
            conn, addr = listen_fd.accept()
            raw={}
            raw['conn'] = conn
            raw['addr'] = addr
            queue.put(raw)


class multi_thread_worker():
    def work(self,name):
        while 1:
            if queue.qsize()>0:
                conn_raw = queue.get()
                print 'Thread %s start work' % str(name)+"\n"
                queue.task_done()
                conn = conn_raw['conn']
                addr = conn_raw['addr']
                print "raw conntect info :", addr,"\n"
                read_data = conn.recv(10000)
                pic_name = read_data.split(" ")[1][1:]
                print 'request file name is : '+pic_name+"\n"
                try:
                    with file(pic_name,'rb') as f:
                        # pic_content = gzip.read32(f.read())
                        # buf=StringIO()
                        # new_zip_file=gzip.GzipFile(mode="wb", fileobj=buf)
                        # new_zip_file.write(f.read())
                        pic_content = f.read()
                        # pic_content = buf.getvalue()
                        length = len(pic_content)
                        html_resp = html
                        html_resp += "%d\r\n\r\n" % (length)
                        html_resp += pic_content
                except:
                    html_resp = html404
                conn.send(html_resp)
                print 'Thread %s end work----' % str(name)+"\n"
                conn.close()

def type_filter(type):
    if not type:
        agentd = agentD()
        agentd.run()
    else:
        mt = multi_thread_worker()
        mt.work(type)

if __name__ == "__main__":
    server_work_thread = 6      #max worker thread,
    pool = ThreadPool(server_work_thread)
    init_type =[0]
    init_type.extend(xrange(1,server_work_thread))
    pool.map(type_filter,init_type)
    pool.join()



"""
Server Running...
Thread 3 start work

raw conntect info : ('127.0.0.1', 2851)

request file name is : 1.jpg

Thread 3 end work----

Thread 2 start work

raw conntect info : ('127.0.0.1', 2852)

request file name is : 1.jpg

Thread 2 end work----

Thread 5 start work

raw conntect info : ('127.0.0.1', 2853)

request file name is : 1.jpg

Thread 5 end work----

Thread 1 start work

raw conntect info : ('127.0.0.1', 2854)

request file name is : 1.jpg

Thread 1 end work----

"""
