#!/bin/env python
#encoding:utf-8
import urllib,urllib2,re

class crawlerImg(object):
    def __init__(self,url,host):
        self.url = url 
        self.host = host
        self.headValue = { 
            'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2490.71 Safari/537.36',
            'host' : host
        }   
        self.headers = urllib.urlencode(self.headValue)
        self.request = urllib2.Request(self.url,self.headers)
        self.response = urllib2.urlopen(self.request)
        self.htmlCode = self.response.read() 
            
    def getsubUrl(self):
        subRe = re.compile('a href="(.+?)\/"')
        subUrl = subRe.findall(self.htmlCode)
        if subUrl:
            return subUrl
        else:
            return False

    def getImg(self):
       imgRe = re.compile('img src="(.+?\.jpg)"') 
       imgUrl = imgRe.findall(self.htmlCode)
       for img in imgUrl:
           imgName = img.split('/')[-1]
           print 'Download %s' % img
           urllib.urlretrieve(img,'%s' % imgName)

    def main(self):
        self.getImg()
        result = self.getsubUrl()
        if not result == False:
            try:
                for childUrl in result:
                    surl = crawlerImg(childUrl,'www.douban.com')
                    surl.main()
            except:
                pass
        else:
            return 'Download finshed!'
 
douban = crawlerImg('http://www.douban.com/group/haixiuzu/','www.douban.com')
douban.main()
