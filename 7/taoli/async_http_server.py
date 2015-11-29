#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: async_http_server.py
@time: 2015/11/26 10:07
"""
import socket
import select
import nbNet

max_header_length = 200  # for http_header read only
http_response = """HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: Close\r\nContent-Length:"""

class async_http_server(nbNet.nbNet):
    def read(self, fd):
        try:
            sock_state = self.conn_state[fd]
            conn = sock_state.sock_obj  # 拿到具体的连接对象
            if sock_state.need_read <= 0:
                raise socket.error
            one_read = conn.recv(max_header_length)  # 第一次读取的时候，是根据协议头大小来的，之后是根据数据大小来的读的
            # dbgPrint('\t read func fd:%d,one_read:%s,need_read:%d'%(fd,one_read,sock_state.need_read))
            if len(one_read) == 0:  # 正常情况下socket发来的数据不可能是空的..那应该是出错了
                # raise socket.error
                return 'closing'
            sock_state.buff_read = one_read
            return 'process'
        except(socket.error), msg:
            return 'closing'

    def process(self, fd):
        sock_state = self.conn_state[fd]
        response = self.logic(sock_state.buff_read)
        sock_state.buff_write = response  # 业务逻辑返回的具体结果
        sock_state.need_write = len(sock_state.buff_write)  # 结果的长度放入字典
        sock_state.state = 'write'  # 修改状态为write
        self.epoll_sock.modify(fd, select.EPOLLOUT)  # 对应fd注册响应事件为EPOLLOUT
        sock_state.printState()

    def write2read(self, fd):
        try:
            write_ret = self.write(fd)
        except socket.error, msg:
            write_ret = 'closing'  # 写入错误，直接关闭
        if write_ret == 'writemore':  # 数据没有写入完毕，继续写
            pass
        elif write_ret == 'writecomplete':
            self.conn_state[fd].state = 'closing'
            self.state_machine(fd)
            # sock_state = self.conn_state[fd]
            # conn = sock_state.sock_obj
            # self.setFd(conn)                 #写入数据完毕,,STATE状态类再洗初始化
            # self.conn_state[fd].state = 'read'  #重置以后默认是accpet状态，需要改为read
            # self.epoll_sock.modify(fd,select.EPOLLIN)   #fd绑定EPOLLIN事件，会响应客户端发送数据的事件
        elif write_ret == 'closing':  # 出错直接关闭
            self.conn_state[fd].state = 'closing'
            self.state_machine(fd)


def logic(res):
    pic_name = res.split(" ")[1][1:]
    with file(pic_name, 'rb') as f:
        res = f.read()
    return http_response+ str(len(res)) + '\r\n\r\n' + res


D = async_http_server('0.0.0.0', 333, logic)
D.run()
