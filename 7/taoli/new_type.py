#!/usr/bin/env python
# encoding: utf-8
"""
@version: 1.0
@author: Mark Tao
@contact: urtop@qq.com
@file: new_type.py
@time: 2015/11/27 21:33
"""
import select,socket
max_header_length = 5000  # for http_header read only
status={
    'close':1,
    'more':2,
    'complete':3
}
EOL1 = b'\n\n'
EOL2 = b'\n\r\n'
class STATE:
    def __init__(self,sock):
        self.state = "read"
        self.have_read = 0
        self.need_read = max_header_length
        self.have_write = 0
        self.need_write = 0
        self.buff_read = ""
        self.buff_write = ""
        self.sock_obj = sock

class new_type():
    def __init__(self, conn_state, epoll_sock, logic):
        self.conn_state = STATE(conn_state)
        self.epoll_sock = epoll_sock
        self.logic = logic
        self.fd = self.conn_state.sock_obj.fileno()
        self.sm = {
            "read": self.read2process,
            "write": self.write2read,
            "process": self.process,
            "closing": self.close,
        }
        self.start_flag = 1
        # print  'init_start...'

    def read(self):
            try:
                conn = self.conn_state.sock_obj  # 拿到具体的连接对象
                if  self.conn_state.need_read <= 0:
                    raise socket.error
                res=b''
                while EOL1 not in res and EOL2 not in res:
                    res += conn.recv(1024)
                if len(res) == 0:  # 正常情况下socket发来的数据不可能是空的..那应该是出错了
                    # raise socket.error
                    return 'closing'
                self.conn_state.buff_read = res
                return 'process'
            except(socket.error), msg:
                return 'closing'

    def process(self):
        response = self.logic(self.conn_state.buff_read)
        self.conn_state.buff_write = response  # 业务逻辑返回的具体结果
        self.conn_state.need_write = len(self.conn_state.buff_write)  # 结果的长度放入字典
        self.conn_state.state = 'write'  # 修改状态为write
        self.epoll_sock.modify(self.fd, select.EPOLLOUT)  # 对应fd注册响应事件为EPOLLOUT

    def read2process(self):
            read_ret = ""
            try:
                # print 'read start'
                read_ret = self.read()
                # print 'read over'
            except (Exception), msg:
                read_ret = "closing"
            if read_ret == "process":
                # print 'go to process'
                # 数据接收完成，转换到process阶段
                self.process()
            # readcontent、readmore、retry 都不用改变socket的state
            elif read_ret == "readcontent":
                pass
            elif read_ret == "readmore":
                pass
            elif read_ret == "retry":
                pass
            elif read_ret == "closing":
                self.conn_state.state = 'closing'
                self.sm[self.conn_state.state]()
            else:
                raise Exception("impossible state returned by self.read")


    def write2read(self):
            try:
                write_ret = self.write()
            except socket.error, msg:
                write_ret = 'closing'  # 写入错误，直接关闭
            if write_ret == 'writemore':  # 数据没有写入完毕，继续写
                pass
            elif write_ret == 'writecomplete':
                # print 'write ok'
                self.conn_state.state = 'closing'
                # self.sm[self.conn_state.state]()
            elif write_ret == 'closing':  # 出错直接关闭
                self.conn_state.state = 'closing'
                # self.sm[self.conn_state.state]()

    def close(self):
        self.epoll_sock.unregister(self.fd)
        self.conn_state.sock_obj.close()
        # raw_conn.pop(fd)

    def write(self):
        conn = self.conn_state.sock_obj
        last_have_send = self.conn_state.have_write
        try:
            have_send = conn.send(self.conn_state.buff_write[last_have_send:])
            self.conn_state.have_write += have_send
            self.conn_state.need_write -= have_send
            if self.conn_state.need_write == 0 and self.conn_state.have_write != 0:
                return "writecomplete"
            else:
                return "writemore"
        except socket.error, msg:
            # 发生错误，直接关闭socket
            return "closing"

    def run(self):
        while self.start_flag:
              for fd,events in self.epoll_sock.poll():
                if fd == self.fd:
                    if (select.EPOLLERR & events) or (select.EPOLLHUP & events) or  (self.conn_state.state == 'closing'):
                        self.close()
                        # print 'closed this threading'
                        self.start_flag = 0
                        break
                    if (select.EPOLLIN & events) or (select.EPOLLOUT & events):
                        self.sm[self.conn_state.state]()
        return self.fd