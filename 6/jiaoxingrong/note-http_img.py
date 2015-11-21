#!/usr/bin/env python
# coding=utf-8

#导入守护进程执行模块
from daemon import Daemon
#导入socket模块
import socket
#导入时间模块
import time

#设定以'\r\n'为断句方式的请求OK的HTTP返回头
html = """HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\nContent-Length: """
#设定以'\r\n'为断句方式的请求文件不存在时的HTTP返回头
html404 = """HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 13\r\n\r\n<h1>404 </h1>"""

#定义一个父类是Daemon(含有守护进程运行程序的方法)名为agentD的子类
class agentD(Daemon):
    #定义run函数
    def run(self):
        #建立一个名为listen_fd的socket对象,socket对象的area family为AF_INET(服务器之间网络通信,其他还有AF_UNIX,只能够用于Unix系统进程间通信)、类型为SOCK_STREAM(流式socket即TCP),协议为IP
        listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        #设置该socket对象的选项,操作套接字选项时需先声明socket.SOL_SOCKET,并且设置socket对象为本地地址重用,协议号为1,是icmp协议
        listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        #设置socket对象的bind地址及端口为0.0.0.0的9000端口
        listen_fd.bind(("0.0.0.0", 9000))
        #监听地址及端口开始接受连接,设置并发数为10,超过10个之后的连接将被拒绝
        listen_fd.listen(10)
        #开启一个死循环用来不断等待处理连接
        while True:
            #等待接受连接触发accept函数,并将来源IP及端口赋值给变量conn,addr
            conn, addr = listen_fd.accept()
            #打印来源IP及端口
            print "coming", conn, addr
            #读取本地连接客户端发来的请求头的前10000个字节,并赋值给read_data
            read_data = conn.recv(10000)
            #print read_data
            #使用try捕捉错误
            try:
                #将客户端的请求头按空格切片生成一个列表,截取出该列表中的第二个元素,之后截取新的列表中的第二到最后一个元素(为客户请求资源的文件名称),将该文件名赋值给pic_name
                pic_name = read_data.split(" ")[1][1:]
                #打印pic_name
                print pic_name
                #使用file函数以只读方式打开pic_name的文件并将该句柄赋给f
                with file(pic_name) as f:
                    #读取该文件的内容赋给pic_content
                    pic_content = f.read()
                    #将读取到的文件内容的长度赋给length
                    length = len(pic_content)
                    #将一开始定义的全局变量html赋给html_resp
                    html_resp = html
                    #将上面得到的本次发送文件内容的Content-Lenth跟一开始定义的返回头内容拼接在一起赋给html_resp
                    html_resp += "%d\r\n\r\n" % (length)
                    #打印html_resp
                    print html_resp
                    #将文件内容跟响应头拼接在一起赋给html_resp
                    html_resp += pic_content
            #捕捉到任意错误时的操作
            except:
                #输出404
                print "404 occur"
                #将html_resp设置为一开始定义的404响应头
                html_resp = html404
           #设定while循环条件:html_resp返回头的长度大于0 
            while len(html_resp) > 0: 
                #将文件内容返回给客户端,并将此次发送的字节数赋给sent_cnt
                sent_cnt = conn.send(html_resp)
                #打印sent_cnt
                print "sent:", sent_cnt
                #将html_resp未发送的字节数切片并重新赋给html_resp,并再次循环,知道发送完毕
                html_resp = html_resp[sent_cnt:]
            #关闭本次连接
            conn.close()

#判断程序是否为main,而不是以模块形式导入
if __name__ == "__main__":
    #为agentD类初始化一个实例,pid文件为agetnd.pid 标准输出和标准错误输出都重定向到agetnd.log
    agentd = agentD(pidfile="agentd.pid", stdout="agentd.log", stderr="agentd.log")
    #执行run函数
    agentd.run()
