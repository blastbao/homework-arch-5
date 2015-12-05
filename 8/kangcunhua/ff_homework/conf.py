#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-11-29 17:17:21
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-11-30 23:51:16
"""
[监控项,操作符,阀值,邮件,累计N次就报警，间隔时间内最多报警M次, 间隔时间]
"""
ff_conf = [
    ['MemUsage', '>', 1863, 'alarm@qq.com', 3, 3, 60],
    ['LoadAvg', '>', 0.2, 'pc@qq.com', 1, 2, 20],
]
