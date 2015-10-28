#!/usr/bin/env python
#_*_coding:utf8_*_

import fileinput
#导入fileinput模块用input方法里面bufsize来控制每次读取的字节数。
import sys
l1 = {}
for i in fileinput.input(sys.argv[1],bufsize=104857600):
    for n in i.lower().split( ):
        if n not in l1:
            l1[n] = 1
        else:
            l1[n] = l1[n] + 1
print l1