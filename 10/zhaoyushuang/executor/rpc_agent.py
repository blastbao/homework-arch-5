#!/usr/bin/env python
#coding=utf-8

import zerorpc
import os 
import time 
import crypt

class HelloRPC(object):
    def hello(self,name):
        print "exec %s %s " %(time.strftime("%Y-%m-%d %h-%m-%s",time.localtime(time.time())) , name)
        
        retult=os.popen(name).read()
        
        ret_str="Result %s \n %s " %(time.strftime("%Y-%m-%d %h-%m-%s",time.localtime(time.time())) , retult)
        
#        return ret_str
        return crypt.encrypt(ret_str)

if __name__=="__main__":
#     print 'hello %s ' % name
    s=zerorpc.Server(HelloRPC())
    s.bind("tcp://127.0.0.1:9090") 
    s.run()   
