#!/usr/bin/env python
#encoding:utf-8
import socket, sys, os
from multiprocessing.dummy import Pool as ThreadPool
def handel(str):
    HOST = ' 127.0.0.1'
    PORT = 333
    CNT = int( sys.argv[2] )
    s = socket. socket( socket.AF_INET, socket.SOCK_STREAM)
    s. connect( ( HOST, PORT) )
    cmd = str
    data = "%010d%s"%( len( cmd) , cmd)
    while True:
        s.send( data * CNT)
        s.recv( len( data) * CNT)

if __name__ == '__main__':
    real_num = int(sys.argv[1])      #get work thread from user input
    pool = ThreadPool(real_num)
    s = ord('a')
    word_list = [0]*real_num
    for i in xrange(real_num):
        s +=1
        word_list[i] = chr(s)
    pool.map(handel,word_list)
    pool.join()