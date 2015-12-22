#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: agent.py
@time: 2015/12/15 16:56
"""
import zerorpc
import os
import sys
import time
from crypt import *
import gipc
import conf
import pdb

sys.path.insert(1,os.path.join(sys.path[0],'..'))
from nbNet.daemon import Daemon
from  collector.agent import startTh

TEST =True

class MyDaemon(Daemon):
    def run(self):
        e = gipc.start_process(target = Executor,args=('Executor',))
        e.join()

def Collector(name):
    print 'hello',name
    startTh()

def Executor(name):
    print 'hello',name
    # pdb.set_trace()
    s= zerorpc.Server(a())
    s.bind("tcp://0.0.0.0:%d" % conf.exec_port)
    # pdb.set_trace()
    s.run()

class a(object):
    def test(self):
        return '1111'

class HelloRPC(object):
    def hello(self,name):
            # print "exec %s %s"%(name,time.strftime('%Y-%m-%d %H-%m-%S',time.localtime((time.time()))))
            # ret = os.popen(name).read()
            # ret_str = "Result %s\n %s" % (time.struct_time('%Y-%m-%d %H-%m-%S',time.localtime(time.time())),ret)
            # return encrypt(ret_str)
            print name
            return '1111'

    def deploy(self,pkg,path):
        '''
        http://reboot:8000/testDeploy/reboot_test_online_mian.tgz
        :param pkg:
        :param path:
        :return:
        '''
        pdb.set_trace()
        ret = {'errno':0,"msg":'succ'}
        print pkg,path
        os.system("mkdir -p %s"%conf.tmp_path)
        import urllib
        print "%s/%s.tgz"%(conf.pkg_server,pkg)
        urllib.urlretrieve("%s/%s.tgz"%(conf.pkg_server,pkg),conf.tmp_path+'/'+pkg+".tgz")
        unzip_ret = os.system("cd %s && tar xzf %s.tgz" % (conf.tmp_path,pkg))
        if unzip_ret != 0:
            ret['errno'] = unzip_ret
            ret['msg'] = 'unzip error'
            return ret
        md5_ret = os.system("cd %s/%s && md5sum -c md5.list" % (conf.tmp_path,pkg))
        if md5_ret !=0:
            ret['errno'] = md5_ret
            ret['msg'] = 'md5 error'
            return ret
        os.system("cd %s/%s/bin && chmod +x *" %(conf.tmp_path,pkg))
        os.system("cd %s/%s/script && chmod +x *" % (conf.tmp_path,pkg))
        print "cd %s/%s/script && ./stop" % (conf.tmp_path,pkg)
        stop_ret = os.system("cd %s/%s/script && ./stop" % (conf.tmp_path,pkg))
        os.system("mkdir -p %s/%s"%(path,pkg))
        print "cd %s/%s/ && cp -r * %s/%s" %(conf.tmp_path,pkg,path,pkg)
        replace_ret = os.system("cd %s/%s/ && cp -r * %s/%s" % (conf.tmp_path,pkg,path,pkg))
        if replace_ret !=0:
            ret['errno'] = replace_ret
            ret['msg'] = 'replace error'
            return ret
        status_ret = os.system("cd %s/%s/script && ./status"% (path,pkg))
        if status_ret !=0:
            ret['errno'] = status_ret
            ret['msg'] = 'status error'
            return ret
        return ret

if __name__ == '__main__':
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if TEST:
        # daemon.run()
        ex = Executor('Executor')

    else :
        if len(sys.arv) == 2:
            if 'start' == sys.argv[1]:
                daemon.start()
            elif 'stop' == sys.argv[1]:
                daemon.stop()
            elif 'restart' == sys.argv[1]:
                daemon.restart()
            else:
                print 'Unknown command'
                sys.exit(2)
            sys.exit(0)
        else:
            print 'usage: %s start|stop|restart' % sys.argv[0]
            sys.exit(2)