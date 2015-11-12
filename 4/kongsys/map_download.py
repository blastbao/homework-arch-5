#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import socket
import sys
import os

browersStr = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'

Header = { 'User-Agent' : browersStr }
DownLoadUrl = 'http://dldir1.qq.com/qqfile/qq/QQ7.8/16379/QQ7.8.exe'

def splitLen(filelength, filestep):
    filelength -= 1
    stepStart = [0]
    stepStop = [filestep - 1]
    while (stepStop[-1] < filelength):
        stepStart.append(stepStart[-1] + filestep)
        stepStop.append(stepStart[-1] + filestep - 1)
    else :
        stepStop[-1] = filelength
    return tuple(zip(stepStart, stepStop))

Req = urllib2.Request(DownLoadUrl, headers=Header)
Req.get_method = lambda : 'HEAD'
Respone = urllib2.urlopen(Req)

Length = int(Respone.headers['Content-Length']) - 1

LforL = splitLen(Length, 5242288)
File = '/tmp/%s' % DownLoadUrl.split('/')[-1]
f = open(File, 'wb')

def writeRespone(request, fileposition):
    Response = urllib2.urlopen(request, timeout=10)
    f.write(Response.read())

def openURL(start):
    Header.update({'Range':'bytes=%s-%s' % (args[0][0], args[0][1])})
    Request = urllib2.Request(DownLoadUrl, headers=Header)
    writeRespone(Request, args[0][0])

map(openURL, LenList)
f.close()
