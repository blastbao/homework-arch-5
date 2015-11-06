#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import socket
import sys
import os

Header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
DownLoadUrl = 'http://dldir1.qq.com/qqfile/qq/QQ7.8/16379/QQ7.8.exe'
Req = urllib2.Request(DownLoadUrl, headers=Header)
Req.get_method = lambda : 'HEAD'
Respone = urllib2.urlopen(Req)
Length = int(Respone.headers['Content-Length'])
Length-=1
LenList = range(0, Length, 1048576)
File = '/tmp/%s' % DownLoadUrl.split('/')[-1]
f = open(File, 'wb')
LaterDownList = list()
def returnRequest(rangNum):
    if rangNum == LenList[-1] :
        Header.update({'Range':'bytes=%s-%s' % (rangNum, Length)})
    else :
        Header.update({'Range':'bytes=%s-%s' % (rangNum, rangNum+1048575)})
    Request = urllib2.Request(DownLoadUrl, headers=Header)
    return Request

def writeRespone(request, fileposition):
    Response = urllib2.urlopen(request, timeout=10)
    f.seek(fileposition, 0)
    f.write(Response.read())

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

def laterDown(start):
    Request = returnRequest(start)
    try:
        writeRespone(Request, start)
        LasterDownList.index(start)
        LasterDownList.pop(start)
    except Exception, e:
        print e,
        print("second dowuload failure")
        sys.exit(127)

map(openURL, LenList)
if len(LaterDownList) == 0 : map(laterDown, LaterDownList)
f.close()
if len(LaterDownList) > 0 : print LaterDownList, "not download"
