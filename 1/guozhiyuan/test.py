#!/usr/bin/env python
#coding=utf8
#作业: 统计一个文件中所有单词数量

import sys

with  open(sys.argv[1],'r') as f:
    start = 0
    s =  f.read(1024)
    while True:
        if s == '':
            print start
            break

        while True:
            if not s[-1].isspace():
                s = s + f.read(1)
            else:
                start += len(s.strip().split())
                break











            
            
