#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: multi_download.py
@time: 2015/11/1 19:55
"""
from multiprocessing.dummy import Pool as ThreadPool
import urllib2
import threading
import datetime


class mulit_threding_download():
    def __init__(self, url, thread_num=4):
        self.url = url
        self.thread_num = thread_num
        self.lock = threading.RLock()

    def get_work_ragnge(self):
        req = urllib2.Request(self.url)
        req.add_header('User-Agent', 'Mozilla 36.10')
        # req.add_header('Accept-encoding', 'gzip')
        req.get_method = lambda: 'HEAD'
        response = urllib2.urlopen(req)
        fileSize = response.headers.get('Content-Length', 0)
        print fileSize
        pos = []
        read_step = int(fileSize) / self.thread_num;
        for index in xrange(self.thread_num):
            if index + 1 == self.thread_num:
                end = int(fileSize) - 1
            else:
                end = int((index + 1) * read_step - 1)
            s = "%d-%d" % (index * read_step, end)
            pos.append(s)
        return pos

    def writer_worker(self, read_range):
        req = urllib2.Request(self.url)
        req.add_header('User-Agent', 'Mozilla 36.10')
        req.add_header("Connection", " Keep-Alive")
        start_pos = int(read_range.split('-')[0])
        end_pos = int(read_range.split('-')[1])
        s = "bytes=%d-%d" % (start_pos, end_pos)
        req.add_header("Range", s)
        res = urllib2.urlopen(req)
        save_file_name = self.url.split('/')[-1]
        with open(save_file_name, 'wb') as f:
            f.seek(start_pos)
            f.write(res.read())
            f.flush()

    def run(self):
        pool = ThreadPool(self.thread_num)
        pool.map(self.writer_worker, self.get_work_ragnge())

if __name__ == '__main__':
    print datetime.datetime.now()
    mulit_threding_download('http://dlsw.baidu.com/sw-search-sp/soft/47/15423/ZendStudio_V12.5.1_setup.1437380753.msi', 6).run()
    print datetime.datetime.now()