#!/usr/bin/env python
# coding=utf-8

from daemon import Daemon
import socket
import time,threading,Queue

""" 
    单线程获取连接,多线程发送请求.在获取连接后将fd获得的信息放到线程池
    ???　将上面放到线程池中　fd? 还是fd获取到的信息?
"""

html = """HTTP/1.1 200 OK\r\nContent-Type: image/jpeg\r\nConnection: close\r\nContent-Length: """
html404 = """HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\nContent-Length: 13\r\n\r\n<h1>404 </h1>"""

class getAgentD(threading.Thread):
    def __init__(self,name,q,que_lock,pidfile,stdout,stderr):
        threading.Thread.__init__(self)
        self.name=name 
        self.q=q 
        self.que_lock=que_lock
        self.pidfile=pidfile
        self.stdout=stdout
        self.stderr=stderr
        
    def run(self):
        g=getFunction(self.name,self.pidfile,self.stdout,self.stderr,self.q,self.que_lock)
        g.run()
    
class getFunction(Daemon):
    def __init__(self,name,pidfile,stdout,stderr,q,que_lock):
        Daemon.__init__(self)
        self.name=name
        self.q=q 
        self.que_lock=que_lock
        
    def run(self):
        listen_fd = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
        listen_fd.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listen_fd.bind(("0.0.0.0", 9090))
        listen_fd.listen(10)
        while True:
            #accept to create a connection
            conn, addr = listen_fd.accept()
            print "----coming", conn, addr 
            read_data = conn.recv(1000)   #10000
            #print read_data
            # regex file name
            pic_name = read_data.split(" ")[1][1:]              
            #print pic_name
            
            try:
                # get Content-Length,and re-build the html
                with file(pic_name,'rb') as f:
                    pic_content = f.read()
                    length = len(pic_content)
                    html_resp = html
                    html_resp += "%d\r\n\r\n" % (length)
                    #print html_resp
                    html_resp += pic_content
            except:
                print "----404 occur"
                html_resp = html404
            #set to queue          
            self.q.put((conn,pic_name,html_resp))
            print "----%s get picture name %s " %(self.name,pic_name)
            time.sleep(3)

class sendAgentD(threading.Thread):
    def __init__(self,name,q,que_lock,pidfile,stdout,stderr):
        threading.Thread.__init__(self)
        self.name=name 
        self.q=q 
        self.que_lock=que_lock
        self.pidfile=pidfile
        self.stdout=stdout
        self.stderr=stderr
        
    def run(self):
        g=SendFunction(self.name,self.pidfile,self.stdout,self.stderr,self.q,self.que_lock)
        g.run()
    
class SendFunction(Daemon):
    def __init__(self,name,pidfile,stdout,stderr,q,que_lock):
        Daemon.__init__(self)
        self.name=name
        self.q=q 
        self.que_lock=que_lock
        
    def run(self):
        while True:
            if not self.q.empty():
                print "====que_lock.acquire===="
                self.que_lock.acquire()
                conn,pic_name,html_resp=self.q.get()
                print "====%s send message name : %s ,%s====" %(self.name,conn,pic_name)

                while len(html_resp) > 0: 
                    sent_cnt = conn.send(html_resp)
                    print "====sent: %s====" %(sent_cnt) 
                    html_resp = html_resp[sent_cnt:]
                conn.close()
                self.que_lock.release()
                print "====que_lock.release===="
                time.sleep(3)
            time.sleep(3)
             

if __name__=="__main__":
    que=Queue.Queue(10)
    que_lock=threading.Lock()

    # start 1 thread to get socket and accept .
    getagent = getAgentD('getDaemon',que,que_lock,pidfile="agentd.pid", stdout="agentd.log", stderr="agentd.log")
    getagent.start()
    
    # start 3 threads to send picture to web page 
    for i in xrange(3):
        sendAgent = sendAgentD('sendAgent__'+ str(i),que,que_lock,pidfile="sagentd.pid", stdout="sagentd.log", stderr="sagentd.log")
        sendAgent.start()


# 加注释,多线程 ,做成线程池 ,accept 之后,fd 放到线程池(accept 单线程,send多线程)



#>python http_img_me.py
#>http://127.0.0.1:9090/3.jpg
#----coming <socket._socketobject object at 0x0000000002654A08> ('127.0.0.1', 61400)
#----getDaemon get picture name 1.jpg
#====que_lock.acquire========que_lock.acquire====
#====sendAgent__0 send message name : <socket._socketobject object at 0x0000000002654A08> ,1.jpg====
#====sent: 501359====
#
# ====que_lock.release========que_lock.acquire====
#
#----coming <socket._socketobject object at 0x0000000002654A70> ('127.0.0.1', 61402)
#----getDaemon get picture name 1.jpg ====sendAgent__2 send message name : <socket._socketobject obje
#ct at 0x0000000002654A70> ,1.jpg====
#====sent: 501359====
#====que_lock.release====
#
#----coming <socket._socketobject object at 0x0000000002654AD8> ('127.0.0.1', 61421)
#----getDaemon get picture name 2.jpg
#====sendAgent__1 send message name : <socket._socketobject object at 0x0000000002654AD8> ,2.jpg====
#====sent: 496714====
#====que_lock.release====
#----coming <socket._socketobject object at 0x0000000002654B40> ('127.0.0.1', 61422)
#----getDaemon get picture name 2.jpg
#====que_lock.acquire====
#====sendAgent__2 send message name : <socket._socketobject object at 0x0000000002654B40> ,2.jpg====
#====sent: 496714====
#====que_lock.release====
#----coming <socket._socketobject object at 0x0000000002654A70> ('127.0.0.1', 61429)
#----getDaemon get picture name 5.jpg
#====que_lock.acquire====
#====sendAgent__0 send message name : <socket._socketobject object at 0x0000000002654A70> ,5.jpg====
#====sent: 144913====
#====que_lock.release====
#----coming <socket._socketobject object at 0x0000000002654A08> ('127.0.0.1', 61430)
#----getDaemon get picture name 5.jpg
#====que_lock.acquire====
#====sendAgent__1 send message name : <socket._socketobject object at 0x0000000002654A08> ,5.jpg====
#====sent: 144913====
#====que_lock.release====
#----coming <socket._socketobject object at 0x0000000002654AD8> ('127.0.0.1', 61434)
#----getDaemon get picture name 3.jpg
#====que_lock.acquire====
#====sendAgent__1 send message name : <socket._socketobject object at 0x0000000002654AD8> ,3.jpg====
#====sent: 517342====
#====que_lock.release====
#----coming <socket._socketobject object at 0x0000000002654A08> ('127.0.0.1', 61435)
#----getDaemon get picture name 3.jpg
#====que_lock.acquire====
#====sendAgent__2 send message name : <socket._socketobject object at 0x0000000002654A08> ,3.jpg====
#====sent: 517342====
#====que_lock.release====

