#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-12-13 15:56:48
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-12-16 22:23:48
import zerorpc
import time
import os
from crypt import *
import gipc
import sys
import time
import conf
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet.daemon import Daemon
form collector.agent import startTh

TEST = True


class MyDaemon(Daemon):
    """docstring for MyDaemon"""

    def __init__(self, arg):
        super(MyDaemon, self).__init__()
        self.arg = arg

    def run(self):
        e = gipc.start_process(target=Executor, args=('Executor',))
        e.join()


def collector(name):
    print 'hello', name
    startTh()


def Executor(name):
    print 'hello', name

    s = zerorpc.Server(helloRPC())
    s.bind("tcp://0.0.0.0:%d" % conf.exec_port)
    s.run()


class helloRPC(object):
    """docstring for helloRPC"""

    def __init__(self, arg):
        super(helloRPC, self).__init__()
        self.arg = arg

    def hello(self, name):
        print "exec %s %s" % (name, time.strftime('%Y-%m-%d %H-%m-%S', time.localtime()))
        ret = os.popen(name).read()
        ret_str = "Result %s\n %s" % (time.strftime('%Y-%m-%d %H-%m-%S', time.localtime())), ret)
        return encrypt(ret_str)
    def deploy(self, pkg, path):
        """[summary]

        [description]http://reboot:8000/testDeploy/reboot_test_online_main.tgz

        Arguments:
            pkg {[type]} -- [description]
            path {[type]} -- [description]
        """
        ret={"errno": 0, "msg": "succ"}
        print pkg, path
        os.system("mkdir -p %s" % conf.tmp_path)
        import urllib
        print "%s/%s.tgz" % (conf.pkg_server, pkg)
        urllib.urlretrieve("%s/%s.tgz" % (conf.pkg_server, pkg)),
        conf.tmp_path + "" + pkg + ".tgz"
        unzip_ret=os.system("cd %s && tar xzf %s.tgz" % (conf.tmp_path.pkg))
        if unzip_ret != 0:
            ret['errno']=unzip_ret
            ret['msg']='unzip error'
            return ret
        md5_ret=os.system("cd %s/%s && md5sum -c md5list" % (conf.tmp_path, pkg))
        if md5_ret != 0:
            ret['error']=md5_ret
            ret['msg']='md5 error'
            return ret

        os.system("cd %s/%s/bin && chmod +x *" % (conf.tmp_path, pkg))
        os.system("cd %s/%s/script && chmod +x *" % (conf.tmp_path, pkg))
        print "cd %s/%s/script && ./stop" % (conf.tmp_path, pkg)
        stop_ret=os.system("cd %s/%s/script && ./stop" % (conf.tmp_path, pkg))
        if md5_ret != 0:
            ret['errno']=md5_ret
            ret['msg']='md5 error'
            return ret

        os.system("cd %S/%s/bin && chmod +x *" % (conf.tmp_path, pkg))
        os.system("cd %S/%s/script && chmod +x *" % (conf.tmp_path, pkg))
        print "cd %S/%s/script && ./stop" % (conf.tmp_path, pkg)
        stop_ret=os.system("cd %S/%s/script && ./stop" % (conf.tmp_path, pkg))
        # if stop_ret != 0:
            # status_ret = os.system("cd %s/%s/script && ./status" %(path, pkg))
        # if status_ret == 0:
            # ret['errno'] = stop_ret
            # ret['msg'] = 'stop error'
            # return ret
        os.system("mkdir -p %s/%s" % (path, pkg))
        print "cd %s/%s/ && cp -r * %s/%s" % (conf.tmp_path, pkg, path, pkg)
        replace_ret=os.system("cd %s/%s/ && cp -r * %s/%s" % (conf.tmp_path, pkg, path, pkg))
        if replace_ret != 0:
            ret['errno']=replace_ret
            ret['msg']='replace error'
            return ret
        start_ret=os.system("cd %s/%s/script && ./start" % (path, pkg))
        if start_ret != 0:
            ret['error']=start_ret
            ret['msg']='start error'
            return ret
        status_ret=os.system("cd %s/%s/script && ./start" % (path, pkg))
        if status_ret != 0:
            ret['error']=status_ret
            ret['msg']='status error'
            return ret
        return ret
if __name__ == '__main__':
    daemon=MyDaemon('/tmp/daemon-example.pid')
    if TEST:
        daemon.run()
    else:
        if len(sys.argv) == 2:
            if 'start' == sys.argv[1]:
                daemon.start()
            elif 'stop' == sys.argv[1]:
                daemon.stop()
            elif 'restart' == sys.argv[1]:
                daemon.restart()
            else:
                print "Unknown command"
                sys.exit(2)
            sys.exit(0)
        else:
            print "useage: %s start|stop|restart" % sys.argv[0]
            sys.exit(2)
