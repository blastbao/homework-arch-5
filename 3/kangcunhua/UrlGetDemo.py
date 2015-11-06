#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 10:01:14
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import urllib
import urllib2

data = {}
data['name'] = 'PC'
data['location'] = '51reboot'
data['Python'] = 'Python'

url_values = urllib.urlencode(data)
print url_values  # 这里的顺序不一定

url = 'http://127.0.0.1:8888/'
full_url = url + '?' + url_values

data = urllib.urlopen(full_url)
