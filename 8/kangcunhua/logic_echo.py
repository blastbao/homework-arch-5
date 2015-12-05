#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-11-29 14:33:49
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-11-29 14:41:08

import sys
import os
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet import nbNet

if __name__ == '__main__':
    def logic_echo(d_in):
        print d_in
        return 'OK'

    echo = nbNet('0.0.0.0', 9099, logic_echo)
    echo.run()
