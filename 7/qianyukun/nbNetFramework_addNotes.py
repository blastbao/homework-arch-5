#!/usr/bin/env python
# coding: utf-8
from daemon import Daemon
import socket
import select
import time
import pdb
from nbNetUtils import *

__all__ = ["nbNet"]
#DEBUG = True

class STATE:
    def __init__(self):
        self.state = "accept"   #连接状态，指示本次执行应做什么
        self.have_read = 0      #记录已经读取的字节数
        self.need_read = 10     #记录还应读取多少字节
        self.have_write = 0     #记录已经写入多少字节
        self.need_write = 0     #记录还应写入多少字节
        self.buff_read = ""     #读缓存，记录已经读出的内容
        self.buff_write = ""    #写缓存，记录还未写入的内容
        self.sock_obj = ""      #记录该连接的socket
    def printState(self):
        if DEBUG:
            dbgPrint('\n - curent state of fd: %d' % self.sock_obj.fileno())
            dbgPrint(" - - state: %s" % self.state)
            dbgPrint(" - - have_read: %s" % self.have_read)
            dbgPrint(" - - need_read: %s" % self.need_read)
            dbgPrint(" - - have_write: %s" % self.have_write)
            dbgPrint(" - - need_write: %s" % self.need_write)
            dbgPrint(" - - buff_write: %s" % self.buff_write)
            dbgPrint(" - - buff_read: %s" % self.buff_read)
            dbgPrint(" - - sock_obj: %s" % self.sock_obj)

class nbNetBase:
    def setFd(self, sock):
        dbgPrint("\n -- setFd start!")
        tmp_state = STATE() #实例化一个状态类
        tmp_state.sock_obj = sock   #指定状态类中的socket
        self.conn_state[sock.fileno()] = tmp_state  #把这个socket插入到conn_state中
        self.conn_state[sock.fileno()].printState()
        dbgPrint("\n -- setFd end!")
    def accept(self, fd):
        dbgPrint("\n -- accept start!")
        sock_state = self.conn_state[fd]    #取出链接状态
        sock = sock_state.sock_obj  #取出socket
        conn, addr = sock.accept()  #接受连接请求
        conn.setblocking(0) #设置该连接为非阻塞
        return conn #返回该连接
    def close(self, fd):
        try:
            sock = self.conn_state[fd].sock_obj #取出socket
            sock.close()    #将socket关闭
        except:
            dbgPrint("Close fd: %s abnormal" % fd)
        finally:
            self.epoll_sock.unregister(fd)  #将fd从epoll中注销
            self.conn_state.pop(fd) #将该fd从连接状态字典中弹出
    def read(self, fd):
        try:
            sock_state = self.conn_state[fd]    #取出连接状态
            conn = sock_state.sock_obj  #取出socket
            if sock_state.need_read <= 0:   #如果还应读取的字节数小于等于0，则崩溃程序
                raise socket.error
            one_read = conn.recv(sock_state.need_read)  #读取一次，并将读取到的内容纪录到one_read
            dbgPrint("\tread func fd: %d, one_read: %s, need_read: %d" % (fd, one_read, sock_state.need_read))
            if len(one_read) == 0:  #如果读取到的字节数为0，则程序崩溃
                raise socket.error
            sock_state.buff_read += one_read    #将读取到的内容写入读取缓冲里
            sock_state.have_read += len(one_read)   #将已经读取的字节数加上本次读取的字节数
            sock_state.need_read -= len(one_read)   #将还需读取的字节数减去本次读取的字节数
            sock_state.printState()
            if sock_state.have_read == 10:  #如果已经读取了10个字节，则表示已经将自定义协议的头部读完
                header_said_need_read = int(sock_state.buff_read)   #将头部转化为整形
                if header_said_need_read <= 0:  #如果头数字小于等于0
                    raise socket.error  #程序报错
                sock_state.need_read += header_said_need_read   #等于其他数字，则将头显示的长度加到还需读取的长度中
                sock_state.buff_read = ''   #清空读取缓冲
                sock_state.printState()
                return "readcontent"    #返回读取内容
            elif sock_state.need_read == 0: #如果还需读取的字节数为0
                return "process"    #则返回process
            else:
                return "readmore"   #否则返回readmore
        except (socket.error, ValueError), msg:
            try:
                if msg.errno == 11: #如果读取出错，返回的错误码为11
                    dbgPrint("11 " + msg)
                    return "retry"  #则重试
            except:
                pass
            return "closing"    #否则将连接置为关闭
    def write(self, fd):
        sock_state = self.conn_state[fd]    #取出连接状态
        conn = sock_state.sock_obj  #取出socket
        last_have_send = sock_state.have_write  #取出需要写入的字节数
        try:
            have_send = conn.send(sock_state.buff_write[last_have_send:])   #写入要发送的内容，并将已发的字节数赋值给have_send
            sock_state.have_write += have_send  #已写入字节数加上已发送字节数
            sock_state.need_write -= have_send  #还需写入字节数减掉已发送字节数
            if sock_state.need_write == 0 and sock_state.have_write != 0:   #如果还需写入字节数等于0，已写入字节数不等于0
                sock_state.printState()
                dbgPrint('\n write data completed!')
                return "writecomplete"  #返回写入完成
            else:
                return "writemore"  #否则返回继续写
        except socket.error, msg:
            return "closing"    #如果写入出错，则返回closing
    def run(self):
        while True:
            dbgPrint("\nrun func loop:")
            for i in self.conn_state.iterkeys():
                dbgPrint("\n - state of fd: %d" % i)
                self.conn_state[i].printState()
            epoll_list = self.epoll_sock.poll() #等待epoll通知新消息
            for fd, events in epoll_list:
                dbgPrint('\n-- run epoll return fd: %d. event: %s' % (fd, events))
                sock_state = self.conn_state[fd]    #从conn_state中拿到fd当前的状态
                if select.EPOLLHUP & events:    #如果状态为EPOLLHUP则关闭连接
                    dbgPrint("EPOLLHUP")
                    sock_state.state = "closing"
                elif select.EPOLLERR & events:  #如果状态为EPOLLHUP则关闭连接
                    dbgPrint("EPOLLERR")
                    sock_state.state = "closing"
                self.state_machine(fd)  #状态正常则执行状态机
    def state_machine(self, fd):    #状态机函数
        dbgPrint("\n - state machine: fd: %d, status: %s" % (fd, self.conn_state[fd].state))
        sock_state = self.conn_state[fd]    #从conn_state字典中取出fd的状态
        self.sm[sock_state.state](fd)   #按照状态机字典sm对fd执行对应的操作
