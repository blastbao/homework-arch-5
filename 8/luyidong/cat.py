import sys,os,socket
from nbNetFramework import nbNet

if __name__ == '__main__':
    def echo(d_in):
        #ret = send
        print d_in
        #ret = ("%010d%s" %(len(d_in),d_in))
        return d_in
        #if ret:
        #    return("ok")
        #else:
        #    return("ER")
    transD = nbNet('0.0.0.0',9011,echo)
    transD.run()
