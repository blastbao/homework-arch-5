import zerorpc
import os

class RPC:
    def run(self,cmd):
        return os.popen(cmd).read()

s = zerorpc.Server(RPC())
s.bind("tcp://0.0.0.0:9011")
s.run()
