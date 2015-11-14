#!/usr/bin/env python
#coding=utf-8

import json
import urllib
import inspect
import os,time,socket

userDefine_check_time=0
userDefine_json=[]


class mon:
    def __init__(self):
        self.data={}

    def getLoadAvg(self):
        """ get load average 获取负载
        cat /proc/loadavg
        0.00 0.00 0.00 1/195 3457
        前三个分别是 1、5、15分钟内的平均进程数,
        第四个:分子是正在运行的进程数，分母是进程总数；
        第五个:最近运行的进程ID号。
        """
        with open('/proc/loadavg') as load_open:
            avgLoad=load_open.read().split()[:3]
            return float(avgLoad[0])
    
    def getMemTotal(self):
        """get memory total 获取系统的内存总量 
        cat /proc/meminfo
        MemTotal:        3924688 kB
        MemFree:          225572 kB
        Buffers:          244728 kB
        Cached:          2885748 kB
        SwapCached:        22460 kB
        Active:          2528980 kB
        Inactive:         823464 kB
        
        MemTotal: 所有可用RAM大小 （即物理内存减去一些预留位和内核的二进制代码大小）

        MemFree: LowFree与HighFree的总和

        Buffers: 用来给块设备做的缓冲大小（只记录文件系统的metadata以及 tracking in-flight pages，就是说 buffers是用来存储，目录里面有什么内容，权限等等。）

        Cached: 用来给文件做缓冲大小（直接用来记忆我们打开的文件）. 它不包括SwapCached

        SwapCached: 已经被交换出来的内存，但仍然被存放在swapfile中。用来在需要的时候很快的被替换而不需要再次打开I/O端口。

        Active: 最近经常被使用的内存，除非非常必要否则不会被移作他用.

        Inactive: 最近不经常被使用的内存，非常用可能被用于其他途径.
        
        """
        
        with open('/proc/meminfo') as mem_open:
            totalMem=int(mem_open.readline().split()[1])
            return totalMem/1024
        
    def getMemUsage(self,noBufferCache=True):
        """get memory usage 获取系统的内存使用 """
        if noBufferCache:
            """ 使用buffer cache 后的内存使用情况"""
            with open('/proc/meminfo') as mem_open:
                T=int(mem_open.readline().split()[1]) # total memory
                F=int(mem_open.readline().split()[1]) # free 
                B=int(mem_open.readline().split()[1]) # buffer 
                C=int(mem_open.readline().split()[1]) # cache
                return (T-F-B-C)/1024
        else:
            with open('/proc/meminfo') as mem_open:
                a=int(mem_open.readline().split()[1])-int(mem_open.readline().split()[1])
                return a/1024
                #T=int(mem_open.readline().split()[1])
                #F=int(mem_open.readline().split()[1])
                #return (T-F)/1024
            
    
    def getMemFree(self,noBufferCache=True):
        """get memory free 获取系统的内存空闲情况 """
        if noBufferCache:
            """ 使用buffer cache 后的内存使用情况"""
            with open('/proc/meminfo') as mem_open:
                T=int(mem_open.readline().split()[1])
                F=int(mem_open.readline().split()[1])
                B=int(mem_open.readline().split()[1])
                C=int(mem_open.readline().split()[1])
                return (F+B+C)/1024
        else:
            with open('/proc/meminfo') as mem_open:
                mem_open.readline()
                a=int(mem_open.readline().split()[1])
                return a/1024
        
    def getHost(self):
        #generate a random hostname to pretend a server.
        return ['host1','host2','host3','host4','host5'][int(time.time() * 1000.0) % 5] 
        # this is the real hostname 
        #return socket.gethostname()
    
    def getTime(self):
        return int(time.time())
    
    def userDefineMon(self):
        """定义规范 """
        
        """
        5min -> GET webapi 获取自定义监控项列表
            {"url":"脚本url","md5":"43214321","name":'eth_all'}
        -> check md5
            /home/work/agent/mon/user/$name/xxx.tgz
        -> xxx.tgz -> main -> chmod +x -> ./main
        -> output
            eth1:10
            eth2:20
            eth3:32
        -> return
            {"eth1":10,"eth2":20,"eth3":32}
        
        """
        
        data={}
        global userDefine_check_time
        global userDefine_json
        if time.time()-userDefine_check_time>300 or userDefine_json==[]:
            url='http://reboot:50004/userdefine_listitem'                  #???
            try:
                #json.loads 
                userDefine_json=json.loads(urllib.urlopen(url).read())
                userDefine_check_time=time.time()
            except:
                userDefine_json=[]
                return data
        print userDefine_json
        for j in userDefine_json:
            data_url,md5,name=j['data_url'],j['md5'],j['name']
            print data_url,md5,name 
        
            data_dir='/home/xxx/agent/mon/user/'+name 
            os.system('mkdir -p %s' % data_dir)
            print 'cd %s && md5sum xxxx.tgz' % data_dir   
            
            #在网络传输时，我们校验源文件获得其md5sum，传输完毕后，校验其目标文件，并对比如果源文件和目标文件md5 一致的话，则表示文件传输无异常。否则说明文件在传输过程中未正确传输。
            if md5 in os.popen('cd %s && md5sum xxxx.tgz' % (data_dir) ).read():
                pass 
            else:
                #download remote url's file to local file 
                urllib.urlretrieve(data_url,data_dir+"/"+"xxxx.tgz")
                
            os.system('cd %s && md5sum xxxx.tgz' % data_dir)
            # add exceute privilege
            os.system('chmod +x %s/main' % datadir)
            ret=os.popen('%s/main' % datadir).read()
            for item in ret.split("\n"):
                if not item:
                    continue
                else:
                    key,val=item.split(":")
                    data["UD_"+key]=val

        return data
        
    
    def runAllGet(self):
        #inspect.getmembers : Return all members of an object as (name, value) pairs sorted by name.
        #Optionally, only return members that satisfy a given predicate.
        #inspect.ismethod:  Return true if the object is an instance method. 可选地,只返回成员满足给定谓词。
        for fun in inspect.getmembers(self,predicate=inspect.ismethod):
            if fun[0]=="userDefineMon":
                self.data.update(fun[1]())            # ????
            elif fun[0][:3]=='get':
                self.data[ fun[0][:3] ]=fun[1]()      # ????
        return self.data
    

if __name__=="__main__":
    print mon().runAllGet()
    
