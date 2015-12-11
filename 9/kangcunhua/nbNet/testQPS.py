#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-12-11 15:53:27
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-12-11 16:18:42
import socket
import sys
import os
import time
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet.nbNetFramework import nbNet


class MyQPSServer(object):
    """docstring for MyQPSServer"""

    def __init__(self, arg):
        super(MyQPSServer, self).__init__()
        self.counter = arg

    def logic(self, d_in):
        """[summary]
        这个是我们测试QPS的“业务逻辑”，做的事情就是每传输100K数据，打印对应的时间
        [description]

        Arguments:
            d_in {[type]} -- [description]：发送的格式化数据
        """
        self.counter += 1
        # 当计数器每次达到10万，打印出响应的时间；
        if self.counter % 100000 == 0:
            print self.counter, time.time()
        return("a")


if __name__ == '__main__':

    # 初始化计数器为0
    qpsserver = MyQPSServer(0)

    # 监听在0.0.0.0:9076
    reverseD = nbNet('0.0.0.0', 60006, qpsserver.logic)
    # 状态机开始运行，除非被kill，否则永不退出
    reverseD.run()
