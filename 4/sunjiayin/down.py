import os,sys
import urllib,urllib2
from multiprocessing.dummy import Pool as ThreadPool 
url = "http://dldir1.qq.com/qqfile/qq/QQ7.8/16379/QQ7.8.exe"
req = urllib2.Request(url)
response = urllib2.urlopen(req)
headers = response.headers
size_list = []
size = int(headers['Content-Length'])
download_name = open(url.split('/')[-1], "wb+")
def downsize_list():
	download_size = int(size)/4
	for num in range(4):
		start_size = num * download_size
		end_size = (num + 1) * download_size - 1
		size_list.append((start_size, end_size))
	return size_list
def download_file(list_size):
	download_req = urllib2.Request(url)
	download_req.add_header('Range', 'Bytes=' + str(list_size[0]) + '-' + str(list_size[1]))
	download_resp = urllib2.urlopen(download_req)
	download_date = download_resp.read()
	fd = os.dup(download_name.fileno())
	file = os.fdopen(fd, 'wb+')
	file.seek(list_size[0])
	file.write(download_date)
	file.close()
download_list = downsize_list()
print download_list
pool = ThreadPool(4)
pool.map(download_file,download_list)