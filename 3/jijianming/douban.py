#!/usr/bin/env python
#_*_coding:utf8_*_
import urllib
import urllib2
import re 

url = "http://www.douban.com/group/haixiuzu"
req = urllib2.Request(url)
response = urllib2.urlopen(req)
S_html = response.read()
'''
<a href="http://www.douban.com/group/topic/80766106/" title="【晒】镯子" class="">【晒】镯子</a>
http://img[1-9].douban.com/view/group_topic/large/public/p35070585.jpg
'''
s1 = re.compile(ur'<a href="(http://www.douban.com/group/topic/.*)?"')
s2 = re.compile(ur'<img src="(http://img[1-9].douban.com/.*\.jpg)')
zu_list = re.findall(s1,S_html)
for zu in zu_list:
    a = zu.split('"')[0]
    print a 
    try:
        
        req2 = urllib2.Request(a)
        reponse2 = urllib2.urlopen(req2).read()
        list_new = re.findall(s2,reponse2)
    except:
        print 'Not Found'
    print list_new
    for list in list_new:
        print list.split('/')[-1]
        f = open(list.split('/')[-1],'wb')
        tupian = urllib2.Request(list)
        #print tupian
        try:
            f.write(urllib2.urlopen(tupian).read())
        except:
            print 'Not Found'
        f.close()

'''
for i in zu_list:
    zu_list = str(i.split('"')[0])
    try:
        html = urllib2.urlopen(urllib2.Request(i)).read()
    except: 
        continue
        
        list_new = re.findall(s2,html)
        for jpg in list_new:
            print jpg
            print jpg.split('/')[-1]
            f = open(jpg.split('/')[-1]+'.jpg','wb')
            tupian = urllib2.Request(jpg)
            print tupian
            f.write(urllib2.urlopen(tupian).read())
            f.close()
            #with file(jpg.split('/')[-1],'w') as f:
             #  f.write(urllib2.urlopen(jpg).read())
'''    

    