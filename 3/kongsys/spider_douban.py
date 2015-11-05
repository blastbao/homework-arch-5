##!/usr/local/env python
# -*- coding: utf-8 -*-
import urllib2
import re

header = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36' }
def openURL(url):
    Request = urllib2.Request(url, headers=header)
    Response = urllib2.urlopen(Request)
    Content = Response.read()
    return Content
    
def grepLink(patRE, html):
    return re.findall(patRE, html)
    
GroupURL = 'http://www.douban.com/group/haixiuzu/'
Grouphtml = openURL(GroupURL)
PostPat = r'(http://www.douban.com/group/topic/\d+/)'
PostURLList = grepLink(PostPat, Grouphtml)

imgPat = r'(http://img\d.douban.com/view/group_topic/large/public/\w*.\w{3})'
for PostUrl in PostURLList:
    Posthtml = openURL(PostUrl)
    imageURLList = grepLink(imgPat, Posthtml) ]
    
    for imageUrl in imageURLList:
        imageFile = open('/home/john/Pictures/'+imageUrl[0].split('/')[-1], 'wb')
        imageFile.write(openURL(imageUrl))
