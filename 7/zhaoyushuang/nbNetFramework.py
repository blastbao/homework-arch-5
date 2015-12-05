#!/usr/bin/env python
# coding: utf-8

from daemon import Daemon
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
        dbgPrint("\n -- setFd start!")
        # init state 
        tmp_state = STATE()
        # set sock_obj
        tmp_state.sock_obj = sock
        # set sock into conn_state  
        self.conn_state[sock.fileno()] = tmp_state
        # print 
        self.conn_state[sock.fileno()].printState()
        dbgPrint("\n -- setFd end!")

    def accept(self, fd): 
        """ scoket.accept """
        #fd is fileno() of socket
        dbgPrint("\n -- accept start!")
        # get sock from conn_state.fd
        sock_state = self.conn_state[fd]
        sock = sock_state.sock_obj
        # scoket.accept
        conn, addr = sock.accept()
        # set to non-blocking: 0
        conn.setblocking(0)
        return conn
    
    def close(self, fd):
        """close socke,close epoll_sock."""
        try:
            # cancel of listen to event
            sock = self.conn_state[fd].sock_obj
            sock.close()
        except:
            dbgPrint("Close fd: %s abnormal" % fd)
            pass
        finally :
            self.epoll_sock.unregister(fd)
            self.conn_state.pop(fd)
    
    def read(self, fd):
        """socket receive and read content from socket"""
        #pdb.set_trace()
        try:    
            # get sock from conn_state
            sock_state = self.conn_state[fd]
            # get connection from sock
            conn = sock_state.sock_obj
            # if need_read is null ,throws exception
            if sock_state.need_read <= 0:
                raise socket.error
            # connection read count= need_read
            one_read = conn.recv(sock_state.need_read)
            dbgPrint("\tread func fd: %d, one_read: %s, need_read: %d" % (fd, one_read, sock_state.need_read))
            # if read content is null ,throws exception
            if len(one_read) == 0:
                raise socket.error
                
            # process received data
            #set buffer read
            sock_state.buff_read += one_read
            #set have read
            sock_state.have_read += len(one_read)
            #set need read
            sock_state.need_read -= len(one_read)
            sock_state.printState()

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
                sock_state.printState()
                return "readcontent"
            elif sock_state.need_read == 0:
                # recv complete, change state to process it
                return "process"
            else:
                return "readmore"
        except (socket.error, ValueError), msg:
            try:
                #if some other error 
                if msg.errno == 11:
                    dbgPrint("11 " + msg)
                    return "retry"
            except:
                pass
            return 'closing'
        

    def write(self, fd):
        """ write """
        # get sock from conn_state.fd
        sock_state = self.conn_state[fd]
        #get connection from sock_state
        conn = sock_state.sock_obj
        last_have_send = sock_state.have_write
        try:
            # to send some Bytes, but have_send is the return num of .send()
            have_send = conn.send(sock_state.buff_write[last_have_send:])
            sock_state.have_write += have_send
            sock_state.need_write -= have_send
            if sock_state.need_write == 0 and sock_state.have_write != 0:
                # send complete, re init status, and listen re-read
                sock_state.printState()
                dbgPrint('\n write data completed!')
                return "writecomplete"
            else:
                return "writemore"
        except socket.error, msg:
            return "closing"



    def run(self):
        while True:
            dbgPrint("\nrun func loop:")
            # print conn_state
            for i in self.conn_state.iterkeys():
                dbgPrint("\n - state of fd: %d" % i)
                self.conn_state[i].printState()

            # get epoll message from epoll_sock
            epoll_list = self.epoll_sock.poll()
            for fd, events in epoll_list:
                dbgPrint('\n-- run epoll return fd: %d. event: %s' % (fd, events))
                # get conn_state 
                sock_state = self.conn_state[fd]
                # when EPOLLHUP,EPOLLERR then close
                if select.EPOLLHUP & events:
                    dbgPrint("EPOLLHUP")
                    sock_state.state = "closing"
                elif select.EPOLLERR & events:
                    dbgPrint("EPOLLERR")
                    sock_state.state = "closing"
                # otherwise run state_machine
                self.state_machine(fd)

    def state_machine(self, fd):
        #time.sleep(0.1)
        dbgPrint("\n - state machine: fd: %d, status: %s" % (fd, self.conn_state[fd].state))
        # get sock_state from conn_state.fd
        sock_state = self.conn_state[fd]
        # run function ,that defined in sm subclass use parameter (sock_state.state) (fd)
        self.sm[sock_state.state](fd)

class nbNet(nbNetBase):
    def __init__(self, addr, port, logic):
        dbgPrint('\n__init__: start!')
        self.conn_state = {}
        # get socket
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_sock.bind((addr, port))
        self.listen_sock.listen(10)
        # set fd
        self.setFd(self.listen_sock)
        # set epoll_sock 
        self.epoll_sock = select.epoll()
        # LT for default, ET add ' | select.EPOLLET '
        # epoll register 
        self.epoll_sock.register(self.listen_sock.fileno(), select.EPOLLIN )
        # set the running function
        self.logic = logic
        # set the dict for some string to some function ,that run  in super class run
        self.sm = {
            "accept" : self.accept2read,
            "read"   : self.read2process,
            "write"  : self.write2read,
            "process": self.process,
            "closing": self.close,
        }
        dbgPrint('\n__init__: end, register no: %s' % self.listen_sock.fileno() )

    def process(self, fd):
        #get scok_state from conn_state dict
        sock_state = self.conn_state[fd]
        # run logic ,and get response of the function
        response = self.logic(sock_state.buff_read)
        # format buffer write
        sock_state.buff_write = "%010d%s" % (len(response), response)
        #set need write
        sock_state.need_write = len(sock_state.buff_write)
        # SET THE next function
        sock_state.state = "write"
        # change epoll status
        self.epoll_sock.modify(fd, select.EPOLLOUT)
        sock_state.printState()
        #self.state_machine(fd)
    
    def accept2read(self, fd):
        #accept connection
        conn = self.accept(fd)
        # epoll register
        self.epoll_sock.register(conn.fileno(), select.EPOLLIN)
        # new client connection fd be initilized 
        self.setFd(conn)
        #set the next function
        self.conn_state[conn.fileno()].state = "read"
        # now end of accept, but the main process still on 'accept' status
        # waiting for new client to connect it.
        dbgPrint("\n -- accept end!")

    def read2process(self, fd):
        """read function """
        #pdb.set_trace()
        read_ret = ""
        try:
            read_ret = self.read(fd)
        except (Exception), msg:
            dbgPrint(msg)
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

    def write2read(self, fd):
        """ write function """
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
            dbgPrint(msg)
            self.conn_state[fd].state = 'closing'
            # closing directly when error.
            self.state_machine(fd)
    

if __name__ == '__main__':
    def logic(d_in):
        return(d_in[::-1])

    reverseD = nbNet('0.0.0.0', 9076, logic)
    reverseD.run()
