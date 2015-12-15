#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet.nbNetFramework import nbNet
import subprocess

if __name__ == '__main__':
    def logic(sock_state, fd):
        print 'a'
        args = shlex.split(sock_state.buff_read)
        print 'A'
        try:
            print 'HAHA'
            sock_state.subp_obj = subprocess.Popen(args, stdout = fd, stderr = fd)
            sock_state.state = 'writeend'
            print 'haha'
        except Exception, msg:
            print msg
            os.write(fd, str(msg) + '\r\n\r\n')
            print "%r" % str(msg) + '\r\n\r\n'
            sock_state.state = "closing"
    reversdD = nbNet('0.0.0.0', 9079, logic)
    reversdD.run()
