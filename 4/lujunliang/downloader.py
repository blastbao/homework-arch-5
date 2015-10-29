#!/usr/bin/env python
#conding=utf-8

import sys
import os
import urllib2
import threading
import time


class DownLoader():
    def __init__(self, WorkerCount = 1, download_url = ur"http://dldir1.qq.com/qqfile/qq/QQ7.8/16379/QQ7.8.exe"):
        if len(sys.argv) >= 2:
            if sys.argv[1].startswith('http://'):
                download_url = sys.argv[1]
            else:
                print "download_url is illegal"
                return 0
        self.download_url = download_url
        self.WorkerCount = WorkerCount
        self.file_name = download_url.split('/')[-1]
        try:
            req = urllib2.Request(download_url)
            req.get_method = lambda: 'HEAD'
            resp = urllib2.urlopen(req).headers
            self.file_size = int(resp['Content-Length'])
            self.file_offset = int(self.file_size/WorkerCount) 
            self.fd = open(self.file_name, 'w+')
        except Exception,e:
            print e
            return 0
    def DownLoadWorker(self, p_start, p_end, p_num):
        req = urllib2.Request(self.download_url)
        req.add_header('Range', 'Bytes=' + str(p_start) + '-' + str(p_end))
        try:
            resp = urllib2.urlopen(req)
            self.save(resp.read(), p_start, p_num)
        except Exception,e:
            print e
            sys.exit(2)
    def save(self, data, p_start, p_num):
        try:
            fd = os.dup(self.fd.fileno())
            fd_wr = os.fdopen(fd, 'w+')
            fd_wr.seek(p_start)
            fd_wr.write(data)
            print "thread %d ---OK---" % p_num
        except Exception,e:
            print e
            return 0

    def distribute(self):
        PositionList = []
        for Position in range(0, self.file_size + 1, self.file_offset):
            PositionList.append(Position)
        file_end = self.file_size % self.WorkerCount
        if file_end != 0:
            PositionList.append(self.file_size)
        return PositionList[1:]

        
    def run(self):
        thread_list = []
        n = 0
        for size in self.distribute():
            print 'thread %d - start: %s, end: %s' % (n, size - self.file_offset,\
                                                        size)
            thread = threading.Thread(target=self.DownLoadWorker,\
                                    args = (size - self.file_offset, size, n))
            thread.start()
            thread_list.append(thread)
            n += 1
        for i in thread_list:
            i.join()
        self.fd.close()
        print 'File:%s was Downloaded success!' % self.file_name
if __name__ == '__main__':
    time_start = time.time()
    down = DownLoader(4)
    down.run()
    time_end = time.time()
    used_time = time_end - time_start
    print "used time: %.4f s" % used_time
