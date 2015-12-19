#!/usr/bin/evn python
#coding=utf-8
import sys,os,socket

sys.path.insert(1,os.path.join(sys.path[0],'..'))

from nbNetFramework import nbNet

def echo_logic(input):
    print input
    return input

if __name__=='__main__':
    app=nbNet('0.0.0.0',9090,echo_logic)
    app.run()


