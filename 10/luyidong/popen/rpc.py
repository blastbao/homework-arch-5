import sys,os
import subprocess
import fcntl

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from nbNet.nbNetFramework import nbNet

if __name__ == '__main__':
    def logic(coming_sock_fd ,d_in):
        #return os.popen(d_in).read()
        #proc = subprocess.Popen([d_in], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        #print coming_sock_fd
        #outfile = open("popen-%d.out" % (coming_sock_fd),"rw")
        #print d_in
        #subprocess.Popen("ls -l",shell=True,stdout=open("popen.out","w"))
        #subprocess.Popen(d_in , shell=True, stdout=outfile, stderr=outfile)
        subprocess.Popen(d_in , shell=True, stdout=coming_sock_fd, stderr=coming_sock_fd)
        #out = os.popen4(d_in)
        #return proc.stdout
        #return outfile
        return None

    reverseD = nbNet('0.0.0.0',9010,logic)
    reverseD.run()
