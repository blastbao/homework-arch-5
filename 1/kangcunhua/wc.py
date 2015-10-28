#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-21 20:53:47
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$
"""Summary

Attributes:
    fileName (str): 接收命令行参数的文件名
    wordsCount (int): 计数器，统计文本文件共计多少英文单词

discription:
    # 统计某50G大小的英文文本中，单词的总数
    # 提示：
    # 1.文本可能不会换行；
    # 2.可以分段读取，累计单词数；
    # 3.如果开始为空格，则单词总数不变；否则单词总数-1；
    # author：kang.cunhua
    # update：2015.10.17 18:00 调试通过：)
"""


import re
import sys
import os


if not len(sys.argv) > 1:
    print '没有检测到文件名！请核对。'.decode("UTF-8")
    print '调用格式 python wc.py fileName'.decode("UTF-8")
    os._exit(0)

fileName = sys.argv[1]

# if not os.path.isfile(fileName):
#     try:
#         sys.exit(0)
#     except:
#         print '文件不存在！请核对。'
#     finally:
#         print '调用格式 python wc.py fileName'

if not os.path.isfile(fileName):
    print '文件不存在！请核对。'.decode("UTF-8")
    print '调用格式 python wc.py fileName'.decode("UTF-8")
    os._exit(0)


#fileName = 'WillamShakespeare.txt'
wordsCount = 0

with open(fileName, 'r') as f:
    # 文件不以空格开头
    chunk = f.read(1000)
    if chunk[0] == ' ':
        wordsCount += 1
    # 按块处理文件，累加计数器
    while chunk:
        # if not chunk:break
        if chunk[0] == ' ':
            wordsCount -= 1
        match = re.findall(r'[^a-zA-Z0-9]+', chunk)  # 只要英文单词，删掉其他字符

        for i in match:
            chunk = chunk.replace(i, ' ')
        chunk_list = chunk.split()
        wordsCount += len(chunk_list)
        chunk = f.read(1000)
print 'words_count is', wordsCount
# note
# 不要把print放while循环里，否则处理时间长十倍
# [Finished in 103.1s]

# buffer = 1000
# words_count is 1650501
# [Finished in 9.3s]
# 把print放while循环外；
#
# output:
# D:\PythonHome\homework-arch-5\1\kangcunhua>python wc.py
# 没有检测到文件名！请核对。
# 调用格式 python wc.py fileName

# D:\PythonHome\homework-arch-5\1\kangcunhua>python wc.py 222
# 文件不存在！请核对。
# 调用格式 python wc.py fileName

# D:\PythonHome\homework-arch-5\1\kangcunhua>python wc.py WillamShakespeare.txt
# words_count is 1650501
#
