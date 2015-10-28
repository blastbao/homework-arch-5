#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 13:13:03
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

"""Summary
    抓取指定url里的Intel的CPU型号
Attributes:
    html (TYPE): Description
    match (TYPE): Description
    response (TYPE): Description
"""
import re
import urllib2
response = urllib2.urlopen(
    'http://cpu.zol.com.cn/546/5465527.html?qq-pf-to=pcqq.group')
# urlopen()返回的是一个句柄
html = response.read()
# 需要进行读取
# print html
#
match = re.findall(r'i[3,5,7][-]\w{3,5}', html)

# print match
for i in xrange(0, len(match)):
    print match[i]

# output:
# i3-4150
# i5-6400
# i5-6500
# i5-4690K
# i5-6600K
# i5-6600K
# i7-4790K
# i5-6600K
# [Finished in 2.1s]
