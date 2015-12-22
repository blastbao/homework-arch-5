#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: rpc_client.py
@time: 2015/12/21 10:22
"""

import sys,os
import subprocess
import pdb
sys.path.insert(1,os.path.join(sys.path[0],'..'))
from nbNet.nbNet_with_pipe import nbNet
pipe = {}
if __name__ == '__main__':
    def  logic(fd,raw):
        raw = raw.split("||")
        cmd = raw[0]
        # user = raw[1]
        # print cmd
        chilld = subprocess.Popen(cmd,stdin = fd, stdout = fd, stderr =fd, shell = True)
        return chilld
    runD = nbNet('0.0.0.0',1119,logic)
    runD.run()