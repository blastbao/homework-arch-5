#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 15:58:17
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import json
import urllib
import insperct
import os
import time
import socket

userDefine_check_time = 0
userDefine_json = []


class mon(object):

    """docstring for mon"""

    def __init__(self):

        self.data = {}

    def getLoadAvg(self):
        with open('/proc/loadavg') as load_open:
            a = load_open