class nbNet(nbNetBase):
    def __init__(self, addr, port, logic):
        dbgPrint('\n__init__: start!')
        self.conn_state = {}    #初始化一个监听状态字典
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) #定义socket，使用TCP/IP协议
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)  #打开地址复用，以免重启时无法监听
        self.listen_sock.bind((addr, port)) #指定监听地址和端口
        self.listen_sock.listen(10) #排队的连接最多为10个
        self.setFd(self.listen_sock)    #将监听的fd加入conn_state
        self.epoll_sock = select.epoll()    #实例化一个epoll
        self.epoll_sock.register(self.listen_sock.fileno(), select.EPOLLIN) #让epoll监视这个socket的进入方向
        self.logic = logic  #业务逻辑
        self.sm = { #定义一个状态机的使用逻辑，当前状态为key的使用就执行value中的方法
            "accept":self.accept2read,
            "read":self.read2process,
            "write":self.write2read,
            "process":self.process,
            "closing":self.close,
        }
        dbgPrint('\n__init__: end,register no: %s' % self.listen_sock.fileno())
    def process(self, fd):  #process函数直接由read2process函数调用
        sock_state = self.conn_state[fd]    #取出连接状态
        response = self.logic(sock_state.buff_read) #执行业务逻辑，并取得返回值
        sock_state.buff_write = "%010d%s" % (len(response), response)   #将业务逻辑返回的值加上头，并赋值给写缓冲
        sock_state.need_write = len(sock_state.buff_write)  #将需要写入的字节数改为写缓冲的长度
        sock_state.state = "write"  #将连接状态置为write
        self.epoll_sock.modify(fd, select.EPOLLOUT) #让epoll监控写方向
        sock_state.printState()
    def accept2read(self, fd):  #状态为accept则执行此函数
        conn = self.accept(fd)  #执行accept函数接受该连接请求
        self.epoll_sock.register(conn.fileno(), select.EPOLLIN) #设置epoll监控该连接的进入方向
        self.setFd(conn)    #将这个连接状态插入到conn_state中，更新状态？
        self.conn_state[conn.fileno()].state = "read"   #将连接状态改为read
        dbgPrint("\n -- accept end!")
    def read2process(self, fd): #当连接状态为read时执行此函数
        read_ret = ""   #定义一个读取状态
        try:
            read_ret = self.read(fd)    #执行read函数并返回读取状态
        except (Exception),msg: #如果读取过程中出错
            dbgPrint(msg)
            read_ret = "closing"    #则关闭连接
        if read_ret == "process":   #如果返回值为process
            self.process(fd)    #则执行process函数
        elif read_ret =="readcontent":  #返回状态为读取内容、读取更多、重试时不做任何处理，等待下次读取。
            pass
        elif read_ret == "readmore":
            pass
        elif read_ret == "retry":
            pass
        elif read_ret == "closing": #返回状态为关闭时
            self.conn_state[fd].state = 'closing'   #将连接状态置为closing
            self.state_machine(fd)  #调用状态机，关闭连接
        else:
            raise Exception("impossible state returned by self.read")
    def write2read(self, fd):   #当连接状态为write时，调用该函数
        try:
            write_ret = self.write(fd)  #调用write函数，并取得返回值
        except socket.error, msg:
            write_ret = "closing"   #如果出错则将写入状态置为closing
        if write_ret == "writemore":    #如果写入状态为继续，则什么都不做，等待下次写入
            pass
        elif write_ret == "writecomplete":  #如果写入状态为已写完
            sock_state = self.conn_state[fd]    #取出连接状态
            conn = sock_state.sock_obj  #取出socket
            self.setFd(conn)    #重置连接
            self.conn_state[fd].state = "read"  #将连接状态置为读取
            self.epoll_sock.modify(fd,select.EPOLLIN)   #使epoll监控入向
        elif write_ret == "closing":    #如果写入状态为closing
            dbgPrint(msg)
            self.conn_state[fd].state = "closing" #将连接状态置为closing
            self.state_machine(fd)  #调用状态机函数关闭连接
if __name__ == '__main__':
    def logic(d_in):    #业务逻辑
        return(d_in[::-1])  #反转内容
    reverseD = nbNet('0.0.0.0', 9000, logic)    #启动一个监听
    reverseD.run()  #运行