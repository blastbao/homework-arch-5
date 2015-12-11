#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-12-06 14:19:45
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-12-12 02:17:31

import socket
import sys
import os
from multiprocessing.dummy import Pool


def loadrun((data, recvlen)):

    HOST = '127.0.0.1'
    PORT = 60006

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    # data = "%010d%s" % (len(content), content)
    while True:
        s.send(data)
        s.recv(recvlen)

if __name__ == '__main__':
    print '调用格式：python loadrun.py 最大线程 集中发送条数'
    threadnum = int(sys.argv[1])
    CNT = int(sys.argv[2])

    pool = Pool(threadnum)

    data = ["%010d%s" % (1, 'a') * CNT]
    recvlen = len(data[0])

    data = data * threadnum
    recvlen = [recvlen] * threadnum

    pool.map(loadrun, zip(data, recvlen))
    pool.join()
