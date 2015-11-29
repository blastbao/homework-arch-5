#!/usr/bin/env python 

from twisted.internet import protocol,reactor,endpoints
class Echo(protocol.Protocol):
    def dataReceived(self,data):
        self.transport.write(data)

class EchoFactory(protocol.Factory):
    def buildProtocol(self,addr):
        return Echo()

endpoints.serverFromString(reactor,"tcp:9090").listen(EchoFactory())
reactor.run()

#session 01
#$ python echo2.py

#session02
#$ telnet localhost 9090
#Trying ::1...
#telnet: connect to address ::1: Connection refused
#Trying 127.0.0.1...
#Connected to localhost.
#Escape character is '^]'.
#ls
#ls
#quit
#quit
#exit
#exit
#qqqqqqqqqqqqq
#qqqqqqqqqqqqq
#Connection closed by foreign host.



