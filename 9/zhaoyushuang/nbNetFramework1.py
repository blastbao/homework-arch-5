#!/usr/bin/env python
# coding: utf-8

from daemon import Daemon
import socket
import select
import time

from nbNetUtils import *

# class STATE:
#     def __init__(self):
#         self.state = "accept"     # 0
#         self.have_read = 0        # 1
#         self.need_read = 10       # 2
#         self.have_write = 0       # 3
#         self.need_write = 0       # 4
#         self.buff_write = ""      # 5
#         self.buff_read = ""       # 6
#         self.sock_obj = ""        # 7

class nbNetBase:
    '''non-blocking Net'''
    def setFd(self, sock):
        """sock is class object of socket"""
        # tmp_state = STATE()
        # tmp_state.sock_obj = sock
        # self.conn_state[sock.fileno()] = tmp_state
        self.conn_state[sock.fileno()] = ["accept",0,10,0,0,"","",sock]

    def accept(self, fd): 
        """fd is fileno() of socket"""
        # sock_state = self.conn_state[fd]
        # sock = sock_state.sock_obj
        # conn, addr = sock.accept()
        conn, addr = self.conn_state[fd][7].accept()
        # set to non-blocking: 0
        conn.setblocking(0)
        return conn
    
    def close(self, fd):
        """fd is fileno() of socket"""
        try:
            # cancel of listen to event
            sock = self.conn_state[fd][7].close()
        except:
            pass
        finally:
            self.epoll_sock.unregister(fd)
            self.conn_state.pop(fd)
    
    def read(self, fd):
        """fd is fileno() of socket"""
        try:
            sock_state = self.conn_state[fd]
            conn = sock_state[7]
            # need_read index =2 
            if sock_state[2] <= 0:
                raise socket.error

            one_read = conn.recv(sock_state[2])
            if len(one_read) == 0:
                raise socket.error
            # process received data
            sock_state[6] += one_read
            # have_read index =1
            sock_state[1] += len(one_read)
            sock_state[2] -= len(one_read)

            # read protocol header
            if sock_state[1] == 10:
                header_said_need_read = int(sock_state[6])
                if header_said_need_read <= 0:
                    raise socket.error
                sock_state[2] += header_said_need_read
                sock_state[6] = ''

                return "readcontent"
            elif sock_state[2] == 0:
                # recv complete, change state to process it
                return "process"
            else:
                return "readmore"
        except (socket.error, ValueError), msg:
            try:
                if msg.errno == 11:
                    return "retry"
            except:
                pass
            return 'closing'
        

    def write(self, fd):
        sock_state = self.conn_state[fd]
        conn = sock_state[7]
        # have_write index =3
        last_have_send = sock_state[3]
        try:
            # to send some Bytes, but have_send is the return num of .send()
            
            # buff_write index =5 
            have_send = conn.send(sock_state[5][last_have_send:])
            sock_state[3] += have_send
            
            # need_write index =4
            sock_state[4] -= have_send
            if sock_state[4] == 0 and sock_state[3] != 0:
                # send complete, re init status, and listen re-read
                return "writecomplete"
            else:
                return "writemore"
        except socket.error, msg:
            return "closing"


    def run(self):
        while True:
            for fd, events in self.epoll_sock.poll:
                sock_state = self.conn_state[fd]
                if select.EPOLLHUP & events:
                    sock_state[0] = "closing"
                elif select.EPOLLERR & events:
                    sock_state[0] = "closing"
                self.state_machine(fd)

    def state_machine(self, fd):
        sock_state = self.conn_state[fd]
        self.sm[sock_state[0]](fd)

class nbNet(nbNetBase):
    def __init__(self, addr, port, logic):
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


    def process(self, fd):
        sock_state = self.conn_state[fd]
        response = self.logic(sock_state[6])
        sock_state[5] = "%010d%s" % (len(response), response)
        sock_state[4] = len(sock_state[5])
        sock_state[0] = "write"
        self.epoll_sock.modify(fd, select.EPOLLOUT)
        #self.state_machine(fd)
    

    def accept2read(self, fd):
        conn = self.accept(fd)
        self.epoll_sock.register(conn.fileno(), select.EPOLLIN)
        # new client connection fd be initilized 
        self.setFd(conn)
        self.conn_state[conn.fileno()][0] = "read"
        # now end of accept, but the main process still on 'accept' status
        # waiting for new client to connect it.

    def read2process(self, fd):
        """fd is fileno() of socket"""
        read_ret = ""
        try:
            read_ret = self.read(fd)
        except (Exception), msg:
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
            self.conn_state[fd][0] = 'closing'
            # closing directly when error.
            self.state_machine(fd)
        else:
            raise Exception("impossible state returned by self.read")

    def write2read(self, fd):
        try:
            write_ret = self.write(fd)
        except socket.error, msg:
            write_ret = "closing"

        if write_ret == "writemore":
            pass
        elif write_ret == "writecomplete":
            sock_state = self.conn_state[fd]
            conn = sock_state[7]
            self.setFd(conn)
            self.conn_state[fd][0] = "read"
            self.epoll_sock.modify(fd, select.EPOLLIN)
        elif write_ret == "closing":
            self.conn_state[fd][0] = 'closing'
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

    reverseD = nbNet('0.0.0.0', 9090, logic)
    reverseD.run()
    
    
    
    
    


