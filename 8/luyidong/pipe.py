import sys,os,socket

from nbNetFramework import nbNet

if __name__ == '__main__':
    def login_echo(d_in):
        HOST = '127.0.0.1'
        PORT = 9011
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((HOST,PORT))
        s.send("%010d%s" %(len(d_in),d_in))
        d_response = s.recv(12)
        return d_response[10:]

    echo = nbNet('0.0.0.0', 9012, login_echo)
    echo.run()

