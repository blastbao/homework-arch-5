__author__ = 'Mark'
import urllib2,re,time
import Queue
from threading import  Thread
img_urls =[]
def send_request(url):
    req = urllib2.Request( url)
    req.add_header('User-agent', 'Mozilla 36.10')
    response = urllib2.urlopen(req)
    return response.read()

def handel_page(url):
        global queue
        global  img_urls
        pattern = re.compile(ur'http://img.*?[gif|jpg|png]{3}')
        raw = pattern.findall(send_request(url))
        for r in raw:
             queue.put(r)


def write_img(i,queue):
    while(queue.qsize()>0):
        # print str(i)+' thread stat ---- \n'
        url = queue.get()
        f = urllib2.urlopen(url)
        with open('./download/'+urllib2.unquote(url).decode('utf8').split('/')[-1], "wb") as res:
            res.write(f.read())
        queue.task_done()
        # print str(i)+' thread done ---\n'
        # print 'queue size: '+str(queue.qsize())+' \n'

print '----load pages--- \n'
pattern = re.compile(ur'http://www.douban.com/group/topic/[\w]{1,}/')
urls = pattern.findall(send_request('http://www.douban.com/group/haixiuzu/'))
queue = Queue.Queue()
result = map(handel_page,urls)
print '----downloading pics--- \n'
num_thread = 8
for i in range(num_thread):
    worker = Thread(target=write_img, args=(i, queue))
    worker.setDaemon(True)
    worker.start()
queue.join()
print '---done--\n'