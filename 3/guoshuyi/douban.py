#!/usr/bin/env python

import urllib
import urllib2
import re

url1 = "http://www.douban.com/group/haixiuzu/"


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0'}

req = urllib2.Request(url1,headers=headers)

response = urllib2.urlopen(req,timeout=10)

the_page = response.read()



p1 = re.compile(ur'\<a href="(http://www.douban.com/group/topic/.*?)"\stitle.*\sclass=""')

matches = re.findall(p1,the_page)

img_list = []


for murl in matches:
    try:
        req = urllib2.Request(murl,headers=headers)
        response = urllib2.urlopen(req,timeout=10)
        the_page2 = response.read()
        print the_page2
        p = re.compile(ur'<div class="topic-figure cc">\s*<img src="(.*?)" alt="" class="">\s*</div>')
        pmatches = re.findall(p,the_page2)
        print pmatches
        img_list.extend(pmatches)
    except:
        pass
print img_list
