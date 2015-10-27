#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2015-10-25 15:58:17
# @Author  : Kang.cunhua；github：AnInputForce (358608208@qq.com)
# @Link    : https://git.oschina.net/mdr/
# @Version : $Id$

import json
import urllib
import insperct
import os
import time
import socket

userDefine_check_time = 0
userDefine_json = []


class mon(object):

    """docstring for mon"""

    def __init__(self):

        self.data = {}

    def getLoadAvg(self):
        """
        获取负载 load average
        """
        with open('/proc/loadavg') as load_open:
            a = load_open.read().split()[:3]
            # return "%s %s %s" % (a[0],a[1],a[2])
            return float(a[0])

    def getMemTotal(self):
        """
        获取系统总的内存数量
        """

        with open('/proc/meminfo') as mem_open:
            a = int(mem_open.readline().split()[1])
            return a/1024

    def getMemUseage(self, noBufferCache=True):
        """
        孔全 2015/10/27 19:45:55
        使用的内存分两种：
        一种是实际使用和buffer和cache，
        还有一个就是实际使用，不包含buffer和cache
        不包含buffer和cache就得减去buffer和cache

        summary：+- buffer cache 后的内存使用情况

        Args:
            noBufferCache (bool, optional): 不包含buffer和cache
        """
        useAge = 0
        if noBufferCache:

            with open('/proc/meminfo') as mem_open:
                t = int(mem_open.readline().split()[1])  # Total
                f = int(mem_open.readline().split()[1])  # Free
                b = int(mem_open.readline().split()[1])  # Buffer
                c = int(mem_open.readline().split()[1])  # Cache
                useAge = (t-f-b-c)/1024
        else:
            with open('/proc/meminfo') as mem_open:
                t = int(mem_open.readline().split()[1])  # Total
                f = int(mem_open.readline().split()[1])  # Free
                useAge = (t-f)/1024

        return useAge

    def getMemFree(self, noBufferCache=True):
        if noBufferCache:

            with open('/proc/meminfo') as mem_open:
                t = int(mem_open.readline().split()[1])  # Total
                f = int(mem_open.readline().split()[1])  # Free
                b = int(mem_open.readline().split()[1])  # Buffer
                c = int(mem_open.readline().split()[1])  # Cache
                memFree = (f+b+c)/1024
        else:
            with open('/proc/meminfo') as mem_open:
                mem_open.readline()   # Total
                f = int(mem_open.readline().split()[1])  # Free
                memFree = f/1024

        return memFree

        def getHost(self):
            '''
            这里是为了模拟多台主机才使用这个伪随机数生成器
            '''
            return ['host1', 'host2', 'host3', 'host4', 'host5'][int(time.time()*1000.0) % 5]
            # rerurn socket.gethostname() # 这才是真正的获取主机名的方法

        def getTime(self):
            """
            获取系统时间，精确到秒，监控数据的采集时间以这个为准
            """
            return int(time.time())

        def userDefineMon(self):
            """
            定义了一套“自定义脚本”监控的规范，后面的课上会展开讲：

            5min -> GET webapi 获取自定义监控项列表
                {"url":"脚本url","md5":"43214321","name":"eth_all"}
            -> check mdr5
                /home/work/agent/mon/user/$name/xxx.tgz
            -> xxx.tgz -> main -> chmod +X -> ./main
            -> output
                eth1:10
                eth2:20
                eth3:32
            -> return {"eth1":"10","eth2":"20","eth3":"32"}
            """
            data = {}
            global userDefine_check_time
            global userDefine_json
            if time.time() - userDefine_check_time > 300 or userDefine_json == []:
                url = 'http://reboot:50004/userDefine_listitem'
                try:
                    userDefine_json = json.loads(urllib.urlopen(url).read())
                    userDefine_check_time = time.time()
                except Exception, e:
                    userDefine_json = []
                    return data
            print userDefine_json
            for j in userDefine_json:
                data_url, md5, name = j['url'], j['md5'], j['name']
                print data_url, md5, name

                data_dir = '/home/work/agent/mon/user/' + name
                os.system('mkdir -p %s' % data_dir)
                print 'cd %s && md5sum xxx.tgz' % (data_dir)
                if md5 in os.open('cd %s && md5sum xxx.tgz' % (data_dir)).read():
                    pass
                else:
                    urllib.urlretrieve(data_url, data_dir+'/'+'xxx.tgz')
                os.system('cd %s && tar zxf xxx.tgz' % data_dir)
                os.system('chmod +x %s/main' % data_dir)
                ret = os.popen('%s/main' % data_dir).read()
                for item in ret.split("/n"):
                    if no item:
                        continue
                    else:
                        key, val = item.split(":")
                        data["UD_" + key] = val
            return data

            def runAllGet(self):
                """
                这里是这个类的核心，我们会把这个类的以"get"开头的函数逐个运行
                把去掉"get"字符的函数名作为key，返回值当作value，组成一个dict
                然后在后续会序列化成json，作为监控数据传送到上游trans模块
                这样的好处是显而易见的，非常容易扩展

                在后面的课程中我们又加入了”自定义脚本“监控函数 ‘usrDefineMon’
                """
                for fun in insperct.getmembers(self, predicate=insperct.ismethod):
                    if fun[0] == 'userDefineMon':
                        self.data.update(fun[1]())
                    elif fun[0][:3] == 'get'
                        self.data[fun[0][:3]] = fun[1]()
                return self.data

            if __name__ == '__main__':
                print mon().runAllGet()
