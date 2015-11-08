#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-01 14:39:54
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import urllib2
import urllib
from multiprocessing.dummy import Pool as ThreadPool
urls = [
    'http://www.baidu.com/s?wd=reboot',
    'http://www.baidu.com/s?wd=reboot+python',
    'http://www.baidu.com/s?wd=reboot+devops',
    'http://www.baidu.com/s?wd=reboot+ops',
    'http://www.baidu.com/s?wd=reboot+gko_pool'
]

pool = ThreadPool(4)

#results = pool.map(urllib2.urlopen, urls)
results = pool.map(urllib.urlretrieve, urls)

print results
pool.close()
pool.join()


# output：urlopen
# [<addinfourl at 33233616 whose fp = <socket._fileobject object at 0x01FB90F0>>, <addinfourl at 33280288 whose fp = <socket._fileobject object at 0x01FB9470>>, <addinfourl at 33232896 whose fp = <socket._fileobject object at 0x01F96EF0>>, <addinfourl at 33234016 whose fp = <socket._fileobject object at 0x01FB9230>>, <addinfourl at 33234536 whose fp = <socket._fileobject object at 0x01FB9370>>]
# [Finished in 1.0s]
