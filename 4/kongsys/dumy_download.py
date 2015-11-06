#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
from multiprocessing.dummy import Pool as ThreadPool
import os
import time
import sys
import socket
import re

if len(sys.argv) == 1 : sys.exit(1)
Header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
DownLoadUrl = sys.argv[1]
Req = urllib2.Request(DownLoadUrl, headers=Header)
Req.get_method = lambda : 'HEAD'
Respone = urllib2.urlopen(Req)
Length = int(Respone.headers['Content-Length'])
Length-=1
LenList = range(0, Length, 1048576)
print LenList
LaterDownList = list()
if ('Content-Disposition' in Respone.headers) and ('filename' in Respone.headers['Content-Disposition']):
    condisStr = Respone.headers['Content-Disposition']
    File = '/tmp/%s' % re.findall(r'\bfilename=.*', condisStr)[0].split("=")[1].replace('"', '') 
else:
    if len(sys.argv) == 3 :
        File = '/tmp/%s' % sys.argv[2]
    else:
        File = '/tmp/%s' % DownLoadUrl.split('/')[-1]
    
def returnRequest(rangNum):
    if rangNum == LenList[-1] :
        Header.update({'Range':'bytes=%s-%s' % (rangNum, Length)})
    else :
        Header.update({'Range':'bytes=%s-%s' % (rangNum, rangNum+1048575)})
    Request = urllib2.Request(DownLoadUrl, headers=Header)
    return Request

def writeRespone(request, fileposition):
    Response = urllib2.urlopen(request, timeout=10)
    fd2 = os.dup(fd)
    os.lseek(fd2, fileposition, os.SEEK_SET)
    print os.write(fd2, Response.read())
    os.close(fd2)

def openURL(start):
    Request = returnRequest(start)
    try:
        writeRespone(Request, start)
    except socket.error, e:
        print e,
        print("%d have error, download later " % start)
        LaterDownList.append(start)
    except urllib2.HTTPError, e:
        print e,
        print("resource unavailable")
        os.remove(File)
        sys.exit(127)

pool = ThreadPool(processes=1)
fd = os.open(File, os.O_WRONLY|os.O_CREAT)
print "go"
pool.map(openURL, LenList)
pool.close()
pool.join()
os.close(fd)
