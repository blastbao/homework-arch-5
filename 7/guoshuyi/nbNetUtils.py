#!/usr/bin/env python
# coding: utf-8
from daemon import Daemon
import socket
import select
import time
import pdb

DEBUG = False

from inspect import currentframe
def get_linenumber():
    """
    获取当前行号，方便debug日志数据定位问题
    """
    cf = currentframe()
    return str(cf.f_back.f_back.f_lineno)

def dbgPrint(msg):
    if DEBUG:
        print get_linenumber(), msg
