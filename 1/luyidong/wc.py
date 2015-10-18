#!/usr/bin/python
#date: 2015-10-17

import sys
import string

f = sys.argv[1]
files = open(f,'rb')
dict = {}

while True:
        lines = files.read(4096)
        word = string.split(lines)
        '''
        Replace special characters
        '''
        if not lines:
                break
        for w in word:
                try:
                        dict[w] += 1
                        pass
                except KeyError:
                        dict[w] = 1
stat=[]
stat = dict.values()
#stat=dict.items()
b = sum(stat)
print b
files.close()
