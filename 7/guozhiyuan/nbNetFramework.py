#!/usr/bin/env python
# coding: utf-8
#战5渣...只添加了注释，在10字节头基础上处理读telent的\r\n情况，但telnet的exit没弄好
#目前对read函数中的部分need_read还是不太理解

#from daemon import Daemon
import socket
import select
import time
import pdb


from nbNetUtils import *


class nbNetBase:
    def setFd(self, sock):
        '''sock is class object of socket'''
        dbgPrint("\n -- setFd start!")
        #设置一个初始状态实例
        tmp_state = STATE()
        #设置socket对象
        tmp_state.sock_obj = sock
        #添加socket的fileno及状态至conn_state
        self.conn_state[sock.fileno()] = tmp_state
        self.conn_state[sock.fileno()].printState()

    def accept(self, fd):
        '''fd is fileno() of socket'''
        #接受并设置socket请求对象为非阻塞
        dbgPrint("\n -- accept start!")
        sock = self.conn_state[fd].sock_obj
        conn, addr = sock.accept()
        conn.setblocking(0)
        return conn

    def close(self, fd):
        #关闭socket句柄
        try:
            sock = self.conn_state[fd].sock_obj
            sock.close()
        #注销epoll_sock中的fd并移出conn_state
        finally:
            self.epoll_sock.unregister(fd)
            self.conn_state.pop(fd)

    def read(self, fd):
        try:
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            #这里的need_read <= 0 还是不太理解...
            if sock_state.need_read <= 0:
                raise socket.error
                #开始读了
            one_read = conn.recv(sock_state.need_read)
            #遇到不可抗力抛异常
            if len(one_read) == 0:
                raise socket.error
                #处理telnet的\r\n情况，这个目前还没法处理telnet中输入exit的情况...
            if one_read[0:2] == "\r\n":
                one_read = one_read[2:]
                #设置socket的读缓冲中的数据，计数
            sock_state.buff_read += one_read
            sock_state.have_read += len(one_read)
            sock_state.need_read -= len(one_read)
            sock_state.printState()

            if sock_state.have_read == 10:
                #读10个字节头之后，把头转换为数字，也就是要读取的数据量的值
                header_said_need_read = int(sock_state.buff_read)
                if header_said_need_read <= 0:
                    raise socket.error
                    #设置need_read的数据量的值，因为have_read=10时，need_read=0,此时重置need_read需要读取的数据量部分的值
                sock_state.need_read += header_said_need_read
                sock_state.buff_read = ""
                sock_state.printState()
                return "readcontent"
            #都读完了转入process，但这里设置need_read==0是哪步代码触发的 有点晕
            elif sock_state.need_read == 0:
                return "process"
            else:
                return "readmore"
        #socket.error为11时，继续读
        except (socket.error, ValueError), msg:
            try:
                if msg.error == 11:
                    dbgPrint("11 " + msg)
                    return "retry"

            except:
                pass
            return "closing"

    def write(self, fd):
        #找到需要写的fd
        sock_state = self.conn_state[fd]
        conn = sock_state.sock_obj
        #找到写数据的起始点位置
        last_have_send = sock_state.have_write
        try:
            have_send = conn.send(sock_state.buff_write[last_have_send:])
            sock_state.have_write += have_send
            sock_state.need_write -= have_send

            if sock_state.need_write == 0 and sock_state.have_write != 0:
                sock_state.printState()
                dbgPrint('\n write data completed')
                return "writecomplete"
            else:
                return "writemore"
        except socket.err, msg:
            return "closing"

    def run(self):
        while True:
            dbgPrint("\nrun func loop:")
            for i in self.conn_state.iterkeys():
                dbgPrint("\n - state of fd: %d" % i)
                self.conn_state[i].printState()

            epoll_list = self.epoll_sock.poll()
            #轮训有时间发生的fd并处理
            for fd, events in epoll_list:
                dbgPrint("\n-- run epool return fd: %d. event: %s" % (fd, events))
                sock_state = self.conn_state[fd]
                if select.EPOLLHUP & events:
                    dbgPrint("EPOLLHUP")
                    sock_state.state = "closing"
                elif select.EPOLLERR & events:
                    dbgPrint("EPOLLERR")
                    sock_state.state = "closing"
                self.state_machine(fd)

    #设置fd的状态机中的状态
    def state_machine(self, fd):
        dbgPrint("\n - state machine: fd: %d, status: %s" % (fd, self.conn_state[fd].state))
        sock_state = self.conn_state[fd]
        self.sm[sock_state.state](fd)

class nbNet(nbNetBase):
    #初始化server的监听socket，注册epoll句柄，设置状态机的调用函数名称
    def __init__(self, addr, port, logic):
        dbgPrint("\n__init__: start!")
        self.conn_state = {}
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_sock.bind((addr, port))
        self.listen_sock.listen(10)

        self.setFd(self.listen_sock)
        self.epoll_sock = select.epoll()
        self.epoll_sock.register(self.listen_sock.fileno(), select.EPOLLIN)
        self.logic = logic

        self.sm = {"accept": self.accept2read, "read": self.read2process, "write": self.write2read, "process": self.process, "closing": self.close}

        dbgPrint("\n __init__:end, register no: %s" % self.listen_sock.fileno())

    def accept2read(self, fd):
        #accept-->read阶段的转换过程
        conn = self.accept(fd)
        self.epoll_sock.register(conn.fileno(), select.EPOLLIN)
        self.setFd(conn)
        self.conn_state[conn.fileno()].state = "read"

    def read2process(self, fd):
        #read-->process转换
        read_ret = ""
        try:
            read_ret = self.read(fd)
        except (Exception), msg:
            dbgPrint(msg)
            read_ret = "closing"

        if read_ret == "process":
            self.process(fd)

        elif read_ret == "readcontent":pass
        elif read_ret == "readmore":pass
        elif read_ret == "retry":pass
        elif read_ret =="closing":
            self.conn_state[fd].state = "closing"
            self.state_machine(fd)
        else:
            raise Exception("impossible state returned by self.read")

    def process(self, fd):
        #业务处理，拼接字符串，状态置为write，epoll_sock切换状态为发送
        sock_state = self.conn_state[fd]
        response = self.logic(sock_state.buff_read)
        sock_state.buff_write = "%010d%s" % (len(response), response)
        sock_state.need_write = len(sock_state.buff_write)
        sock_state.state = "write"
        self.epoll_sock.modify(fd, select.EPOLLOUT)

    def write2read(self, fd):
        try:
            write_ret = self.write(fd)
        except socket.error, msg:
            write_ret = "closing"

        if write_ret == "writemore":
            pass
        #发送完之后继续setFd(accept)并设置该fd为read，以接收下次来的recv，切换epoll_sock状态为接收
        elif write_ret == "writecomplete":
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            self.setFd(conn)
            self.conn_state[fd].state = "read"
            self.epoll_sock.modify(fd, select.EPOLLIN)
        elif write_ret == "closing":
            self.conn_state[fd].state = "closing"
            self.state_machine(fd)


if __name__ == '__main__':
    def logic(d_in):
        return (d_in[::-1])

    reverseD = nbNet('0.0.0.0', 6789, logic)
    reverseD.run()