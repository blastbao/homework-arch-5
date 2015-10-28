#!/usr/bin/env python
# coding=utf-8
"""

format：
<a href="http://www.douban.com/group/topic/72522805/" title="【晒xiong】猜猜这是什么尺码？" class="">【晒xiong】猜猜这是什么尺码？</a>
<img src="http://img3.douban.com/view/group_topic/large/public/p34742680.jpg" alt="" class="">

"""


import re,urllib2
import time

url = 'http://www.douban.com/group/haixiuzu/'
#初始化headers
headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/    537.36' }


try:

    #构建请求的request
    request = urllib2.Request(url,headers = headers)
    #利用urlpoen获取页面代码
    response = urllib2.urlopen(request)
    #将页面转换为utf-8编码
    pageCode = response.read().decode('utf-8')

    pattern = re.compile(ur'<td class="title">\s*<a href="(.*?)" title=".*?" class="">.*?</a>\s*</td>')
    items = re.findall(pattern,pageCode)
  
    for item in items:
        page = urllib2.Request(item,headers=headers)
        response = urllib2.urlopen(page)
        posts = response.read().decode('utf-8')
 	img = re.compile(ur'<div class="topic-figure cc">\s*<img src="(.*?)" alt="" class="">\s*</div>')
        imgs = re.findall(img,posts)

	for m in imgs:
		with file(m.split("/")[-1],"wb") as f:
	            f.write(urllib2.urlopen(m).read())
		    
                time.sleep(2)

except urllib2.URLError,e:
    if hasattr(e,"code"):
	print e.code
    if hasattr(e,"reason"):
	print e.reason
