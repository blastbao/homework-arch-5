#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-01 11:51:46
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$


def test(*args, **dic):
    for arg in args:
        print arg
    for k, v in dic.iteritems():
        print k, ':', v

test("yes", 1, 2, me="mdr", where="北京")
# "yes",1,2传递给元组
# me="mdr",where="北京" 传递给字典

# output：
# yes
# 1
# 2
# me : mdr
# where : 北京
# [Finished in 0.8s]
