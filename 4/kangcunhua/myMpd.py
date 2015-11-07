#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-05 21:30:03
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$
'''
PC老师<auxtenwpc@gmail.com> 16:23:44 
明天上课了，大家努力做作业，人总是要逼自己一把
嗯，对，今天作业不写，明天课听起来就没有感觉
写程序很重要的一个能力就是debug，这个必须要自己动手才能收获
写个多线程多连接下载工具 下载QQ安装包
大家每次花一小时努力一下，就能在能力上超过好几百人
有我给大家指路，大家能少走很多弯路，一定好抓住机会
'''

import re
import urllib2
from multiprocessing.dummy import Pool

downloadUrl = 'http://dldir1.qq.com/qqfile/qq/QQ7.7/16096/QQ7.7.exe'
# 调试url ，目标文件小，下载快，写入快，方便调试；
# 最开始用的是豆瓣害羞组的URL，但是豆瓣无论你请求head的range是多少，都会给你返回整个html
downloadUrl2 = 'http://www.python.org/'
proNum = 5


def getFileSize(downloadUrl):
    user_agent = 'Mozilla/8.0 (compatible;MSIE 8.0;Windows NT)'
    headers = {'User-Agent': user_agent}

    req = urllib2.Request(
        downloadUrl, headers=headers)

    req.get_method = lambda: 'HEAD'
    response = urllib2.urlopen(req)
    fileSize = response.headers.get('Content-Length', 0)

    print '要下载的文件大小为： ', fileSize
    return fileSize

# 测试getFileSize函数
# getFileSize(downloadUrl)
# getFileSize(downloadUrl2)


def getRangeList(proNum=5):
    '''
    这段代码基本是copy了陶力童鞋的算法
    仔细研读了代码之后，认为有缺陷，自己还常识修复了一下，
    最后发现是自己想多了。陶力童鞋写的还是很严谨的。
    见注释掉的 if int(fileSize) % proNum:那两行
    '''
    fileSize = getFileSize(downloadUrl)
    print fileSize
    rangeList = []
    se = ()
    blockNum = int(fileSize) / proNum
    for i in xrange(proNum):
        if i + 1 == proNum:
            end = int(fileSize) - 1
        else:
            end = int((i + 1) * blockNum - 1)
        se = (i * blockNum, end)
        rangeList.append(se)
    # if int(fileSize) % proNum:
    #      rangeList.append([(proNum + 1) * blockNum, int(fileSize)])
    return rangeList
# 测试getRangeList()
print 'range list is :\n', getRangeList()
# range list is :[(0, 11024112),(11024113, 22048225),(22048226,
# 33072338),(33072339, 44096451),(44096452, 55120567)]


def getStartList():

    fileSize = getFileSize(downloadUrl)
    print fileSize
    startList = []
    blockNum = int(fileSize) / proNum
    for i in xrange(proNum):
        startList.append(i * blockNum)

    return startList

print 'getStartList():', getStartList()


def getResponseBlock((startNum, endNum)):
    user_agent = 'Mozilla/8.0 (compatible;MSIE 8.0;Windows NT)'
    # print '调用输出为：(',startNum,'-',')','\n''\n'
    # print '调用输出为：(''-', endNum,')','\n''\n'
    # print '调用输出为：\n',ll[0], ll(1),'\n''\n'
    s = "bytes=%d-%d" % (startNum, endNum)
    # print 's=', s,'\n''\n'
    headers = {'User-Agent': user_agent, 'Range': s}
    req = urllib2.Request(downloadUrl, '', headers=headers)
    res = urllib2.urlopen(req)

    # print 'filename:',downloadUrl2.split("/")[-1]
    print '下载内容为：\n ', res
    return res
# 测试 getResponseBlock函数
#  "%3s" % temp.encode('hex')
# print '下载内容为：\n %3s', getResponseBlock().read().encode('hex')


