#!/usr/bin/env python
# coding: utf-8

#from daemon import Daemon
import socket
import select
import time
import pdb

__all__ = ["nbNet", "sendData_mh"]
#DEBUG = True

from nbNetUtils import *

class nbNetBase:
    '''non-blocking Net'''
    def setFd(self, sock):
        """sock is class object of socket"""
        #dbgPrint("\n -- setFd start!")
        tmp_state = STATE(sock_obj=sock)
        #tmp_state.sock_obj = sock
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
            sock = self.conn_state[fd].sock_obj
            sock.close()
            self.epoll_sock.unregister(fd)
            self.conn_state.pop(fd)
        except:
            #dbgPrint("Close fd: %s abnormal" % fd)
            pass
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
            if sock_state.have_read == 10:
                header_said_need_read = int(sock_state.buff_read)
                if header_said_need_read <= 0:
                    raise socket.error
                sock_state.need_read += header_said_need_read
                sock_state.buff_read = ''
                # call state machine, current state is read. 
                # after protocol header haven readed, read the real cmd content, 
                # call machine instead of call read() it self in common.
                #sock_state.printState()
        #0:(accept, accept2read) 1:(read, read2process)
        #2:(write, write2read 3:(process, process)
        #4:(closing, close)
                #return "readcontent"
                return 1
            elif sock_state.need_read == 0:
                # recv complete, change state to process it
                #return "process"
                return 3
            else:
                #return "readmore"
                return 1
        except (socket.error, ValueError), msg:
            try:
                if msg.errno == 11:
                    #dbgPrint("11 " + msg)
                    return 1
                    #return "retry"
            except:
                pass
            #return 'closing'
            return 4
        

    def write(self, fd):
        sock_state = self.conn_state[fd]
        conn = sock_state.sock_obj
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
            #dbgPrint("\nrun func loop:")
            # print conn_state
            #for i in self.conn_state.iterkeys():
                #dbgPrint("\n - state of fd: %d" % i)
                #self.conn_state[i].printState()

            epoll_list = self.epoll_sock.poll()
            for fd, events in epoll_list:
                #dbgPrint('\n-- run epoll return fd: %d. event: %s' % (fd, events))
                sock_state = self.conn_state[fd]
                if select.EPOLLHUP & events:
                    #dbgPrint("EPOLLHUP")
                    sock_state.state = 4 #0:(accept, accept2read) 1:(read, read2process)
                                         #2:(write, write2read 3:(process, process)
                                         #4:(closing, close)
                elif select.EPOLLERR & events:
                    #dbgPrint("EPOLLERR")
                    sock_state.state = 4 #0:(accept, accept2read) 1:(read, read2process)
                                         #2:(write, write2read 3:(process, process)
                                         #4:(closing, close)
                self.state_machine(fd)

    def state_machine(self, fd):
        #time.sleep(0.1)
        #dbgPrint("\n - state machine: fd: %d, status: %s" % (fd, self.conn_state[fd].state))
        #0:(accept, accept2read) 1:(read, read2process)
        #2:(write, write2read 3:(process, process)
        #4:(closing, close)
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
        '''
        self.sm = {
            "accept" : self.accept2read,
            "read"   : self.read2process,
            "write"  : self.write2read,
            "process": self.process,
            "closing": self.close,
        }'''
        #0:(accept, accept2read) 1:(read, read2process)
        #2:(write, write2read 3:(process, process)
        #4:(closing, close)
        self.sm = ( self.accept2read, self.read2process, self.write2read,
                self.process, self.close, )
        #dbgPrint('\n__init__: end, register no: %s' % self.listen_sock.fileno() )

    def process(self, fd):
        sock_state = self.conn_state[fd]
        response = self.logic(sock_state.buff_read)
        sock_state.buff_write = "{0:010d}{1}".format(len(response), response)
        sock_state.need_write = len(sock_state.buff_write)
        sock_state.state = 2
        self.epoll_sock.modify(fd, select.EPOLLOUT)
        #sock_state.printState()
        #self.state_machine(fd)
    
    #@profile
    def accept2read(self, fd):
        conn = self.accept(fd)
        self.epoll_sock.register(conn.fileno(), select.EPOLLIN)
        # new client connection fd be initilized 
        self.setFd(conn)
        self.conn_state[conn.fileno()].state = 1 #0:(accept, accept2read) 1:(read, read2process)
                                                #2:(write, write2read 3:(process, process)
                                                #4:(closing, close)
        # now end of accept, but the main process still on 'accept' status
        # waiting for new client to connect it.
        #dbgPrint("\n -- accept end!")

    def read2process(self, fd):
        """fd is fileno() of socket"""
        #pdb.set_trace()
        #0:(accept, accept2read) 1:(read, read2process)
        #2:(write, write2read 3:(process, process)
        #4:(closing, close)
        read_ret = ""
        try:
            read_ret = self.read(fd)
        except (Exception), msg:
            #dbgPrint(msg)
            read_ret = 4
        #if read_ret == "process":
        if read_ret == 3:
            # recv complete, change state to process it
            #sock_state.state = "process"
            self.process(fd)
        elif read_ret == 1:
            pass
            '''
        elif read_ret == "readcontent":
            pass
        elif read_ret == "readmore":
            pass
        elif read_ret == "retry":
            pass'''
        elif read_ret == 4:
            self.conn_state[fd].state = read_ret
            # closing directly when error.
            self.state_machine(fd)
        else:
            raise Exception("impossible state returned by self.read")

    def write2read(self, fd):
        #0:(accept, accept2read) 1:(read, read2process)
        #2:(write, write2read 3:(process, process)
        #4:(closing, close)
        try:
            write_ret = self.write(fd)
        except socket.error, msg:
            write_ret = 4

        if write_ret == "writemore":
            pass
        elif write_ret == "writecomplete":
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            #self.setFd(conn)
            self.conn_state[fd] = STATE(1, conn)
            #self.conn_state[fd].sock_obj = conn
            self.epoll_sock.modify(fd, select.EPOLLIN)
        elif write_ret == "closing":
            #dbgPrint(msg)
            self.conn_state[fd].state = 4
            # closing directly when error.
            self.state_machine(fd)
    
counter = 0
if __name__ == '__main__':
    
    def logic(d_in):
        global counter
        counter += 1
        if counter % 100000 == 0:
            print counter, time.time()
        return("a")

    reverseD = nbNet('0.0.0.0', 9099, logic)
    reverseD.run()
