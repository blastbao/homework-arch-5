#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.1
@author: Mark Tao
@contact: urtop@qq.com
@file: telnet_version_nbNet.py
@time: 2015/11/23 10:42
"""
#导入守护进程
from daemon import Daemon
import socket
import select
import time
import pdb

__all__ =['nbNet']
#DEBUG=True
from nbNetUtils import *
max_header_length = 5   #协议头长度

#STATE类定义，就是conn_state存储的类，包含了各种读取的计数器和当前fd的状态
class STATE:
    def __init__(self):
        self.state = 'accept' #默认创建状态
        self.have_read =0      #已经读取的字符长度
        self.need_read = max_header_length    #第一次读取时候长度等于协议头的长度
        self.have_write = 0   #已经写到缓冲区的字符长度
        self.need_write =0    #写入字符串总长度
        #下面定于的是缓冲区计数器
        self.buff_read = ''  #存放recv函数执行以后结果，包含目前一直所有的读取结果字符
        self.buff_write = ''#存放所有发送过的字符，通过send函数发给客户端
        self.sock_obj = ''  #报错sock对象

    def printState(self):
        """
        debug输出函数
        """
        if DEBUG:
            dbgPrint('\n - current state of fd: %d' % self.sock_obj.fileno())
            dbgPrint(" - - state: %s" % self.state)
            dbgPrint(" - - have_read: %s" % self.have_read)
            dbgPrint(" - - need_read: %s" % self.need_read)
            dbgPrint(" - - have_write: %s" % self.have_write)
            dbgPrint(" - - need_write: %s" % self.need_write)
            dbgPrint(" - - buff_write: %s" % self.buff_write)
            dbgPrint(" - - buff_read:  %s" % self.buff_read)
            dbgPrint(" - - sock_obj:   %s" % self.sock_obj)


class nbNetBase:

    def setFd(self,sock):
        '''
        把以fd为key，把连接和计数器等状态信息写入字典
        :param sock:
        :return:
        '''
        dbgPrint('\n --setFd start!')
        tmp_state = STATE()
        tmp_state.sock_obj = sock
        self.conn_state[sock.fileno()] = tmp_state
        self.conn_state[sock.fileno()].printState()
        dbgPrint('\n--- sefFd end!')

    def accept(self,fd):
        """
        通过fd，取出sock对象，然后设置这个sock为非阻塞模式，并返回连接
        :param fd:
        :return:
        """
        dbgPrint('\n accept start!')
        sock_state = self.conn_state[fd]
        sock = sock_state.sock_obj
        conn,addr = sock.accept()
        conn.setblocking(0)
        return conn

    def close(self,fd):
        '''
        通过fd，拿到sock对象，然后关闭，并从state里删除这个连接对象
        :return:
        '''
        try:
            sock = self.conn_state[fd].sock_obj
            sock.close()
        except:
            dbgPrint('Close fd%s '%fd)
        finally:
            self.epoll_sock.unregister(fd)
            self.conn_state.pop(fd)

    def read(self,fd):
        '''
        通过fd，从state字典里取出连接信息还有计数器等
        :param fd:
        :return:
        '''
        #pdb.set_trace()
        try:
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj      #拿到具体的连接对象
            if sock_state.need_read <=0:
                raise socket.error
            one_read = conn.recv(sock_state.need_read)    #第一次读取的时候，是根据协议头大小来的，之后是根据数据大小来的读的
            dbgPrint('\t read func fd:%d,one_read:%s,need_read:%d'%(fd,one_read,sock_state.need_read))
            if len(one_read) ==0: #正常情况下socket发来的数据不可能是空的..那应该是出错了
                raise socket.error
            sock_state.buff_read += one_read
            sock_state.have_read +=  len(one_read)   #已经读取的数据总长度
            sock_state.need_read -= len(one_read)    #需要读取的总长度减去本地读取长度，就是下一次需要读取的长度
            sock_state.printState()

            ###开始判断协议头
            if sock_state.have_read == max_header_length:  #如果这次读取已经独到了协议头
                if(sock_state.buff_read[0:2] == '\r\n'):
                    sock_state.have_read -= 2
                    sock_state.need_read +=2
                    sock_state.buff_read = sock_state.buff_read[3:]
                    return 'readmore'

                header_said_need_read = int(sock_state.buff_read)  #读取协议头里的数据实际长度
                if header_said_need_read<= 0:
                    raise socket.error
                sock_state.need_read += header_said_need_read    #获得需要读取的数据总的长度，要算上之前可能没有读取完成的数据长度所以是相加
                sock_state.buff_read = '' #清空读取的数据缓存，为下一次读取数据正文做准备
                sock_state.printState()
                return 'readcontent'  #返回状态表示下次要读取数据正文了
            elif sock_state.need_read ==0:      #所有数据都读完了
                return 'process'                 #转入 process

            else:
                return 'readmore'    #还有数据没有读取完毕，继续读取

        except(socket.error,ValueError),msg:
            try:
                if msg.errno == 11:
                    dbgPrint('11'+msg)
                    return 'retry'
            except:
                pass
            return 'closing'

    def write(self,fd):
        '''
        通过fd，拿到state字典里的sock对象，从buff_write里读取数据,并非阻塞发送数据给客户端
        :param fd:
        :return:
        '''
        sock_state = self.conn_state[fd]
        conn = sock_state.sock_obj
        last_have_send = sock_state.have_write   #获得上一次发送数据的长度
        try:
            have_send = conn.send(sock_state.buff_write[last_have_send:])  #从上次位置开始继续发送，同事返回发送成功的数据长度
            sock_state.have_write += have_send
            sock_state.need_write -= have_send
            if sock_state.need_write == 0 and sock_state.have_write !=0:   #全部发送完毕，可以修改状态了
                sock_state.printState()
                dbgPrint('\n write data completed!')
                return 'writecomplete'
            else:
                return 'writemore'             #没有发送完毕，等待下一次epoll事件触发
        except socket.error,msg:
            return 'closing                 #发送错误就关闭'

    def run(self):
        '''
        通过run里的while循环来获得发生epoll事件的fd，并传给状态机来处理
        :return:
        '''
        while True:
            epoll_list = self.epoll_sock.poll()
            for fd,events in epoll_list:
                sock_state = self.conn_state[fd]
                if select.EPOLLHUP & events:
                    dbgPrint('EPOLLHUP')
                    sock_state.state = 'closing'
                elif select.EPOLLERR & events:
                    dbgPrint('EPOLLERR')
                    sock_state.state = 'closing'
                self.state_machine(fd)  #状态机启动

    def state_machine(self,fd):
        sock_state = self.conn_state[fd]
        self.sm[sock_state.state](fd)


class nbNet(nbNetBase):
    def __init__(self,addr,port,logic):
        dbgPrint('\n __init__:start')
        self.conn_state = {}             #初始化 state字典，记住默认的状态是accept哦
        self.listen_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM,0)
         # 开启SO_REUSEADDR，这样当监听端口处于各种xxx_WAIT的状态的时候
        # 也能正常的listen、bind
        self.listen_sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
        self.listen_sock.bind((addr,port))
        self.listen_sock.listen(10)
        self.setFd(self.listen_sock)  #把监听的sock对象放入state字典
        self.epoll_sock = select.epoll()
        self.epoll_sock.register(self.listen_sock.fileno(),select.EPOLLIN) #把监听的socket注册上EPOLLIN事件，只关心连接上的事件，默认水平触发
        self.logic = logic
        self.sm = {
            'accept':self.accept2read,
            'read':self.read2process,
            'write':self.write2read,
            'process':self.process,
            'closing':self.close,
        }
        dbgPrint('\n __init__ end,register No: %s'%self.listen_sock.fileno())

    def accept2read(self,fd):
        '''
        完成从accpet到read的处理过程，
        :param fd:
        :return:
        '''
        conn = self.accept(fd)
        self.epoll_sock.register(conn.fileno(),select.EPOLLIN) #让此FD注册EPOLL监听事件
        self.setFd(conn)
        self.conn_state[conn.fileno()].state = 'read'  #setfd以后状态默认accpet，所以要改变为read，不然会一直进入这个accept2read死循环了
        dbgPrint('\n accept-end!')

    def read2process(self,fd):
        '''
         负责处理读取数据到处理业务逻辑的状态转换
        :param fd:
        :return:
        '''
        try:
            read_ret = self.read(fd)
        except(Exception),msg:
            dbgPrint(msg)
            read_ret ='closing'    #读取中出现错误就直接关闭
        if read_ret == 'process':
            self.process(fd)        #读取完成，直接调用处理函数
        elif read_ret == 'readcontent':      #读取完协议头，还需要继续读数据
            pass
        elif read_ret == 'readmore': #没读完，继续
            pass
        elif read_ret == 'retry':  #11错误，重拾，继续读把
            pass
        elif read_ret == 'closing':   #read函数里估计哪里出错了，直接关闭
            self.conn_state[fd].state = 'closing'
            self.state_machine(fd)
        else:                                    #太阳黑子干扰。直接放弃
            raise Exception('impossibe state returned by self.read')


    def write2read(self,fd):
        '''
        完成从发送数据 到 重新等待客户端发来的响应 的状态转换
        :param fd:
        :return:
        '''
        try:
            write_ret = self.write(fd)
        except socket.error,msg:
            write_ret = 'closing'      #写入错误，直接关闭
        if write_ret == 'writemore': #数据没有写入完毕，继续写
            pass
        elif write_ret == 'writecomplete':
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            self.setFd(conn)                 #写入数据完毕,,STATE状态类再洗初始化
            self.conn_state[fd].state = 'read'  #重置以后默认是accpet状态，需要改为read
            self.epoll_sock.modify(fd,select.EPOLLIN)   #fd绑定EPOLLIN事件，会响应客户端发送数据的事件
        elif write_ret == 'closing':       #出错直接关闭
            dbgPrint()
            self.conn_state[fd].state = 'closing'
            self.state_machine(fd)


    def process(self,fd):
        '''
            此函数用于处理完成read状态以后，拿到数据，需要执行具体业务逻辑的情况
            :param fd:
            :return:
        '''
        sock_state = self.conn_state[fd]
        response = self.logic(sock_state.buff_read)
        sock_state.buff_write = '%05d%s' %(len(response),response)  #业务逻辑返回的具体结果
        sock_state.need_write = len(sock_state.buff_write)        #结果的长度放入字典
        sock_state.state = 'write'                                    #修改状态为write
        self.epoll_sock.modify(fd,select.EPOLLOUT)      #对应fd注册响应事件为EPOLLOUT
        sock_state.printState()

if __name__== '__main__':
    def logic(res):
        return (res[::-1])
    D = nbNet('0.0.0.0',333,logic)
    D.run()
