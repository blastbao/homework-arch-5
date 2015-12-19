import zerorpc
import time
import os
from crypt import *
import sys,time

class HelloRPC(object):
    def hello(self, name):
        ret = "Hello, %s" % name
        #ret_str = "Resule  %s" ret
        #return "Hello, %s" % name
        return encrypt(ret)

s = zerorpc.Server(HelloRPC())
s.bind("tcp://0.0.0.0:4242")
s.run()
