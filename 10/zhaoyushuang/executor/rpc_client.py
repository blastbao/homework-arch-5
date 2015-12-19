#!/usr/bin/env python
#coding=utf-8

import zerorpc
import os,sys 
import crypt

def rpc_call(host):
    c=zerorpc.Client()
    c.connect("tcp://%s" % host)
    get_str=c.hello("hostname")
#    print get_str
    print crypt.decrypt(get_str)
    
if __name__=="__main__":
    rpc_call("127.0.0.1:9090")
