#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from multiprocessing.dummy import Pool as ThreadPool
import os
import time

Header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
DownLoadUrl = 'http://dldir1.qq.com/qqfile/qq/QQ7.8/16379/QQ7.8.exe'
Req = urllib2.Request(DownLoadUrl, headers=Header)
Respone = urllib2.urlopen(Req)
global Length
Length = int(Respone.headers['Content-Length'])
Length-=1
global LenList
global FDList
LenList = range(0, Length, 1048576)
FDList = range(100, 100 + len(LenList))
Index = range(0, len(LenList))
global fd2 
fd2 = 100
def openURL(index):
    start = LenList[index]
    if start == LenList[-1] :
        Header.update({'Range':'Bytes=%s-%s' % (start, Length)})
    else :
        Header.update({'Range':'Bytes=%s-%s' % (start, start+1048575)})
    Request = urllib2.Request(DownLoadUrl, headers=Header)
    Response = urllib2.urlopen(Request)
    Content = Response.read()
    f.seek(start, 0)
    f.write(Content)
    
    '''
    fd2=FDList[index]
    os.lseek(fd2, os.SEEK_SET, start)
    os.write(fd2, Content)
    os.close(fd2) '''


pool = ThreadPool(processes=4)
#fd = os.open('/tmp/'+DownLoadUrl.split('/')[-1], os.O_WRONLY|os.O_CREAT)
f = open('/tmp/'+DownLoadUrl.split('/')[-1], 'w')
pool.map(openURL, Index)
pool.close()
pool.join()
