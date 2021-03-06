#!/usr/bin/env python
# coding=utf-8
import urllib2
import sys
from multiprocessing import Pool
from progressbar import *
url = 'http://dldir1.qq.com/qqfile/qq/QQ7.8/16379/QQ7.8.exe'


if len(sys.argv) > 2:
    print "Usage : multiDownload.py process<default 1>"
    sys.exit(2) 
if len(sys.argv) == 2:
    process = int(sys.argv[1])
if len(sys.argv) == 1:
    process = 1
def getRange(url):
    request = urllib2.Request(url)
    request.get_method = lambda : 'HEAD'
    response = urllib2.urlopen(request)
    dataLength = response.headers['Content-Length']
    return dataLength

def sliceRange(datarange, process=1):
    Range = []
    avgRange = int(datarange) / process - 1
    start = 0
    end = 0
    for i in range(process):
        start, end = end + 1, end + avgRange
        if start == 1:
            start = 0
        if i == process-1:
            end = ''
        range_i = (start, end)
        Range.append(range_i)
    return Range

def downloader(Range):
    realRange = 'bytes=%s-%s' % Range
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.80 Safari/537.36'
    }
    headers['Range'] = realRange
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    package = response.read()
    try:
        with open('qq-multi-2.exe', 'r+') as f:
            f.seek(Range[0])
            f.write(package)
    except Exception as e:
        with open('qq-multi-2.exe','w') as f:
            f.seek(Range[0])
            f.write(package)


def main(url, process=1):
    widgets = ['Progress: ', Percentage(), ' ', Bar(marker=RotatingMarker('>-=')),
      ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=10000000).start()
    process = process
    datarange = getRange(url)
    rangeList = sliceRange(datarange,process)
    pool = Pool(process)
    pool.map(downloader,rangeList)
    pool.close()
    pool.join()
    pbar.finish()
#    for i in rangeList:
#       downloader(i) 

if __name__ == '__main__':
    main(url,process)

