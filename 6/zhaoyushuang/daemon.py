#!/usr/bin/env python

import sys, os, time, atexit
from signal import SIGTERM

class Daemon:
    """
    通用的能将程序变成守护进程的类,重写run方法
    """
    def __init__(self, pidfile='nbMon.pid', stdin='/dev/null', stdout='nbMon.log', stderr='nbMon.log'):
	    self.stdin = stdin
	    self.stdout = stdout
	    self.stderr = stderr
	    self.pidfile = pidfile
   
    def daemonize(self):
	    try:
            #os.fork : fork() -> pid . Fork a child process. 创建一个新线程
		    pid = os.fork()
		    if pid > 0:
			    # exit first parent
			    sys.exit(0)
	    except OSError, e:
		    sys.stderr.write("fork #1 failed: %d (%s)\n" % (e.errno, e.strerror))
		    sys.exit(1)
   
	    #decouple from parent environment
	    #os.chdir("/")
        #设置SID
	    os.setsid()
        #设置UMASK
	    os.umask(0)
   
	    # 第二次 fork
	    try:
		    pid = os.fork()
		    if pid > 0:
			    # exit from second parent
			    sys.exit(0)
	    except OSError, e:
		    sys.stderr.write("fork #2 failed: %d (%s)\n" % (e.errno, e.strerror))
		    sys.exit(1)
   
	    # flush log
	    sys.stdout.flush()
	    sys.stderr.flush()
	    si = file(self.stdin, 'r')
	    so = file(self.stdout, 'a+')
	    se = file(self.stderr, 'a+', 0)
	    os.dup2(si.fileno(), sys.stdin.fileno())
	    os.dup2(so.fileno(), sys.stdout.fileno())
	    os.dup2(se.fileno(), sys.stderr.fileno())
   
	    # 写入 pidfile 
        #atexit 模块允许你注册一个或多个终止函数(暂且这么叫), 这些函数将在解释器终止前被自动调用.
        #调用 register 函数, 便可以将函数注册为终止函数,你也可以添加更多的参数, 这些将作为 exit 函数的参数传递.
	    atexit.register(self.delpid)
	    pid = str(os.getpid())
	    file(self.pidfile,'w+').write("%s\n" % pid)
    
    # 删除PID文件
    def delpid(self):
	    os.remove(self.pidfile)
    
    #启动守护线程
    def start(self):
	    # 检查pid文件是否存在,存在就认为程序在运行
	    try:
		    pf = file(self.pidfile,'r')
		    pid = int(pf.read().strip())
		    pf.close()
	    except IOError:
		    pid = None
   
	    if pid:
		    message = "pidfile %s already exist. Daemon already running?\n"
		    sys.stderr.write(message % self.pidfile)
		    sys.exit(1)
	   
	    # 将程序变成守护线程
	    self.daemonize()
	    self.run()
    
    #停止守护进程
    def stop(self):
	    # 读取PID文件获得PID
	    try:
		    pf = file(self.pidfile,'r')
		    pid = int(pf.read().strip())
		    pf.close()
	    except IOError:
		    pid = None
   
	    if not pid:
		    message = "pidfile %s does not exist. Daemon not running?\n"
		    sys.stderr.write(message % self.pidfile)
		    return # not an error in a restart

	    # 开始kill掉守护进程       
	    try:
		    while 1:
			    os.kill(pid, SIGTERM)
			    time.sleep(0.1)
	    except OSError, err:
		    err = str(err)
		    if err.find("No such process") > 0:
			    if os.path.exists(self.pidfile):
				    os.remove(self.pidfile)
		    else:
			    print str(err)
			    sys.exit(1)

    #restart
    def restart(self):
	    self.stop()
	    self.start()
    
    #subclass need rewrite
    def run(self):
	    """
	    You should override this method when you subclass Daemon. It will be called after the process has been
	    daemonized by start() or restart().
	    """

