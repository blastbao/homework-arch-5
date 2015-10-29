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
PostPat = r'(\shref="http://www.douban.com/group/topic/\d+/")'
PostURLList = [ x.replace(r' href="', '').replace(r'"', '') for x in grepLink(PostPat, Grouphtml) ]

imgPat = r'<img\ssrc=".*"\salt'
for PostUrl in PostURLList:
    Posthtml = openURL(PostUrl)
    imageURLList = [ x.split()[1].replace("src=\"", '').replace('\"', '') for x in grepLink(imgPat, Posthtml) ]
    
    for imageUrl in imageURLList:
        imageFile = open('/home/john/Pictures/'+imageURLList[0].split('/')[-1], 'wb')
        imageFile.write(openURL(imageUrl))
