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

browersStr = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'

Header = { 'User-Agent' : browersStr }
DownLoadUrl = sys.argv[1]

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
#split by 512K
LforL = splitLen(Length, 5242288)

#get file name
if ('Content-Disposition' in Respone.headers) and ('filename' in Respone.headers['Content-Disposition']):
    condisStr = Respone.headers['Content-Disposition']
    File = '/tmp/%s' % re.findall(r'\bfilename=.*', condisStr)[0].split("=")[1].replace('"', '') 
elif len(sys.argv) == 3 :
    File = '/tmp/%s' % sys.argv[2]
else:
    File = '/tmp/%s' % DownLoadUrl.split('/')[-1]
    

def writeRespone(request, fileposition):
    Response = urllib2.urlopen(request, timeout=100)
    print fileposition
    fd2 = os.dup(f.fileno())
    file = os.fdopen(fd2, 'w')
    file.seek(fileposition)
    file.write(Response.read())
    file.close()

def openURL(*args):
    Header.update({'Range':'bytes=%s-%s' % (args[0][0], args[0][1])})
    Request = urllib2.Request(DownLoadUrl, headers=Header)
    writeRespone(Request, args[0][0])
    '''
    try:
        writeRespone(Request, args[0][0])
    except socket.error, e:
        print e,
        openURL(args)
    except urllib2.HTTPError, e:
        print e,
        print("resource unavailable")
        os.remove(File)
        sys.exit(127)
    '''

pool = ThreadPool(processes=4)
f = open(File, 'w')
print "go"
pool.map(openURL, LforL)
pool.close()
pool.join()
f.close()
