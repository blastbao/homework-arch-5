#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: agent_ctl.py
@time: 2015/12/16 16:06
"""
import zerorpc
import os,sys
import conf
from crypt import *

from multiprocessing import Pool

pkg = sys.argv[1]
deploy_path = sys.argv[2]
host_l = ["%s:%d"%(h.strip(),conf.exec_port) for h in sys.argv[3].split(',')]

def deploy_call(host):
    c = zerorpc.Client()
    c.connect("tcp://%s"%(host))
    # ret = c.deploy(pkg,deploy_path)
    ret = c.hello('ls')

def rpc_call(host):
    c = zerorpc.Client()
    c.connect("tcp://%s"%(host))
    get_str = c.test()
    print decrypt(get_str)

if __name__ == '__main__':
    rpc_call(host_l[0])





