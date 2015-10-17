#!/usr/bin/env python
#coding=utf8
#作业: 统计一个文件中所有单词数量

import sys

with  open(sys.argv[1],'r') as f:
    start = 0
    s =  f.read(10)
    while True:
        if len(s) == 0:
            print start
            break

        while True:
            if not s[-1].isspace():
                s = s + f.read(1)
            else:
                start += len(s.strip().split())
                break











            
            