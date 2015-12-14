#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: nbNet_with_pipe.py
@time: 2015/12/14 11:19
"""
#!/usr/bin/env python
# coding: utf-8

from daemon import Daemon
import socket
import select
import time
import pdb
import subprocess

__all__ = ["nbNet", "sendData_mh"]
#DEBUG = True
maxheader =5
from nbNetUtils import *

class nbNetBase:
    '''non-blocking Net'''
    def setFd(self, sock):
        """sock is class object of socket"""
        #dbgPrint("\n -- setFd start!")
        tmp_state = STATE()
        tmp_state.sock_obj = sock
        self.conn_state[sock.fileno()] = tmp_state
        #self.conn_state[sock.fileno()].printState()
        #dbgPrint("\n -- setFd end!")

    def accept(self, fd):
        """fd is fileno() of socket"""
        #dbgPrint("\n -- accept start!")
        sock_state = self.conn_state[fd]
        sock = sock_state.sock_obj
        conn, addr = sock.accept()
        # set to non-blocking: 0
        conn.setblocking(0)
        return conn

    def close(self, fd):
        """fd is fileno() of socket"""
        try:
            # cancel of listen to event
            self.epoll_sock.unregister(fd)
            sock = self.conn_state[fd].sock_obj
            sock.close()
            self.conn_state.pop(fd)
            # print fd
            # print 'close'
            # print self.epoll_sock.poll()
        except Exception,msg:
            #dbgPrint("Close fd: %s abnormal" % fd)
            print 'close error :'
            print msg
    #@profile
    def read(self, fd):
        """fd is fileno() of socket"""
        #pdb.set_trace()
        try:
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            if sock_state.need_read <= 0:
                raise socket.error
            one_read = conn.recv(sock_state.need_read)
            #dbgPrint("\tread func fd: %d, one_read: %s, need_read: %d" % (fd, one_read, sock_state.need_read))
            if len(one_read) == 0:
                raise socket.error
            # process received data
            sock_state.buff_read += one_read
            sock_state.have_read += len(one_read)
            sock_state.need_read -= len(one_read)
            #sock_state.printState()

            # read protocol header
            if sock_state.have_read == maxheader:
                header_said_need_read = int(sock_state.buff_read)
                if header_said_need_read <= 0:
                    raise socket.error
                sock_state.need_read += header_said_need_read
                sock_state.buff_read = ''
                # call state machine, current state is read.
                # after protocol header haven readed, read the real cmd content,
                # call machine instead of call read() it self in common.
                #sock_state.printState()
                return "readcontent"
            elif sock_state.need_read == 0:
                # recv complete, change state to process it
                return "process"
            else:
                return "readmore"
        except (socket.error, ValueError), msg:
            try:
                if msg.errno == 11:
                    #dbgPrint("11 " + msg)
                    return "retry"
            except:
                pass
            return 'closing'


    #@profile
    def write(self, fd):
        sock_state = self.conn_state[fd]
        conn = sock_state.sock_obj
        #pdb.set_trace()
        last_have_send = sock_state.have_write
        try:
                # to send some Bytes, but have_send is the return num of .send()
                have_send = conn.send(sock_state.buff_write[last_have_send:])
                sock_state.have_write += have_send
                sock_state.need_write -= have_send
                if sock_state.need_write == 0 and sock_state.have_write != 0:
                    # send complete, re init status, and listen re-read
                    #sock_state.printState()
                    #dbgPrint('\n write data completed!')
                    return "writecomplete"
                else:
                    return "writemore"
        except socket.error, msg:
                return "closing"


    def run(self):
        while True:
            epoll_list = self.epoll_sock.poll()
            # print '---epoll--:'
            # print epoll_list
            for fd, events in epoll_list:
                #dbgPrint('\n-- run epoll return fd: %d. event: %s' % (fd, events))
                sock_state = self.conn_state[fd]
                if select.EPOLLHUP & events:
                    #dbgPrint("EPOLLHUP")
                    sock_state.state = "closing"
                elif select.EPOLLERR & events:
                    #dbgPrint("EPOLLERR")
                    sock_state.state = "closing"
                self.state_machine(fd)

    def state_machine(self, fd):
        #time.sleep(0.1)
        #dbgPrint("\n - state machine: fd: %d, status: %s" % (fd, self.conn_state[fd].state))
        sock_state = self.conn_state[fd]
        self.sm[sock_state.state](fd)

class nbNet(nbNetBase):
    def __init__(self, addr, port, logic):
        #dbgPrint('\n__init__: start!')
        self.conn_state = {}
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_sock.bind((addr, port))
        self.listen_sock.listen(10)
        self.setFd(self.listen_sock)
        self.epoll_sock = select.epoll()
        # LT for default, ET add ' | select.EPOLLET '
        self.epoll_sock.register(self.listen_sock.fileno(), select.EPOLLIN )
        self.logic = logic
        self.sm = {
            "accept" : self.accept2read,
            "read"   : self.read2process,
            "write"  : self.write2read,
            "process": self.process,
            "closing": self.close,
        }

    #@profile
    def process(self, fd):
        sock_state = self.conn_state[fd]
        response = self.logic(fd, sock_state.buff_read)
        if response == None:
            conn = sock_state.sock_obj
            self.setFd(conn)
            self.conn_state[fd].state = "read"
            self.epoll_sock.modify(fd, select.EPOLLIN)
        else:
            sock_state.buff_write = "%0"+maxheader+"d%s" % (len(response), response)
            sock_state.need_write = len(sock_state.buff_write)
            #sock_state.printState()
            #self.state_machine(fd)
            sock_state.state = "write"
            self.epoll_sock.modify(fd, select.EPOLLOUT)



    #@profile
    def accept2read(self, fd):
        conn = self.accept(fd)
        self.epoll_sock.register(conn.fileno(), select.EPOLLIN)
        # new client connection fd be initilized
        self.setFd(conn)
        self.conn_state[conn.fileno()].state = "read"
        # now end of accept, but the main process still on 'accept' status
        # waiting for new client to connect it.
        #dbgPrint("\n -- accept end!")

    #@profile
    def read2process(self, fd):
        """fd is fileno() of socket"""
        #pdb.set_trace()
        read_ret = ""
        try:
            read_ret = self.read(fd)
        except (Exception), msg:
            #dbgPrint(msg)
            read_ret = "closing"
        if read_ret == "process":
            # recv complete, change state to process it
            #sock_state.state = "process"
            self.process(fd)
        elif read_ret == "readcontent":
            pass
        elif read_ret == "readmore":
            pass
        elif read_ret == "retry":
            pass
        elif read_ret == "closing":
            self.conn_state[fd].state = 'closing'
            # closing directly when error.
            self.state_machine(fd)
        else:
            raise Exception("impossible state returned by self.read")

    #@profile
    def write2read(self, fd):
        try:
            write_ret = self.write(fd)
        except socket.error, msg:
            write_ret = "closing"

        if write_ret == "writemore":
            pass
        elif write_ret == "writecomplete":
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            self.setFd(conn)
            self.conn_state[fd].state = "read"
            self.epoll_sock.modify(fd, select.EPOLLIN)
        elif write_ret == "closing":
            #dbgPrint(msg)
            self.conn_state[fd].state = 'closing'
            # closing directly when error.
            self.state_machine(fd)

counter = 0
if __name__ == '__main__':

    def logic(fd,cmd):
        global counter
        counter += 1
        if counter % 100000 == 0:
            print counter, time.time()
        subprocess.Popen(cmd,stdin = fd, stdout = fd, stderr =fd, shell = True)
        return None

    reverseD = nbNet('0.0.0.0', 8080, logic)
    reverseD.run()