#!/usr/bin/env python
#coding=utf-8

import json
import urllib
import inspect
import os, time, socket

class getItems:
    def __init__(self):
        self.data = {}
    
    def getLoadAvg(self):
        with open('/proc/loadavg') as load_open:
            a = load_open.read().split()[:3]
            return float(a[0])
    
    def MemInfo(self, memUsage = False, memFree = False, noBufferCache = True):
        if noBufferCache:
            with open('/proc/meminfo') as mem_open:
                Total = int(mem_open.readline().split()[1])
                Free = int(mem_open.readline().split()[1])
                Buffer = int(mem_open.readline().split()[1])
                Cache = int(mem_open.readline().split()[1])
                if memUsage:
                    return (Total - Free - Buffer - Cache) / 1024
                else:
                    return (Free + Buffer + Cache) / 1024
        else:
            with open('/proc/meminfo') as mem_open:
                Total = int(mem_open.readline().split()[1])
                Free = int(mem_open.readline().split()[1])
                if memUsage:
                    return (Total - Free)  / 1024
                else:
                    return Free / 1024
    def getMemUsage(self):
        return self.MemInfo(memUsage = True)

    def getMemFree(self):
        return self.MemInfo(memFree = True)

    def getHost(self):
        #return ['host1', 'host2', 'host3', 'host4'][int(time.time() * 1000.0) % 5]
        return socket.gethostname()

    def getTime(self):
        return int(time.time())

    def runAllGet(self):
        for fun in inspect.getmembers(self, predicate = inspect.ismethod):
            if fun[0] == "userDefineMon":
                self.data.update(fun[1]())
            elif fun[0][:3] == 'get':
                self.data[fun[0][3:]] = fun[1]()
        return self.data
if __name__ == '__main__':
    print getItems().runAllGet()
