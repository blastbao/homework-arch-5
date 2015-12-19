#!/usr/bin/env python
#coding=utf-8

import os
import sys
import time
import urllib

class HelloRPCDeploy(object):
    def deploy(pkg,path):
        '''
        http://reboot:8000/testDeploy/reboot_test_online_main.tgz
        '''
    
        return_dic={"errno":0,"msg":"succ"}
        print "Params : %s , %s" % (pkg,path)
        os.system("mkdir -p %s" % conf.tmp_path )
        local_pkg=conf.tmp_path + "/" + pkg + ".tgz"
        remote_pkg="%s/%s.tgz" %(conf.pkg_server,pkg)

        print "remote : %s  local : %s " %(remote_pkg,local_pkg)
        
        urllib.urlretrieve(remote_pkg,local_pkg)
        unzip_ret=os.system("cd %s && tar xzf %s.tgz" %(conf.tmp_path,pkg))
        if unzip_ret !=0:
            return_dic['errno']=unzip_ret
            return_dic['msg']='unzip error'
            return return_dic

        md5_ret=os.system("cd %s/%s && md5sum -c md5.list" %( conf.tmp_path,pkg ))
        if md5_ret!=0:
            return_dic['errno']=md5_ret
            return_dic['msg']='unzip error'
            return return_dic

        os.system("cd %s/%s/bin    && chmod +x *"  %( conf.tmp_path,pkg ))
        os.system("cd %s/%s/script && chmod +x *"  %( conf.tmp_path,pkg ))
        print "cd %s/%s/script && ./stop" %( conf.tmp_path,pkg )
        stop_ret=os.system( "cd %s/%s/script && ./stop" %( conf.tmp_path,pkg ) )

        os.system("mkdir -p %s/%s" %(path,pkg))
        print "cd %s/%s/ && cp -r * %s/%s" %(conf.tmp_path,pkg,path,pkg)
        replace_ret=os.system("cd %s/%s/ && cp -r * %s/%s" %(conf.tmp_path,pkg,path,pkg))
        if replace_ret !=0:
            return_dic['errno']=replace_ret
            return_dic['msg']='replace error'
            return return_dic

        start_ret=os.system("cd %s/%s/script && ./start" %(path,pkg))
        if start_ret !=0:
            return_dic['errno']=start_ret
            return_dic['msg']='start error'
            return return_dic


        status_ret=os.system("cd %s/%s/script && ./start" %(path,pkg))
        if status_ret !=0:
            return_dic['errno']=status_ret
            return_dic['msg']='status error'
            return return_dic

if __name__=='__main__':
    h=HelloRPCDeploy()
    h.deploy('sss','abc')
