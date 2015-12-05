#!/usr/bin/evn python
#coding=utf-8
import sys,os,socket

sys.path.insert(1,os.path.join(sys.path[0],'..'))

from nbNetFramework import nbNet

def echo_logic(input):
    print input
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(("0.0.0.0", 9090))
    sock.send("%010d%s" % (len(input),input))
    output=sock.recv( 10+len(input) )
    print output
    return output[10:]



if __name__=='__main__': 
    app=nbNet('0.0.0.0',9091,echo_logic)
    app.run()


