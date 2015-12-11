#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-12-06 14:19:45
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-12-11 16:03:21

import socket
import sys
import os

HOST = '127.0.0.1'
PORT = 60006
CNT = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

cmd = sys.argv[1]
data = "%010d%s" % (len(cmd), cmd)
while True:
    s.send(data * CNT)
    s.recv(len(data) * CNT)
    # for i in xrange(CNT):
    #    buf = s.recv(len(data))
