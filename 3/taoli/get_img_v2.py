__author__ = 'Mark'
from multiprocessing.dummy import Pool as ThreadPool
import urllib2,re,time
img_list=[]
def send_request(url):
    req = urllib2.Request( url)
    req.add_header('User-agent', 'Mozilla 36.10')
    response = urllib2.urlopen(req)
    return response.read()

def handel_page(url):
        global  img_list
        pattern = re.compile(ur'http://img.*?[gif|jpg|png]{3}')
        raw = pattern.findall(send_request(url))
        img_list.extend(raw)

def write_img(url):
    f = urllib2.urlopen(url)
    with open('./download/'+urllib2.unquote(url).decode('utf8').split('/')[-1], "wb") as res:
        res.write(f.read())
    #time.sleep(0.1)

pattern = re.compile(ur'http://www.douban.com/group/topic/[\w]{1,}/')
urls = pattern.findall(send_request('http://www.douban.com/group/haixiuzu/'))
pool = ThreadPool(6)
pool.map(handel_page,urls)
pool.map(write_img,img_list)