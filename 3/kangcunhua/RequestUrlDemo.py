#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 09:31:48
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import urllib2
response = urllib2.urlopen('http://51reboot.com/')  # urlopen()返回的是一个句柄
html = response.read()  # 需要进行读取
print html

# output ,如果不加http://
# ValueError: unknown url type: 51reboot.com/
# [Finished in 1.6s with exit code 1]

req = urllib2.Request('http://Python.org/')
response = urllib2.urlopen(req)
html = response.read()
print html
