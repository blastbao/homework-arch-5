#!/usr/bin/env python
# -*- coding: utf-8 -*-

from daemon import Daemon
import socket
import select
import time

__all__ = ["nbNet"]

from nbNetUtils import *

class STATE:
    def __init__(self):
        #这是socket状态,读写头,读写缓冲
        self.state = "accept"
        self.have_read = 0
        self.need_read = 10
        self.have_write = 0
        self.need_write = 0

        self.buff_read = ""
        self.buff_write = ""

        self.sock_obj = ""

    def printState(self):
        if DEBUG:
            dbgPrint("\n - current state of fd: %d" % self.sock_obj.fileno())
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
        #初始化STATE类 默认socket状态是accept
        tmp_state = STATE()
        #设置socket对象
        tmp_state.sock_obj = sock
        #将socket放入字典，并将状态作为值传进去
        self.conn_state[sock.fileno()] = tmp_state
        self.conn_state[sock.fileno()].printState()
        dbgPrint("\n -- setFd end!")

    def accept(self, fd):
        dbgPrint("\n -- accept start!")
        sock_state = self.conn_state[fd]
        sock = sock_state.sock_obj
        conn, addr = sock.accept()
        #这是socket为非阻塞
        conn.setblocking(0)
        return conn

    def close(self, fd):
        try:
            #关闭连接
            sock = self.conn_state[fd].sock_obj
            sock.close()
        except:
            dbgPrint("Close fd: %s abnormal" % fd)
        finally:
            #注销socket,将socket从连接中删除
            self.epoll_sock.unregister(fd)
            self.conn_safe.pop(fd)

    def read(self, fd):
        try:
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj

            if sock_state.need_read <= 0:
                raise socket.error
            #第一次读取头获得数据长度，以后读取数据
            one_read = conn.recv(sock_state.need_read)
            dbgPrint("\tread func fd: %d, one_read: %s, need_read: %d" % (fd,
                        one_read, sock_state.need_read))

            if len(one_read) == 0:
                raise socket.error

            sock_state.buff_read += one_read
            sock_state.have_read += len(one_read)
            sock_state.need_read -= len(one_read)
            sock_state.printState()

            if sock_state.have_read == 10:
                header_said_need_read = int(sock_state.buff_read)
                if header_said_need_read <= 0:
                    raise socket.error
                sock_state.need_read += header_said_need_read
                sock_state.buff_read = ''

                sock_state.printState()
                return "readcontent"
                #读完数据返回process,否则返回readmore
            elif sock_state.need_read == 0:
                return "process"
            else:
                return "readmore"
        except (socket.error, ValueError), msg:
            try:
                if msg.errno == 11:
                    dbgPrint("11" + msg)
                    return "retry"
            except:
                pass
            #将socket置为closing状态
            return 'closing'

    def write(self, fd):
        sock_state = self.conn_state[fd]
        conn = sock_state.sock_obj
        last_have_send = sock_state.have_write
        try:
            #发送数据
            have_send = conn.send(sock_state.buff_write[last_have_send:])
            sock_state.have_write += have_send
            sock_state.need_write -= have_send
            if sock_state.need_write == 0 and sock_state.have_write != 0:
                sock_state.printState()
                dbgPrint("\n write data completed!")
                return "writecomplete"
            else:
                return "writemore"
        except socket.error, msg:
            return "closing"

    def run(self):
        while True:
            #返回事件列表
            epoll_list = self.epoll_sock.poll()
            for fd, events in epoll_list:
                #获取socket状态
                sock_state = self.conn_state[fd]
                #与运算 判断事件状态
                if select.EPOLLHUP & events:
                    dbgPrintf("EPOLLHUP")
                    sock_state.state = 'closing'
                elif select.EPOLLERR & events:
                    dbgPrintf("EPOLLERR")
                    sock_state.state = 'closing'
                self.state_machine(fd)

    def state_machine(self, fd):
        #获取指定socket 当前状态类
        sock_state = self.conn_state[fd]
        #根据socket状态执行处理该状态函数
        self.sm[sock_state.state](fd)

class nbNet(nbNetBase):
    def __init__(self, addr, port, logic):
        dbgPrint("\n__init__: start!")
        #初始化状态字典
        self.conn_state = {}
        #初始化socket对象，tcp/ipv4 类型
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_sock.bind((addr, port))
        self.listen_sock.listen(10)
        #使用setFd设置socket状态,4个头,读写缓冲，将当前scoket状态类放入字典中
        #并打印当前scoket状态
        self.setFd(self.listen_sock)
        self.epoll_sock = select.epoll()
        #注册 listen_sock 至epollin interface 边缘触发模式
        self.epoll_sock.register(self.listen_sock.fileno(), select.EPOLLIN)
        self.logic = logic
        #初始化状态机字典
        self.sm = {
            "accept" : self.accept2read,
            "read"   : self.read2process,
            "write"  : self.write2read,
            "process": self.process,
            "closing": self.close,
        }
        dbgPrint("\n__init__: end, register no: %s" %
                self.listen_sock.fileno())



    def process(self, fd):
        sock_state = self.conn_state[fd]
        respone = self.logic(sock_state.buff_read)
        sock_state.buff_write = "%010d%s" % (len(respone), respone)
        sock_state.need_write = len(sock_state.buff_write)
        sock_state.state = "write"
        #修改 sock 至epollout interface
        self.epoll_sock.modify(fd, select.EPOLLOUT)
        sock_state.printState()

    def accept2read(self, fd):
        conn = self.accept(fd)
        #将socket注册 至epollin interface
        self.epoll_sock.register(conn.fileno(), select.EPOLLIN)
        #使用setFd设置socket状态,4个头,读写缓冲，将当前scoket状态类放入字典中
        #并打印当前scoket状态
        self.setFd(conn)
        #将socket状态设置为read
        self.conn_state[conn.fileno()].state = "read"
        dbgPrint("\n -- accept end!")

    def read2process(self, fd):
        read_ret = ""
        try:
            read_ret = self.read(fd)
        except (Exception), msg:
            dbgPrint(msg)
            read_ret = 'closing'
        if read_ret == 'process':
            self.process(fd)
        elif read_ret == 'readcontent':
            pass
        elif read_ret == 'readmore':
            pass
        elif read_ret == 'retry':
            pass
        elif read_ret == 'closing':
            self.conn_state[fd].state == 'closing'
            #关闭socket
            self.state_machine(fd)
        else:
            raise Exception("impossible state returned by self.read")

    def write2read(self, fd):
        try:
            write_ret = self.write(fd)
        except socket.error, msg:
            write_ret = 'closing'

        if write_ret == 'writemore':
            pass
        elif write_ret == 'writecomplete':
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            #发送成功后，保持连接，将socket状态置为read，注册到epollin
            self.setFd(conn)
            self.conn_state[fd].state = 'read'
            self.epoll_sock.modify(fd, select.EPOLLIN)
        elif write_ret == 'closing':
            dbgPrint(msg)
            #调用状态机关闭socket
            self.conn_state[fd].state = 'closing'
            self.state_machine(fd)

if __name__ == '__main__':
    def logic(d_in):
        return(d_in[::-1])
    #传递参数,初始化nbNet对象
    reverseD = nbNet('0.0.0.0', 9076, logic)
    #启动nbNet父类nbNetBase run方法,
    reverseD.run()
