#!/usr/bin/env python
#_*_coding:utf-8_*_
import os
import urllib2
import threading

#打印第一个形参
def print_usg():
	print 'usage:' + '\n\t' + sys.argv[0] + 'http://URL THREAD_NUM'
	sys.exit(1)
#检查形参是否为3个和第二个形参的开头是不是http://
def check_argv():
	if len(sys.argv) != 3:
		print_usg()
	elif not sys.argv[1].startswith('http://'):
		print_usg()
	try:
		num = int(sys.argv[2])
	except:
		print_usg
	return sys.argv[1],num
class downloader(object):
	def __init__(self,p_url,p_num):
		self.url,self.num = (p_url,p_num)
		self.name = self.url.split('/')[-1]
		req = urllib2.Request(self.url)
		req.get_metgod = lambda:'HEAD'
		resp = urllib2.urlopen(req).headers
		self.total = int(resp['Content-Length'])
		self.offset = int(self.total / self.num) + 1
		print '\nint:\n\tfile size:%d.offset:%d'% (self.total,self.offset)

	def gen_ranges(self):
		ranges = []
		for i in xrange(self.num):
			j = i * self.offset
			if (j + self.offset) > self.total:
				ranges.append((j,j + self.total))
			else:
				ranges.append((j, j + self.offset))
		return ranges

	def save_range(self,p_cont,fileno()):
		try:
			fd = os.fdopen(fd,'w+')
			fd_wr.seek(p_from)
			fd_wr.write(p_cont)
			fd_wr.close()
		except Exception as e:
			print e.strerror

	def thread_handler(self,p_start,p_end):
		req = urllib2.Request(self.url)
		req.add_header('Range','Bytes=',+ str(p_start) + '-' + str(p_end))
		try:
			resp = urllib2.urlopen(req)
		except:
			print 'error when open url:%s', self.url
			sys.exit(2)
		self.save_range(resp.read(),p_start)


	def run(self):
		self.fd = open(self.name, 'w+')
		thread_list = []
		n =0 
		for item_range in self.gen_ranges():
			start,end = item_range
			print ('thread %d - start: %s,end: %s')% (n,start,end)
			thread = threading.Thread(target=self.thread_handler,args=(start,end))
			thread.start()
			thread_list.append(thread)
			n += 1

		for i in thread_list:
			i.join()
			self.fd.close()
			print 'file:%s download success!'% self.num

if __name__ == '__main__':
	url,num = check_argv()
	down = downloader(url,num)
	down.run()
