#coding=utf-8
#!/usr/bin/python2.7
#__author__ = 'louis'

from Queue import Queue
import socket
import threading
import SocketServer
from SocketServer import ThreadingMixIn

html = """HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\nContent-Length: """
html404 = """HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 13\r\n\r\n<h1>404 </h1>"""

"""
使用ThreadingMixIn支持异步，其在有新的请求时,创建一个新的线程,在该线程中处理请求
1.定义一个请求处理类 ，作为BaseRequestHandler的子类并重载handle（）
2.生成server类
3.调用server对象的handle_request()

"""

class ThreadedTCPRequestHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        try:
            pic_name = data.split(" ")[1][1:]   #截取图片名字
            print pic_name
            with file(pic_name) as f: #打开指定的图片，并读取
                pic_content = f.read()                                #
                length = len(pic_content)#统计图片的长度
                html_resp = html #
                html_resp += "%d\r\n\r\n" % (length) #打印长度
                print html_resp #打印html
                html_resp += pic_content #打印文件名
        except:
            print "404 occur"   #如果不存在，报404
            html_resp = html404
        self.request.sendall(html_resp) #发送图片
        self.request.close() #关闭套接字

class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):

    numThreads = 5

    def serve_forever(self):
        self.requests = Queue(self.numThreads) # 队列大小

        for x in range(self.numThreads):
            t = threading.Thread(target=self.process_request_thread)
            t.setDaemon(1)#设定守护线程
            t.start()

        while True:
            self.handle_request()#调用server的handl_request()对象

        self.server_close()

    def process_request_thread(self):
        #从队列中GET请求
        while True:
            ThreadingMixIn.process_request_thread(self, *self.requests.get())

    def handle_request(self):
        # 把请求PUT到队列中
        try:
            request, client_address = self.get_request()
        except socket.error:
            return
        if self.verify_request(request, client_address):
            self.requests.put((request, client_address))

if __name__ == "__main__":
    #指定IP端口
    HOST, PORT = "0.0.0.0", 8888
    #实力服务器类
    server = ThreadedTCPServer((HOST, PORT), ThreadedTCPRequestHandler)
    #接收客户端的连接
    ip, port = server.server_address
    #请求做多线程处理
    server_thread = threading.Thread(target=server.serve_forever)
    #主线程结束的时候退出server线程
    server.serve_forever()
