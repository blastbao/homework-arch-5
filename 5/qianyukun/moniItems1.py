#!/usr/bin/env python
#coding=utf-8
import time
from timing import timeout
class mon:
    #@timeout(3)
    def runAllGet(self):
        time.sleep(10)
        return int(time.time())
if __name__ == "__main__":
    print mon().runAllGet()