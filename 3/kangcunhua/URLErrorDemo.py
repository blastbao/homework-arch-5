#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 10:15:31
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

from urllib2 import Request, urlopen, URLError, HTTPError
req = Request('http://51reboot.com/ada')
try:
    response = urlopen(req)
except HTTPError, e:
    print 'The server couldn\'t fulfill the request.'
    print 'Error code: ', e.code
except URLError, e:
    print 'We failed to reach a server'
    print 'Reasoon: ', e.reason

finally:
    print 'Game over!'

# output,http://51reboot.com
# Game over!
# [Finished in 1.0s]

# output,http: // 51reboot.com/ada
# The server couldn't fulfill the request.
# Error code:  404
# Game over!
# [Finished in 0.6s]

# output,http://52reboot.com
# We failed to reach a server
# Reasoon:  [Errno 11004] getaddrinfo failed
# Game over!
# [Finished in 3.4s]
shed in 3.4s]
s]
