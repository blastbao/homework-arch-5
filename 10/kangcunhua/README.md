#第十次作业：
1. 将讲义上的HelloRPC程序抄写完毕；
2. 将课堂上未调试完毕的执行命令改为非阻塞 调试完成：
    1. os.Popen改subprocess.Popen 
    2. 默认的subprocess.PIPE有大小限制：65536.因此当输出内容超过65536，会引起阻塞；
    2. 默认调用：subprocess.Popen(cmd,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    3. 解决方法是不用subprocess提供的PIPE，而是使用自己创建的流
    4. 自定义调用：subprocess.Popen(d_in , shell= True, stdout=coming_sock_fd, stderr=coming_sock_fd)

##关于作业1：
抄写了一遍，木有啥好说的；
##关于作业2：subprocess.Popen
###相关文件：
1. /collector/rpc_demo.py
2. /nbNet/nbNetFramework.py
3. /nbNet/nbNetUtils.py
4. /nbNet/loadrun.py

###思路：
1. 修改nbNetUtils.py STATE类增加一个状态 self.popen_pipe = 0
2. rpc_demo.py 自定义PIPE ：subprocess.Popen(d_in , shell= True, stdout=coming_sock_fd, stderr=coming_sock_fd)
3. nbNetFramework.py 修改 class nbNet的 process函数：置标志位pip，跳转至"write"状态
    1. sock_state.popen_pipe = 1
    2. sock_state.have_read = 0
    3. sock_state.need_read = 10
    4. sock_state.buff_read = ""
    5. sock_state.state = "write"
4. nbNetBase类中 write方法：如果 pipe，则直接转换为 "writecomplete"
5. 测试：
    1. 启动服务器： python rpc_demo.py
    2. 启动客户端： echo -n "0000000002ls" | nc 127.0.0.1 9079
    3. 启动客户端： echo -n "0000000027hostname&&sleep 5&&hostname" | nc 127.0.0.1 9079
    4. 或者 启动客户端： python loadrun.py ls 10
    5. enjoy your self！
6. update:2015.12.23 修复close时服务器端异常退出的缺陷；
    1. 根据课上的讲解，彻底修复close时报异常的缺陷：先unregister，再close就搞定了。
    2. 在ctrl +c 或ctrl + \ 终止 agent 程序时，服务器端 会关闭agent链接， 保持socket，等待 客户端agent 的再次 连接
    2. 原思路是将状态机流转到writecomplate之后就再次read，长连接，不触发close方法
    3. 按照原思路，在ctrl +c 或ctrl + \ 终止 agent程序时，服务器端 报异常退出，长连接关闭 触发close方法，报一个异常，不能算最终修复缺陷；
    4. 原思路写的代码 其余部分 运行正常，只是逻辑上略微 多绕了两个状态函数。
    5. 最新的修复 逻辑上的 多走俩状态的 问题 在下一次作业 提交。这个保留自己的解决办法。 

###关于之前的异常
```python
 - state of fd: 5
154 
 - current state of fd: 5
155  - - state: write
156  - - have_read: 0
157  - - need_read: 10
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7f29f4e5d9f0>
165  - - popen_pipe:   1
140 
-- run epoll return fd: 5. event: 25
143 EPOLLHUP
152 
 - state machine: fd: 5, status: closing
50 Close fd: 5 abnormal
132 
run func loop:
135 
 - state of fd: 3
154 
 - current state of fd: 3
155  - - state: accept
156  - - have_read: 0
157  - - need_read: 10
158  - - have_write: 0
159  - - need_write: 0
160  - - buff_write: 
161  - - buff_read:  
162  - - sock_obj:   <socket._socketobject object at 0x7f29f4e5d980>
165  - - popen_pipe:   0
140 
-- run epoll return fd: 5. event: 25
Traceback (most recent call last):
  File "rpc_demo.py", line 20, in <module>
    reverseD.run()
  File "/home/kang/arch-5/rebootMon/collector/../nbNet/nbNetFramework.py", line 141, in run
    sock_state = self.conn_state[fd]
KeyError: 5
>>study:/home/kang/arch-5/rebootMon/collector>
```

###思路2：
1. 使用文件中转

```python
    import tempfile

    out_temp = tempfile.SpooledTemporaryFile(bufsize=10*1000)
    fileno = out_temp.fileno()
    obj = subprocess.Popen(cmd,stdout=fileno,stderr=fileno,shell=True)
```
###思路3：
1. 使用commands包，也是不阻塞，还可以分析返回。但素，貌似这个包要废弃了；

##socket编程原理
> 使用 SOCK_STREAM/TCP 套接字才有“连接”的概念。连接意味着可靠的数据流通讯机制，可以同时有多个数据流。可以想象成一个数据互不干扰的管道。另外一个重要的提示是：数据包的发送和接收是有顺序的。其他一些 Socket 如 UDP、ICMP 和 ARP 没有“连接”的概念，它们是无连接通讯，意味着你可从任何人或者给任何人发送和接收数据包。

###socket客户端编程：
1. 创建 Socket
2. 连接到远程服务器
3. 发送数据
4. 接收回应

###socket服务器端编程主要包括下面几步：
1. 打开 socket
2. 绑定到一个地址和端口
3. 侦听进来的连接
4. 接受连接
5. 读写数据

### socket编程问题的引出
> http://blog.csdn.net/hguisu/article/details/7444092
> 1) 普通的I/O操作过程:
UNIX系统的I/O命令集，是从Maltics和早期系统中的命令演变出来的，其模式为打开一读/写一关闭（open-write-read-close）。在一个用户进程进行I/O操作时，它首先调用“打开”获得对指定文件或设备的使用权，并返回称为文件描述符的整型数，以描述用户在打开的文件或设备上进行I/O操作的进程。然后这个用户进程多次调用“读/写”以传输数据。当所有的传输操作完成后，用户进程关闭调用，通知操作系统已经完成了对某对象的使用。 

> 2) TCP/IP协议被集成到UNIX内核中

> TCP/IP协议被集成到UNIX内核中时，相当于在UNIX系统引入了一种新型的I/O操作。UNIX用户进程与网络协议的交互作用比用户进程与传统的I/O设备相互作用复杂得多。首先，进行网络操作的两个进程在不同机器上，如何建立它们之间的联系？其次，网络协议存在多种，如何建立一种通用机制以支持多种协议？这些都是网络应用编程界面所要解决的问题。 

> 3) 需要一种通用的网络编程接口:  独立于具体协议和通用的网络编程

> 在UNIX系统中，网络应用编程界面有两类：UNIX BSD的套接字（socket）和UNIX System V的TLI。由于Sun公司采用了支持TCP/IP的UNIX BSD操作系统，使TCP/IP的应用有更大的发展，其网络应用编程界面──套接字（socket）在网络软件中被广泛应用，至今已引进微机操作系统DOS和Windows系统中，成为开发网络应用软件的强有力工具，本章将要详细讨论这个问题。

