#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-12-24 10:02:46
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-12-24 16:39:53
import sys
import os
import socket
import subprocess
import fcntl
import tempfile

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet.nbNetFramework import nbNet


if __name__ == '__main__':
    def logic(coming_sock_fd, d_in):
        out_temp = tempfile.SpooledTemporaryFile(bufsize=10 * 1000)
        fileno = out_temp.fileno()
        obj = subprocess.Popen(d_in, shell=True, stdout=fileno, stderr=fileno)
        obj.wait()
        out_temp.seek(0)
        callres = '%s %s %s %s' % ('==fd==', coming_sock_fd, '==fd==', out_temp.read())
        print '返回输出%010d%s' % (len(callres),  callres)
        # print '=========d_in start=========\n', d_in, '=========d_in end=========\n'
        return callres

    reverseD = nbNet('0.0.0.0', 9999, logic)
    reverseD.run()
