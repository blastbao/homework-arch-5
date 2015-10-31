import urllib
import urllib2
import re
url="http://www.douban.com/group/haixiuzu/"
def geturl(strurl):
   headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36',
        'cookie':'bid="eFv50RNBoTA"; ll="108288"; __utmt=1; _pk_id.100001.8cb4=1661373936c24daa.1446305376.1.1446305651.1446305376.; _pk_ses.100001.8cb4=*; __utma=30149280.1074281686.1446305377.1446305377.1446305377.1; __utmb=30149280.8.10.1446305377; __utmc=30149280; __utmz=30149280.1446305377.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)'}
   req=urllib2.Request(strurl,headers=headers)
   response=urllib2.urlopen(strurl)
   the_page=response.read()
   return the_page
def gethttp(page,num):	
   if  num == 'a':
		mate=re.compile(ur'<a\shref="http:(.*?)"\stitle=".*?"')
   elif num == 'b':
		mate=re.compile(ur'<img\ssrc="(.*?)"\salt=".*?"\sclass="">')
   return mate.findall(page)
page1=geturl(url)
mate1=gethttp(page1,'a')
for m1 in mate1:
	print m1
	url2="http:"+m1
	page2=geturl(url2)
	mate2=gethttp(page2,'b')
	for m2 in mate2:
		if len(m2) != 0 :
			with file(m2.split("/")[-1],"wb") as f:
				f.write(urllib2.urlopen(m2).read())
			print 'ok'