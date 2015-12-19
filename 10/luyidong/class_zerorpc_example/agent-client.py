import zerorpc
c = zerorpc.Client()
c.connet("tcp://127.0.0.1:9010")
b = c.run("uname -a")
print b
