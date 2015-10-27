#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 9:55:10
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import urllib
import urllib2

url = 'http://127.0.0.1:8888/'
values = {
    'name': 'PC',
    'location': '51reboot',
    'language': 'Python'
}
data = urllib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
the_page = response.read()
