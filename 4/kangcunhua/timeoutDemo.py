#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-11-01 10:05:50
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import signal
import functools  # 下面会用到这两个库


class TimeoutError(Exception):
    pass  # 定义一个Exception，后面超时抛出


def timeout(seconds, error_message='Function call timed out'):

    def decorated(func):
        def _handle_timeout(signum, frame):
            raise TimeoutError(error_message)

        def wrapper(*args, **kwargs):
            # 定义闹钟
            signal.signal(signal.SIGALRM, _handle_timeout)
            signal.alarm(seconds)
            try:
                result = func(*args, **kwargs)
            finally:
                # 删除闹钟
                signal.alarm(0)
            return result
        return functools.wraps(func)(wrapper)
    return decorated


@timeout(5)
def slowfunc(sleep_time):
    import time
    time.sleep(sleep_time)  # 这个函数就是休眠 sleep_time秒
    print 'sleep_time ', sleep_time, '秒被执行啦！'

slowfunc(3)  # sleep 3秒，正常返回，没有异常
slowfunc(10)  # 被终止

# output: 必须在linux下运行，windows不支持signal.SIGALRM信号
# >>study:/home/kang/arch-5/lession04>rz -y
# z waiting to receive.**B0100000023be50
# >>study:/home/kang/arch-5/lession04>python timeoutDemo.py
# sleep_time  3 秒被执行啦！
# Traceback (most recent call last):
#   File "timeoutDemo.py", line 43, in <module>
#     slowfunc(10)  # 被终止
#   File "timeoutDemo.py", line 27, in wrapper
#     result = func(*args, **kwargs)
#   File "timeoutDemo.py", line 39, in slowfunc
#     time.sleep(sleep_time)  # 这个函数就是休眠 sleep_time秒
#   File "timeoutDemo.py", line 20, in _handle_timeout
#     raise TimeoutError(error_message)
# __main__.TimeoutError: Function call timed out
