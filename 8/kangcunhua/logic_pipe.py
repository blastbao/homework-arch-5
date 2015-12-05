#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-11-29 15:10:28
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-11-29 17:22:32

import sys
import os
import socket
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet import nbNet

if __name__ == '__main__':

    def logic_pipe(d_in):
        HOST = '127.0.0.1'
        PORT = 9099
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        s.send('%05d%s' % (len(d_in), d_in))
        d_response = s.recv(7)

        return d_response[5:]

    pipe = nbNet('0.0.0.0', 9098, logic_pipe)
    pipe.run()


# output
#
# 第一个终端启动pipe server
# >>study:
#     /home / kang / arch - 5 / lession08 > python logic_pipe.py
# 第二个终端启动echo server
# >>study:/home/kang/arch-5/lession08>python logic_echo.py
# kangc
# 第三个终端连接pipe server
# >>study:
#     /home / kang > telnet 127.0.0.1 9098
# Trying 127.0.0.1...
# Connected to 127.0.0.1.
# Escape character is '^]'.
# 00005kangc
# 00002OK
