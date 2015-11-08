#coding=utf-8
#!/usr/bin/python2.7
#__author__ = 'louis'

import sys
import os
import urllib2
from threading import Thread

'''
1. 获取文件大小
2. 任务拆分 请求文件的range/threadNum
3.多线程下载，文件聚合
'''

url=sys.argv[1]
thread_num=int(sys.argv[2])
filename=url.split('/')[-1]

def download(size,files):

    header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/    537.36' }
    req = urllib2.Request(url,headers=header)
    # 添加HTTP Header(RANGE)设置下载数据的范围
    req.headers['Range'] = 'bytes=%s' % size
    #req = urllib2.Request(url,headers=head)
    data = urllib2.urlopen(req).read()

    #with open('QQ.exe','w+') as f:
    f = files
    f.seek(int(size.split('-')[0]))
    f.write(data)
    f.flush()

file_size=int(urllib2.urlopen(url).info()['Content-Length'])
part_size=file_size / thread_num
last_size=(thread_num - 1)*part_size
Rangelist=[(str(x),str(x + part_size - 1)) for x in xrange(0,file_size,part_size) if x < last_size]


def main():
    threads = []
    file_fd = []
    for part in Rangelist:
        part = '%s-%s' % part
        file_fd.append(open(filename,'w+'))
        threads.append(Thread(target=download,args=(part,file_fd.pop())))
    else:
        file_fd.append(open(filename,'w+'))
        threads.append(Thread(target=download,args=(str(last_size)+'-',file_fd.pop())))

    for t in threads:
        t.start()
    for t in threads:
        t.join()

if __name__ == '__main__':
    main()
