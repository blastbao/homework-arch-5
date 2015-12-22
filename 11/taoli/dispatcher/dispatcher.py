#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: dispatcher.py
@time: 2015/12/21 11:05
usage :  dispatcher.py  'date' root 127.0.0.1 127.0.0.1
"""
import socket
import sys,os
import socket,select
import pdb
sys.path.insert(1,os.path.join(sys.path[0],'..'))
from nbNet.nbNet_with_pipe import nbNet,STATE
remote_port = 1119
maxheader = 5
read_size = 256
end_tag ='\r\n'
class Dispatcher(nbNet):
    def __init__(self,logic):
            self.conn_state = {}
            self.epoll_sock = select.epoll()
            self.logic = logic
            remote_cmd = sys.argv[1]+'||'+ sys.argv[2]    # 'date|||root'
            for host in sys.argv[3:] :        #start with the host1 ,host2,host3
                sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
                sock.connect((host,remote_port))
                sock.setblocking(0)
                tmp_state = STATE()
                tmp_state.state = 'write'
                tmp_str = '%0'+str(maxheader)+"d%s"
                tmp_state.buff_write = tmp_str % (len(remote_cmd), remote_cmd)   #00010date||root
                tmp_state.need_write = len(tmp_state.buff_write)
                tmp_state.sock_obj = sock
                self.conn_state[sock.fileno()] = tmp_state
                self.epoll_sock.register(sock.fileno(), select.EPOLLOUT)
            self.sm = {
                "accept" : self.accept2read,
                "read"   : self.read2process,
                "write"  : self.write2read,
                "process": self.process,
                "closing": self.close,
            }

    def setFd(self,sock):
        tmp_state = STATE()
        tmp_state.sock_obj = sock
        self.conn_state[sock.fileno()] = tmp_state

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
            self.conn_state[fd].state = 'closing'
            self.state_machine(fd)

    def read2process(self, fd):
        #pdb.set_trace()
        read_ret = ""
        try:
            read_ret = self.read(fd)
            # print read_ret
        except (Exception), msg:
            #dbgPrint(msg)
            read_ret = "closing"
        if read_ret == "process":
            self.process(fd)
        elif read_ret == "readmore":
            pass
        elif read_ret == "retry":
            pass
        elif read_ret == "closing":
            self.conn_state[fd].state = 'closing'
            self.state_machine(fd)
        else:
            raise Exception("impossible state returned by self.read")

    def process(self, fd):
        # pdb.set_trace()
        sock_state = self.conn_state[fd]
        response = self.logic(fd, sock_state.buff_read)
        # sock_state.state = 'closing'
        # self.state_machine(fd)
        # print 'process end'

    def read(self, fd):
        # print 'read'
        # pdb.set_trace()
        try:
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            read = conn.recv(read_size)
            if len(read) == 0:
                raise socket.error
            if read[-2:] == end_tag:
                sock_state.buff_read += read[:-2]
                return "process"
            else:
                 sock_state.buff_read += read
                 return "readmore"
        except (socket.error, ValueError), msg:
            try:
                if msg.errno == 11:
                    return "retry"
            except:
                print msg
            return 'closing'

    def write(self, fd):
        # print 'write'
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
                    return "writecomplete"
                else:
                    return "writemore"
        except socket.error, msg:
                print msg
                return "closing"

    def run(self):
        while True:
            # pdb.set_trace()
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

if __name__ == '__main__':
    def logic(fd,d_in):
        print d_in  #获得rpc端口的执行结果
    d = Dispatcher(logic)
    d.run()





