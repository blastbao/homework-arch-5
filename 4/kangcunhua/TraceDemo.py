#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-01 11:28:26
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import sys
import os
import linecache


def trace(f):
    def globaltrace(frame, why, arg):
        if why == "call":
            return localtrace
        return None

    def localtrace(frame, why, arg):
        if why == "line":
            # record the file name and line number of every trace
            filename = frame.f_code.co_filename
            lineno = frame.f_lineno
            bname = os.path.basename(filename)
            print "{}({}): {}".format(bname,
                                      lineno,
                                      linecache.getline(filename, lineno)),
        return localtrace

    def _f(*args, **kwds):
        sys.settrace(globaltrace)
        result = f(*args, **kwds)
        sys.settrace(None)
        return result
    return _f

# 调用举例


@trace
def xxx():
    print 1
    print 22
    print 333

xxx()  # 调用

# output：
# TraceDemo.py(42):     print 1
# 1
# TraceDemo.py(43):     print 22
# 22
# TraceDemo.py(44):     print 333
# 333
# [Finished in 0.5s]
