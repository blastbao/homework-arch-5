#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-12-23 17:21:19
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-12-24 17:23:48
import sys
import os
import socket
import select
import pdb
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet.nbNetFramework import nbNet
from nbNet.nbNetUtils import *


class RpcDispatcher(nbNet):

    def __init__(self, cmd, hosts, port, logic):
        #dbgPrint('\n__init__: start!')
        self.conn_state = {}
        self.logic = logic
        self.epoll_sock = select.epoll()
        # 先调试分发到一个主机的情况：
        # hosts = ['127.0.0.1']
        for host in hosts:
            # self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
            # self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            # self.listen_sock.bind((host, port))
            # self.listen_sock.listen(10)
            print '=======hs=====:', host, '====p====', port
            self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.listen_sock.connect((host, port))
            self.listen_sock.setblocking(0)

            self.initState(self.listen_sock, cmd)

            # LT for default, ET add ' | select.EPOLLET '
            self.epoll_sock.register(self.listen_sock.fileno(), select.EPOLLOUT)

        self.sm = {
            "accept": self.accept2read,
            "read": self.read2process,
            "write": self.write2read,
            "process": self.process,
            "closing": self.close,
        }

    def initState(self, sock, cmd):
        """sock is class object of socket"""
        #dbgPrint("\n -- setFd start!")
        tmp_state = STATE()
        tmp_state.state = 'write'
        tmp_state.sock_obj = sock
        tmp_state.have_read = 0
        tmp_state.need_read = 0
        tmp_state.buff_write = "%010d%s" % (len(cmd), cmd)
        tmp_state.need_write = len(tmp_state.buff_write)
        self.conn_state[sock.fileno()] = tmp_state
        #@profile

    def write2read(self, fd):
        pdb.set_trace()
        try:
            write_ret = self.write(fd)
        except socket.error, msg:
            write_ret = "closing"

        if write_ret == "writemore":
            pass
        elif write_ret == "writecomplete":
            sock_state = self.conn_state[fd]
            """
            初始化下，开始读取返回的报文
            """
            sock_state.have_read = 0
            sock_state.need_read = 10
            conn = sock_state.sock_obj
            self.setFd(conn)
            self.conn_state[fd].state = "read"
            self.epoll_sock.modify(fd, select.EPOLLIN)
        elif write_ret == "closing":
            # dbgPrint(msg)
            self.conn_state[fd].state = 'closing'
            # closing directly when error.
            self.state_machine(fd)
    # #@profile
    # def write(self, fd):
    #     sock_state = self.conn_state[fd]
    #     conn = sock_state.sock_obj

    #     # pdb.set_trace()

    #     last_have_send = sock_state.have_write
    #     try:
    #         # to send some Bytes, but have_send is the return num of .send()
    #         have_send = conn.send(sock_state.buff_write[last_have_send:])
    #         sock_state.have_write += have_send
    #         sock_state.need_write -= have_send
    #         if sock_state.need_write == 0 and sock_state.have_write != 0:
    #             # send complete, re init status, and listen re-read
    #             # sock_state.printState()
    #             #dbgPrint('\n write data completed!')
    #             return "writecomplete"
    #         else:
    #             return "writemore"
    #     except socket.error, msg:
    #         return "closing"

    def process(self, fd):
        sock_state = self.conn_state[fd]
        response = self.logic(fd, sock_state.buff_read)
        # 当向某主机分发完成之后关闭链接
        sock_state.state = "closing"
        # pdb.set_trace()
        # if response == None:
        # conn = sock_state.sock_obj
        # self.setFd(conn)
        # # self.conn_state[fd].state = "read"
        # # self.epoll_sock.modify(fd, select.EPOLLIN)

        # sock_state.state = "write"
        # self.epoll_sock.modify(fd, select.EPOLLOUT)
        # else:
        #     sock_state.buff_write = "%010d%s" % (len(response), response)
        #     sock_state.need_write = len(sock_state.buff_write)
        #     # sock_state.printState()
        #     # self.state_machine(fd)
        #     sock_state.state = "write"
        #     self.epoll_sock.modify(fd, select.EPOLLOUT)

    def run(self):
        """
        此处并未重写任何语句，copy一份放到这个类里，仅仅为了调试方便；
        """
        while True:
            #dbgPrint("\nrun func loop:")
            # print conn_state
            for i in self.conn_state.iterkeys():
                dbgPrint("\n - state of fd: %d" % i)
                self.conn_state[i].printState()
            pdb.set_trace()
            epoll_list = self.epoll_sock.poll()
            for fd, events in epoll_list:
                #dbgPrint('\n-- run epoll return fd: %d. event: %s' % (fd, events))
                print '===self.conn_state:===', self.conn_state
                # print fd, events
                sock_state = self.conn_state[fd]
                if select.EPOLLHUP & events:
                    # dbgPrint("EPOLLHUP")
                    sock_state.state = "closing"
                elif select.EPOLLERR & events:
                    # dbgPrint("EPOLLERR")
                    sock_state.state = "closing"
                self.state_machine(fd)
if __name__ == '__main__':
    def logic(coming_sock_fd, d_in):
        # 得到执行命令的返回结果，打印出来：
        print '=========d_in start=========\n', coming_sock_fd, '===', d_in, '=========d_in end=========\n'

        return None
    CMD = sys.argv[1]
    HOSTS = sys.argv[2].split(',')
    print 'hosts:', HOSTS
    PORT = 9999
    reverseD = RpcDispatcher(CMD, HOSTS, PORT, logic)
    reverseD.run()
