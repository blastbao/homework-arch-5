#!/usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2

Header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
DownLoadUrl = 'http://dldir1.qq.com/qqfile/qq/QQ7.8/16379/QQ7.8.exe'
Req = urllib2.Request(DownLoadUrl, headers=Header)
Respone = urllib2.urlopen(Req)
Length = int(Respone.headers['Content-Length'])
Length-=1
LenList = [ x for x in range(0, Length, 1048576)]

def openURL(start, method = lambda : 'GET'):
    if start == LenList[-1] :
        Header.update({'Range':'Bytes=%s-%s' % (start, Length)})
    else :
        Header.update({'Range':'Bytes=%s-%s' % (start, start+1048575)})
    Request = urllib2.Request(DownLoadUrl, headers=Header)
    Request.getmethod = method
    Response = urllib2.urlopen(Request)
    f.write(Response.read())


f = open('/tmp/'+DownLoadUrl.split('/')[-1], 'wb')
map(openURL, LenList)
f.close()
