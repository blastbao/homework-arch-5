#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys, os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet.nbNetFramework import nbNet
import subprocess

if __name__ == '__main__':
    def logic(d_in, fd):
        return subprocess.Popen(d_in, stdout = fd, stderr = fd)
    reversdD = nbNet('0.0.0.0', 9079, logic)
    reversdD.run()
