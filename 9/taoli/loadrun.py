#!/usr/bin/env python
#encoding:utf-8
import socket, sys, os
HOST = ' 127.0.0.1'
PORT = 333
CNT = int( sys.argv[2] )
s = socket. socket( socket.AF_INET, socket.SOCK_STREAM)
s. connect( ( HOST, PORT) )
cmd = sys.argv[1]
data = "%010d%s"%( len( cmd) , cmd)
# 不断的发送和接受뻟 pipeline模式
while True:
    s.send( data * CNT)
    s.recv( len( data) * CNT)
