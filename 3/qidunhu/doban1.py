#!/usr/bin/env python
#########################################################################
# File Name: doban1.py
# Author: qidunhu
# mail: qidunhu@126.com
# Created Time: Mon 26 Oct 2015 10:12:46 AM CST
#########################################################################

# -*- coding: utf-8 -*-

import urllib2,urllib,re

page=urllib2.urlopen("http://www.douban.com/group/haixiuzu/")
html=page.read()
htmlallreg=r'http://www.douban.com/group/topic/[\d]*'
urlpattern=re.compile(htmlallreg)
urllist=urlpattern.findall(html)
imgreg=r'src=(.+?jpg)'
imgpattern=re.compile(imgreg)
tmpreg=r'(h.+?jpg)'  
tmppattern=re.compile(tmpreg)

for i in urllist:
    imgpage=urllib2.urlopen(i)
    imghtml=imgpage.read()
tmpimglist=imgpattern.findall(imghtml)
y=0
for x in tmpimglist:
	tmppage=urllib2.urlopen(x)
	tmphtml=tmppage.read()
	tmpurl=tmppattern.findall(tmphtml)
	urllib.urlretrieve(tmpurl,'%s'.jpg %y)
	y+=1
