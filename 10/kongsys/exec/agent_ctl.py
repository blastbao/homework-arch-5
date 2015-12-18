#!/usr/bin/env python
# -*- coding: utf-8 -*-
import zerorpc
import os, sys
import conf
from crypt import *

from multiprocessing import Pool

pkg = sys.argv[1]
deploy_path = sys.argv[2]
host_l = ["%s:%d" % (h.strip(), conf.exec_port) for h in sys.argv[3].split(',')]

#agent_ctl.py module_name path host_list(',')
#send json to aget {"pkgname": "package_name", "path":"deploy_path"} in host list 

def deploy_call(host):
    c = zerorpc.Client()
    c.connect("tcp://%s" % host)
    ret = c.deploy(pkg, deploy_path)
    print(ret)

def rpc_call(host):
    c = zerorpc.Client()
    c.connect("tcp://%s" % (host))
    get_str = c.hello('hostname')
    print decrypt(get_str)

if __name__ == '__main__':
    deploy_call(host_l[0])
