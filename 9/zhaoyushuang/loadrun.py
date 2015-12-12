#!/usr/bin/python
#encoding=utf-8

import socket,sys,os 

address=('127.0.0.1',9090)
cnt=int(sys.argv[2])

sock=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect(address)
cmd=sys.argv[1]
data="%010d%s" %(len(cmd),cmd)

while True:
    sock.send(data*cnt)
    sock.recv(len(data)*cnt)