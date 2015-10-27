#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 10:39:10
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import urllib
import urllib2

url = 'http://weibo.com/u/auxten'
req = urllib2.Request(url)
response = urllib2.urlopen(req)

print "URL: ", url
print "After redirection:", response.geturl()

# URL:  http://weibo.com/u/auxten
# After redirection: http://passport.weibo.com/visitor/visitor?entry=miniblog&a=enter&url=http%3A%2F%2Fweibo.com%2Fu%2Fauxten&domain=.weibo.com&ua=php-sso_sdk_client-0.6.16&_rand=1445740969.4822
# [Finished in 1.9s]
