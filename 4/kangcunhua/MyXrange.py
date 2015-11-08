#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-01 14:04:14
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$


class xxrange:

    """docstring for xxrange"""

    def __init__(self, n):
        # super(xxrange, self).__init__()
        self.n = n

    def __iter_(self):
        n = self.n
        while n:
            n -= 1
            yield n
for i in xxrange(5):
    print i
