import zerorpc
import os,sys
from crypt import *

c = zerorpc.Client()
c.connect("tcp://127.0.0.1:4242")
#print c.hello("RPC")
get_str = c.hello("RPC")
print decrypt(get_str)