#[zhaoyushang@teach nbNet]$ python -m cProfile -s cumulative ./nbNetFramework2.py 
#100000 1449931839.61
#200000 1449931848.04
#300000 1449931856.55
#400000 1449931865.18
#500000 1449931873.81
#600000 1449931882.46
#700000 1449931891.3
#800000 1449931899.92
#900000 1449931908.75
#^C         26565889 function calls (26565071 primitive calls) in 82.476 seconds
#
#   Ordered by: cumulative time
#
#   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#        1    0.001    0.001   82.476   82.476 nbNetFramework2.py:4(<module>)
#        1    7.168    7.168   82.403   82.403 nbNetFramework2.py:117(run)
#  2737694    6.180    0.000   68.828    0.000 nbNetFramework2.py:129(state_machine)
#  1825128    5.612    0.000   41.104    0.000 nbNetFramework2.py:173(read2process)
#  1825128   12.698    0.000   23.250    0.000 nbNetFramework2.py:52(read)
#   912563    5.097    0.000   21.543    0.000 nbNetFramework2.py:198(write2read)
#   912563    7.174    0.000   12.241    0.000 nbNetFramework2.py:154(process)
#   912567    3.170    0.000    7.896    0.000 nbNetFramework2.py:24(setFd)
#   996670    6.408    0.000    6.408    0.000 {method 'poll' of 'select.epoll' objects}
#7304294/7304145    6.305    0.000    6.306    0.000 {len}
#   912563    2.932    0.000    6.272    0.000 nbNetFramework2.py:94(write)
#  1825128    5.828    0.000    5.828    0.000 {method 'recv' of '_socket.socket' objects}
#   912580    2.920    0.000    4.726    0.000 socket.py:223(meth)
#  1825126    4.576    0.000    4.576    0.000 {method 'modify' of 'select.epoll' objects}
#   912563    3.340    0.000    3.340    0.000 {method 'send' of '_socket.socket' objects}
#   912563    1.191    0.000    1.191    0.000 nbNetFramework2.py:220(logic)
#   912625    0.947    0.000    0.947    0.000 {getattr}
#   912574    0.859    0.000    0.859    0.000 {method 'fileno' of '_socket.socket' objects}
#        1    0.002    0.002    0.063    0.063 nbNetUtils.py:4(<module>)
#        1    0.001    0.001    0.059    0.059 inspect.py:25(<module>)
#        1    0.001    0.001    0.050    0.050 tokenize.py:23(<module>)
#        6    0.000    0.000    0.049    0.008 re.py:188(compile)
#        6    0.000    0.000    0.049    0.008 re.py:226(_compile)
#        6    0.000    0.000    0.049    0.008 sre_compile.py:493(compile)
#        7    0.000    0.000    0.047    0.007 {map}
#        6    0.000    0.000    0.025    0.004 sre_parse.py:677(parse)
#     56/6    0.001    0.000    0.024    0.004 sre_parse.py:301(_parse_sub)
#        6    0.000    0.000    0.024    0.004 sre_compile.py:478(_code)
#    115/6    0.007    0.000    0.024    0.004 sre_parse.py:379(_parse)
#    262/6    0.006    0.000    0.021    0.003 sre_compile.py:32(_compile)
#      115    0.001    0.000    0.009    0.000 sre_compile.py:178(_compile_charset)
#        1    0.007    0.007    0.008    0.008 socket.py:45(<module>)
#      115    0.004    0.000    0.007    0.000 sre_compile.py:207(_optimize_charset)
#      735    0.002    0.000    0.006    0.000 sre_parse.py:201(get)
#      904    0.004    0.000    0.006    0.000 sre_parse.py:182(__next)
#        6    0.003    0.001    0.005    0.001 collections.py:288(namedtuple)
#     1185    0.003    0.000    0.005    0.000 sre_parse.py:130(__getitem__)
#     3395    0.004    0.000    0.004    0.000 {method 'append' of 'list' objects}
#  377/123    0.002    0.000    0.003    0.000 sre_parse.py:140(getwidth)
#        6    0.000    0.000    0.003    0.001 sre_compile.py:359(_compile_info)
#        1    0.001    0.001    0.002    0.002 pdb.py:3(<module>)
#      718    0.001    0.000    0.002    0.000 sre_parse.py:195(match)
#      562    0.001    0.000    0.002    0.000 sre_parse.py:126(__len__)
#       25    0.002    0.000    0.002    0.000 sre_compile.py:258(_mk_bitmap)
#     1209    0.002    0.000    0.002    0.000 {isinstance}
#        1    0.001    0.001    0.002    0.002 collections.py:1(<module>)
#      117    0.001    0.000    0.001    0.000 sre_compile.py:354(_simple)
#      310    0.001    0.000    0.001    0.000 sre_parse.py:138(append)
#       30    0.000    0.000    0.001    0.000 {all}
#        1    0.000    0.000    0.001    0.001 dis.py:1(<module>)
#      609    0.001    0.000    0.001    0.000 {min}
#        1    0.001    0.001    0.001    0.001 daemon.py:3(<module>)
#      244    0.001    0.000    0.001    0.000 collections.py:332(<genexpr>)
#        1    0.000    0.000    0.001    0.001 opcode.py:5(<module>)
#        3    0.000    0.000    0.001    0.000 nbNetFramework2.py:164(accept2read)
#        1    0.001    0.001    0.001    0.001 repr.py:1(<module>)
#      262    0.000    0.000    0.000    0.000 sre_parse.py:90(__init__)
#       31    0.000    0.000    0.000    0.000 {method 'join' of 'str' objects}
#       67    0.000    0.000    0.000    0.000 sre_parse.py:257(_escape)
#        1    0.000    0.000    0.000    0.000 heapq.py:31(<module>)
#        3    0.000    0.000    0.000    0.000 nbNetFramework2.py:31(accept)
#      353    0.000    0.000    0.000    0.000 sre_compile.py:24(_identityfunction)
#        3    0.000    0.000    0.000    0.000 socket.py:201(accept)
#      285    0.000    0.000    0.000    0.000 {ord}
#        1    0.000    0.000    0.000    0.000 bdb.py:1(<module>)
#      214    0.000    0.000    0.000    0.000 {method 'isalnum' of 'str' objects}
#        4    0.000    0.000    0.000    0.000 socket.py:185(__init__)
#       54    0.000    0.000    0.000    0.000 {method 'format' of 'str' objects}
#        1    0.000    0.000    0.000    0.000 nbNetFramework2.py:134(__init__)
#      157    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
#        1    0.000    0.000    0.000    0.000 os.py:35(_get_exports_list)
#       38    0.000    0.000    0.000    0.000 sre_parse.py:83(closegroup)
#      119    0.000    0.000    0.000    0.000 opcode.py:27(def_op)
#       30    0.000    0.000    0.000    0.000 collections.py:358(<genexpr>)
#       38    0.000    0.000    0.000    0.000 sre_parse.py:225(_class_escape)
#      117    0.000    0.000    0.000    0.000 sre_parse.py:134(__setitem__)
#        2    0.000    0.000    0.000    0.000 {dir}
#       38    0.000    0.000    0.000    0.000 sre_parse.py:72(opengroup)
#       30    0.000    0.000    0.000    0.000 collections.py:356(<genexpr>)
#       90    0.000    0.000    0.000    0.000 {method 'startswith' of 'str' objects}
#        3    0.000    0.000    0.000    0.000 {method 'accept' of '_socket.socket' objects}
#       89    0.000    0.000    0.000    0.000 {max}
#        1    0.000    0.000    0.000    0.000 token.py:1(<module>)
#       19    0.000    0.000    0.000    0.000 tokenize.py:45(group)
#       11    0.000    0.000    0.000    0.000 opcode.py:31(name_op)
#        1    0.000    0.000    0.000    0.000 socket.py:179(_socketobject)
#        6    0.000    0.000    0.000    0.000 sre_parse.py:178(__init__)
#       41    0.000    0.000    0.000    0.000 {setattr}
#       38    0.000    0.000    0.000    0.000 {method 'remove' of 'list' objects}
#        6    0.000    0.000    0.000    0.000 {_sre.compile}
#       12    0.000    0.000    0.000    0.000 sre_compile.py:472(isstring)
#        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#        1    0.000    0.000    0.000    0.000 nbNetUtils.py:27(decorated)
#        4    0.000    0.000    0.000    0.000 {method 'register' of 'select.epoll' objects}
#        6    0.000    0.000    0.000    0.000 opcode.py:35(jrel_op)
#       30    0.000    0.000    0.000    0.000 {method '__contains__' of 'frozenset' objects}
#       26    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}
#        1    0.000    0.000    0.000    0.000 pdb.py:59(Pdb)
#       30    0.000    0.000    0.000    0.000 {method 'isdigit' of 'str' objects}
#        6    0.000    0.000    0.000    0.000 opcode.py:39(jabs_op)
#        1    0.000    0.000    0.000    0.000 functools.py:17(update_wrapper)
#        1    0.000    0.000    0.000    0.000 pprint.py:35(<module>)
#        6    0.000    0.000    0.000    0.000 {repr}
#       11    0.000    0.000    0.000    0.000 {range}
#       12    0.000    0.000    0.000    0.000 {method 'replace' of 'str' objects}
#       24    0.000    0.000    0.000    0.000 {method 'add' of 'set' objects}
#        9    0.000    0.000    0.000    0.000 {time.time}
#        6    0.000    0.000    0.000    0.000 {method 'split' of 'str' objects}
#        1    0.000    0.000    0.000    0.000 {method 'bind' of '_socket.socket' objects}
#        1    0.000    0.000    0.000    0.000 cmd.py:46(<module>)
#        1    0.000    0.000    0.000    0.000 collections.py:26(OrderedDict)
#        7    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
#        3    0.000    0.000    0.000    0.000 {method 'setblocking' of '_socket.socket' objects}
#        1    0.000    0.000    0.000    0.000 atexit.py:6(<module>)
#        1    0.000    0.000    0.000    0.000 {method 'listen' of '_socket.socket' objects}
#        1    0.000    0.000    0.000    0.000 <string>:1(Attribute)
#        6    0.000    0.000    0.000    0.000 {sys._getframe}
#        1    0.000    0.000    0.000    0.000 <string>:1(Traceback)
#        1    0.000    0.000    0.000    0.000 <string>:1(ArgInfo)
#        2    0.000    0.000    0.000    0.000 tokenize.py:47(maybe)
#        1    0.000    0.000    0.000    0.000 <string>:1(ModuleInfo)
#        1    0.000    0.000    0.000    0.000 <string>:1(ArgSpec)
#        1    0.000    0.000    0.000    0.000 <string>:1(Arguments)
#        6    0.000    0.000    0.000    0.000 sre_parse.py:67(__init__)
#        1    0.000    0.000    0.000    0.000 keyword.py:11(<module>)
#        1    0.000    0.000    0.000    0.000 tokenize.py:46(any)
#        1    0.000    0.000    0.000    0.000 bdb.py:14(Bdb)
#        1    0.000    0.000    0.000    0.000 pprint.py:84(PrettyPrinter)
#        4    0.000    0.000    0.000    0.000 {hasattr}
#        1    0.000    0.000    0.000    0.000 cmd.py:55(Cmd)
#        1    0.000    0.000    0.000    0.000 socket.py:235(_fileobject)
#        1    0.000    0.000    0.000    0.000 fnmatch.py:11(<module>)
#        1    0.000    0.000    0.000    0.000 collections.py:390(Counter)
#        2    0.000    0.000    0.000    0.000 repr.py:10(__init__)
#        1    0.000    0.000    0.000    0.000 {method 'setsockopt' of '_socket.socket' objects}
#        1    0.000    0.000    0.000    0.000 repr.py:8(Repr)
#        1    0.000    0.000    0.000    0.000 nbNetFramework2.py:22(nbNetBase)
#        1    0.000    0.000    0.000    0.000 daemon.py:6(Daemon)
#        1    0.000    0.000    0.000    0.000 bdb.py:449(Breakpoint)
#        1    0.000    0.000    0.000    0.000 socket.py:167(_closedsocket)
#        1    0.000    0.000    0.000    0.000 functools.py:39(wraps)
#        1    0.000    0.000    0.000    0.000 nbNetFramework2.py:133(nbNet)
#        1    0.000    0.000    0.000    0.000 nbNetUtils.py:120(STATE)
#        1    0.000    0.000    0.000    0.000 nbNetUtils.py:26(timeout)
#        1    0.000    0.000    0.000    0.000 bdb.py:614(Tdb)
#        1    0.000    0.000    0.000    0.000 tokenize.py:146(TokenError)
#        1    0.000    0.000    0.000    0.000 bdb.py:10(BdbQuit)
#        1    0.000    0.000    0.000    0.000 {method 'update' of 'dict' objects}
#        1    0.000    0.000    0.000    0.000 tokenize.py:179(Untokenizer)
#        1    0.000    0.000    0.000    0.000 inspect.py:632(BlockFinder)
#        1    0.000    0.000    0.000    0.000 nbNetUtils.py:25(TimeoutError)
#        1    0.000    0.000    0.000    0.000 inspect.py:630(EndOfBlock)
#        1    0.000    0.000    0.000    0.000 {globals}
#        1    0.000    0.000    0.000    0.000 tokenize.py:148(StopTokenizing)
#        1    0.000    0.000    0.000    0.000 pdb.py:18(Restart)
#        1    0.000    0.000    0.000    0.000 {method 'lower' of 'str' objects}
#        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#