#!/usr/bin/env python
import threading
import urllib2
import sys
if len(sys.argv) != 2:
    print "Error ! Parameter is not enough!"
    print "Usage: python multireq.py xx.jpg"
    sys.exit(2)
else:
    img = sys.argv[1]
class Th(threading.Thread):
    def __init__(self, name, img):
        threading.Thread.__init__(self)
        self.name = name
        self.img = img
    
    def run(self):
        url = 'http://127.0.0.1:40000/%s' % self.img
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        package = response.read()
        try:
            with open(self.name+'.jpg', 'w') as f:
                f.write(package)
        except Exception as e:
            print e

if __name__ == "__main__":
    thlist = []
    for i in range(8):
        thread = Th(i, img)
        thlist.append(thread)
        thread.start()

    for i in thlist:
        i.join