def getRequestsList():

    reqList = []
    pool = Pool(proNum)
    reqList = pool.map(getResponseBlock, getRangeList())
    # reqList = pool.map(getResponseBlock, zip([0, 11024113, 22048226, 33072339, 44096452], [
    #                    11024112, 22048225, 33072338, 44096451, 55120567]))
    # [0,11024113,22048226,33072339,44096452], [11024112,22048225,33072338,44096451, 55120567])
    # [(0, 11024112),(11024113, 22048225),(22048226, 33072338),(33072339, 44096451),(44096452, 55120567)])
    # [0,11024113,22048226,33072339,44096452], [11024112,22048225,33072338,44096451, 55120567])
    pool.close()
    pool.join()
    return reqList

# print 'getreqlist:\n', getRequestsList(5)


def writeToFile((res, start)):

    with file('qq.exe', "wb") as f:
        f.seek(start)
        f.write(res.read())
# print '测试写入文件：\n',writeToFile(getResponseBlock(downloadUrl))

pool = Pool(proNum)
reqList = pool.map(writeToFile, zip(getRequestsList(), getStartList()))

# ll = [[0, 11024113, 22048226, 33072339, 44096452], [
#     11024112, 22048225, 33072338, 44096451, 55120567]]
# reqList = pool.map(writeToFile, zip(getRequestsList(), ll[0]))
# [0,11024113,22048226,33072339,44096452], [11024112,22048225,33072338,44096451, 55120567])
# [(0, 11024112),(11024113, 22048225),(22048226, 33072338),(33072339, 44096451),(44096452, 55120567)])
# [0,11024113,22048226,33072339,44096452], [11024112,22048225,33072338,44096451, 55120567])
# getRangeList(proNum))
pool.close()
pool.join()


# output：参考，http://blog.csdn.net/cctt_1/article/details/4512103
# socket.error: [Errno 10054]
# 而我最后发现是 req = urllib2.Request(downloadUrl, '', headers=headers)，
# 如果中间不用''占位的话，参数怎么写都会报这个10054错误。
# 学艺不精，记得老师说是可以不写的，只需要用参数名=参数的形式即可传参
# 周末请教下PC老师
#

# output： 参考，http://bbs.chinaunix.net/thread-1856521-1-1.html
# getreqlist:
# Traceback (most recent call last):
#   File "D:\PythonHome\Python-arch-5-Lesson\Lession04\mympd.py", line 85, in <module>
#     print 'getreqlist:\n',getRequestsList(5)
#   File "D:\PythonHome\Python-arch-5-Lesson\Lession04\mympd.py", line 76, in getRequestsList
#     reqList = pool.map(getResponseBlock,[0,11024113,22048226,33072339,44096452], [11024112,22048225,33072338,44096451, 55120567])
#   File "C:\Python27\lib\multiprocessing\pool.py", line 251, in map
#     return self.map_async(func, iterable, chunksize).get()
#   File "C:\Python27\lib\multiprocessing\pool.py", line 314, in map_async
#     result = MapResult(self._cache, chunksize, len(iterable), callback)
#   File "C:\Python27\lib\multiprocessing\pool.py", line 599, in __init__
#     self._number_left = length//chunksize + bool(length % chunksize)
# TypeError: unsupported operand type(s) for //: 'int' and 'list'
# [Finished in 0.7s with exit code 1]


# output：sucess 按照调试url调试成功的输出
# range list is :
# 要下载的文件大小为：  46995
# 46995
# [(0, 9398), (9399, 18797), (18798, 28196), (28197, 37595), (37596, 46994)]
# getStartList(): 要下载的文件大小为：  46995
# 46995
# [0, 9399, 18798, 28197, 37596]
# 要下载的文件大小为：  46995
# 46995
# 下载内容为：
#   <addinfourl at 33998128 whose fp = <socket._fileobject object at 0x01FB19F0>>
# 下载内容为：
#   <addinfourl at 33922664 whose fp = <socket._fileobject object at 0x01FB1AF0>>
# 下载内容为：
#   <addinfourl at 33265904 whose fp = <socket._fileobject object at 0x01FB1BB0>>
# 下载内容为：
#   <addinfourl at 33920544 whose fp = <socket._fileobject object at 0x01FB1C70>>
# 下载内容为：
#   <addinfourl at 33926800 whose fp = <socket._fileobject object at 0x01FB1CF0>>
# 要下载的文件大小为：  46995
# 46995
# [Finished in 17.0s]
