#!/usr/bin/env python
#coding=utf-8

import zerorpc
import gipc
import os 
import time 
import sys
import crypt

sys.path.insert(1, os.path.join(sys.path[0], '..'))

from nbNet.daemon import Daemon
#from collector.agent import startTh 


class HelloRPC(object):
    def hello(self,name):
        print "exec %s %s " %(time.strftime("%Y-%m-%d %h-%m-%s",time.localtime(time.time())) , name)
        
        retult=os.popen(name).read()
        
        ret_str="Result %s \n %s " %(time.strftime("%Y-%m-%d %h-%m-%s",time.localtime(time.time())) , retult)
        
#        return ret_str
        return crypt.encrypt(ret_str)


def Executor(name):
    print "Hello : %s " % name
    s=zerorpc.Server(HelloRPC())
    s.bind("tcp://127.0.0.1:9090")
    s.run()

class MyDaemon(Daemon):
    def run(self):
        e=gipc.start_process(target=Executor,args=('Execute',))
        e.join()

if __name__=="__main__":
    daemon = MyDaemon('/tmp/daemon-9090.pid')
    daemon.run()
