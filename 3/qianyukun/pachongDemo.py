import urllib
import urllib2
import re
import time

headers = {'user_agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.10240'}
matches = []
for i in range(10):
	req = urllib2.Request('http://www.douban.com/group/haixiuzu/discussion?start=%s' % (25*i),headers=headers)
	resp = urllib2.urlopen(req)
	top_html = resp.read()
	#print top_html
	
	p = re.compile(ur'<td class="title">\s*<a href="(.*?)" title=".*?" class="">.*?</a>\s*</td>')
	matches += re.findall(p,top_html)
	#print matches

for page in matches:
	req2 = urllib2.Request(page,headers=headers)
	resp2 = urllib2.urlopen(req2)
	botn_html = resp2.read()
	p2 = re.compile(ur'<div class="topic-figure cc">\s*<img src="(.*?)" alt="" class="">\s*</div>')
	matches2 = re.findall(p2,botn_html)
	for img in matches2:
		with file("img\\"+img.split("/")[-1],"wb") as f:
			f.write(urllib2.urlopen(img).read())
#	print matches2
#	time.sleep(1)
