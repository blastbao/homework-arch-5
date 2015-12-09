#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.1
@author: Mark Tao
@contact: urtop@qq.com
@file: telnet_version_nbNet.py
@time: 2015/11/23 10:42
"""
import socket
import select
import time

__all__ = ['nbNet']
DEBUG = 0
max_header_length = 10  # 协议头长度

# 110 for closing  101 for process   1011 for writemore    10 for 'writecomplete'      111 for accept     read for 1100     11011 for write   10011 for 'readcontent
# 10111 for readmore'
class STATE:
    def __init__(self):
        self.list = [0]*8
        self.state = 111  # 默认创建状态
        self.have_read = 0  # 已经读取的字符长度
        self.need_read = max_header_length  # 第一次读取时候长度等于协议头的长度
        self.have_write = 0  # 已经写到缓冲区的字符长度
        self.need_write = 0  # 写入字符串总长度
        self.buff_read = ''  # 存放recv函数执行以后结果，包含目前一直所有的读取结果字符
        self.buff_write = ''  # 存放所有发送过的字符，通过send函数发给客户端
        self.sock_obj = ''  # 报错sock对象


class nbNetBase:
    def setFd(self, sock):
        tmp_state = STATE()
        tmp_state.sock_obj = sock
        self.conn_state[sock.fileno()] = tmp_state

    def accept(self, fd):
        sock_state = self.conn_state[fd]
        sock = sock_state.sock_obj
        conn, addr = sock.accept()
        conn.setblocking(0)
        return conn

    def close(self, fd):
        try:
            sock = self.conn_state[fd].sock_obj
            sock.close()
        except:
            # dbgPrint('Close fd%s '%fd)
            pass
        finally:
            self.epoll_sock.unregister(fd)
            self.conn_state.pop(fd)

    def read(self, fd):
        try:
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj  # 拿到具体的连接对象
            if sock_state.need_read <= 0:
                raise socket.error
            one_read = conn.recv(sock_state.need_read)  # 第一次读取的时候，是根据协议头大小来的，之后是根据数据大小来的读的
            if len(one_read) == 0:  # 正常情况下socket发来的数据不可能是空的..那应该是出错了
                raise socket.error
            sock_state.buff_read += one_read
            sock_state.have_read += len(one_read)  # 已经读取的数据总长度
            sock_state.need_read -= len(one_read)  # 需要读取的总长度减去本地读取长度，就是下一次需要读取的长度

            if sock_state.have_read == max_header_length:  # 如果这次读取已经独到了协议头

                header_said_need_read = int(sock_state.buff_read)  # 读取协议头里的数据实际长度
                if header_said_need_read <= 0:
                    raise socket.error
                sock_state.need_read += header_said_need_read  # 获得需要读取的数据总的长度，要算上之前可能没有读取完成的数据长度所以是相加
                sock_state.buff_read = ''  # 清空读取的数据缓存，为下一次读取数据正文做准备
                return 10011  # 返回状态表示下次要读取数据正文了
            elif sock_state.need_read == 0:  # 所有数据都读完了
                return 101  # 转入 process

            else:
                return 10111  # 还有数据没有读取完毕，继续读取

        except(socket.error, ValueError), msg:
            try:
                if msg.errno == 11:
                    return 'retry'
            except:
                pass
            return 110

    def write(self, fd):
        sock_state = self.conn_state[fd]
        conn = sock_state.sock_obj
        try:
            have_send = conn.send(sock_state.buff_write[sock_state.have_write:])  # 从上次位置开始继续发送，同事返回发送成功的数据长度
            sock_state.have_write += have_send
            sock_state.need_write -= have_send
            if sock_state.need_write == 0 and sock_state.have_write != 0:  # 全部发送完毕，可以修改状态了
                return 10
            else:
                return 1011  # 没有发送完毕，等待下一次epoll事件触发
        except socket.error, msg:
            return 110                 #发送错误就关闭

    def run(self):
        while 1:
            epoll_list = self.epoll_sock.poll()
            for fd, events in epoll_list:
                sock_state = self.conn_state[fd]
                if select.EPOLLHUP & events:
                    sock_state.state = 110
                elif select.EPOLLERR & events:
                    sock_state.state = 110
                self.state_machine(fd)  # 状态机启动

    def state_machine(self, fd):
        sock_state = self.conn_state[fd]
        self.sm[sock_state.state](fd)


class nbNet(nbNetBase):
    def __init__(self, addr, port, logic):
        self.conn_state = {}  # 初始化 state字典，记住默认的状态是accept哦
        self.listen_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        self.listen_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.listen_sock.bind((addr, port))
        self.listen_sock.listen(10)
        self.setFd(self.listen_sock)  # 把监听的sock对象放入state字典
        self.epoll_sock = select.epoll()
        self.epoll_sock.register(self.listen_sock.fileno(), select.EPOLLIN)  # 把监听的socket注册上EPOLLIN事件，只关心连接上的事件，默认水平触发
        self.logic = logic
        self.sm = {
            111: self.accept2read,
            1100: self.read2process,
            11011: self.write2read,
            101: self.process,
            110: self.close,
        }

    def accept2read(self, fd):
        '''
        完成从accpet到read的处理过程，
        :param fd:
        :return:
        '''
        conn = self.accept(fd)
        self.epoll_sock.register(conn.fileno(), select.EPOLLIN)  # 让此FD注册EPOLL监听事件
        self.setFd(conn)
        self.conn_state[conn.fileno()].state = 1100  # setfd以后状态默认accpet，所以要改变为read，不然会一直进入这个accept2read死循环了
        # dbgPrint('\n accept-end!')

    def read2process(self, fd):
        '''
         负责处理读取数据到处理业务逻辑的状态转换
        :param fd:
        :return:
        '''
        try:
            read_ret = self.read(fd)
        except Exception, msg:
            read_ret = 110  # 读取中出现错误就直接关闭
        if read_ret == 101:
            self.process(fd)  # 读取完成，直接调用处理函数
        elif read_ret == 10011:  # 读取完协议头，还需要继续读数据
            pass
        elif read_ret == 10111:  # 没读完，继续
            pass
        elif read_ret == 'retry':  # 11错误，重拾，继续读把
            pass
        elif read_ret == 110:  # read函数里估计哪里出错了，直接关闭
            self.conn_state[fd].state = 110
            self.state_machine(fd)
        else:
            raise Exception()

    def write2read(self, fd):
        try:
            write_ret = self.write(fd)
        except socket.error, msg:
            write_ret = 110  # 写入错误，直接关闭
        if write_ret == 1011:  # 数据没有写入完毕，继续写
            pass
        elif write_ret == 10:
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj
            self.setFd(conn)  # 写入数据完毕,,STATE状态类再洗初始化
            self.conn_state[fd].state = 1100  # 重置以后默认是accpet状态，需要改为read
            self.epoll_sock.modify(fd, select.EPOLLIN)  # fd绑定EPOLLIN事件，会响应客户端发送数据的事件
        elif write_ret == 110:  # 出错直接关闭
            self.conn_state[fd].state = 110
            self.state_machine(fd)

    def process(self, fd):
        sock_state = self.conn_state[fd]
        response = self.logic(sock_state.buff_read)
        sock_state.buff_write = '%05d%s' % (len(response), response)  # 业务逻辑返回的具体结果
        sock_state.need_write = len(sock_state.buff_write)  # 结果的长度放入字典
        sock_state.state = 11011  # 修改状态为write
        self.epoll_sock.modify(fd, select.EPOLLOUT)  # 对应fd注册响应事件为EPOLLOUT

counter = 0
if __name__ == '__main__':
    def logic(res):
        global counter
        counter +=1
        if counter % 100000 ==0:
            print counter, time.time()
        return (res[::-1])


    D = nbNet('0.0.0.0', 333, logic)
    D.run()
