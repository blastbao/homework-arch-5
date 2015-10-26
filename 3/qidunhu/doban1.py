#!/usr/bin/env python
#########################################################################
# File Name: doban1.py
# Author: qidunhu
# mail: qidunhu@126.com
# Created Time: Mon 26 Oct 2015 10:12:46 AM CST
#########################################################################

# -*- coding: utf-8 -*-

import urllib2,urllib,re,os

page=urllib2.urlopen("http://www.douban.com/group/haixiuzu/")
html=page.read()
htmlallreg=r'http://www.douban.com/group/topic/[\d]*'
urlpattern=re.compile(htmlallreg)
urllist=urlpattern.findall(html)
imgreg=r'(http://img3.douban.com/view/group_topic/large/public.+?jpg)'
imgpattern=re.compile(imgreg)
header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
'Accept':'text/html;q=0.9,*/*;q=0.8',
'Accept-Charset':'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
'Accept-Encoding':'gzip',
'Connection':'close',
'Referer':'http://douban.com'
}
y=0
for i in urllist:
    imgpage=urllib2.urlopen(i)
    imghtml=imgpage.read()
    imgpattern.findall(imghtml)
    for x in imgpattern.findall(imghtml):
	try:
	   urllib.urlretrieve(x,'%s.jpg' % y)
	   y=y+1
	except urllib2.HTTPError, e:
	   print e.code
	   print e.reason
