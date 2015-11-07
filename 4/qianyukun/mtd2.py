import urllib2
import os
from multiprocessing.dummy import Pool as ThreadPool
url = 'http://dldir1.qq.com/qqfile/qq/QQ7.7/16096/QQ7.7.exe'
req = urllib2.Request(url)
req.get_method = lambda :"HEAD"
resp = urllib2.urlopen(req).headers
dataLenth = int(resp['Content-Length'])
print "file:%s" % (dataLenth)
downFile = open(url.split('/')[-1],"w+")
def download(downRange):
	downReq = urllib2.Request(url)
	downReq.headers['Range'] = 'Bytes=%s-%s' % downRange
	downResp = urllib2.urlopen(downReq)
	tmp = downResp.read()
	writeFile(tmp, downRange[0])
def writeFile(tmp, start):
	fd = os.dup(downFile.fileno())
	fd_wr = os.fdopen(fd,"r+")
	fd_wr.seek(start, 0)
	fd_wr.write(tmp)
	fd_wr.close()
sum = 0
rangeList = []
unitLenth = 100000
while sum < dataLenth:
	rangeList.append((sum, sum+unitLenth -1))
	sum += unitLenth
rangeList.pop()
rangeList.append((sum-unitLenth, dataLenth))
pool = ThreadPool(4)
pool.map(download,rangeList)
