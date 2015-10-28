#!/usr/bin/env python
#coding=utf-8


import urllib, urllib2, re
import time, os

def return_html(url = 'http://www.douban.com/group/haixiuzu/'):

    req = urllib2.Request(url)
    response = urllib2.urlopen(req)
    html = response.read()
#    print html
    return html

html1 = return_html()
'''
<td class="title">
                    <a href="http://www.douban.com/group/topic/76960919/" title="【晒】虎牙" class="">【晒】虎牙</a>
                                    </td>
'''


p = re.compile(ur'''<td class="title">\s*<a href="(.*)"\stitle''')
matches = re.findall(p, html1)
#print matches
pics = []
for url in matches:
    html2 = return_html(url)
    p = re.compile(ur'''<div class="topic-figure\s.*\s.*<img src="(.*)"\salt''')
    matches = re.findall(p,html2)
#    print matches
    time.sleep(0.5)
    pics.extend(matches)
if not os.path.exists('pics'):
    os.mkdir('./pics') 
for m in pics:
    with file('./pics/'+m.split("/")[-1], "w") as f:
        print 'Downloading : ' + m
        f.write(urllib2.urlopen(m).read())
