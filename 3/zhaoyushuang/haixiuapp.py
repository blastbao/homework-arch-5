#!/usr/bin/env python 

# download douban haixiuzu's group picture
import urllib2 
import urllib
import re,os,time

locateFolder="E:\\gitdir\\51reboot\\homework-arch-5\\3\\zhaoyushuang\\"
imageFolder="picture"
imageFile="imageLink.txt"

newImageFolder=locateFolder+imageFolder+"\\"
newImageLinkFile=locateFolder+imageFile

def openDoubanGroup():
    ''' Get douban group web page. '''
    url='http://www.douban.com/group/haixiuzu/discussion?start=0'
    req=urllib2.Request(url)
    response=urllib2.urlopen(req)
    html=response.read()
    #print html
    return html
 
def findTopicLink(text):
    ''' Get topic page link and save to a List.'''
    str ="http://www.douban.com/group/topic/\d+\/"
    #The topic href like : <a href="http://www.douban.com/group/topic/81120345/"
    pat=re.compile(str) 
    topicList= pat.findall(text)
    #print topicList
    #print len(topicList)
    return topicList

def openTopicLink(url):
    ''' open topic web page.'''
    req=urllib2.Request(url)
    response=urllib2.urlopen(req)
    html=response.read()
    return html

def findImageLocate(text):
    ''' find the image file URL,and return as a list.'''
    #<div class="topic-figure cc">
    # <img src="http://img3.douban.com/view/group_topic/large/public/p38019233.jpg" alt="" class="">
    #</div>

    str ="http://img3.douban.com/view/group_topic/large/public/p\d+.jpg"
    pat=re.compile(str) 
    imageList= pat.findall(text)
    #print imageList
    return imageList

def save(url):
    ''' Save Image : 1,save image link ,2 save Image .'''
    saveImageLink(url)
    saveImage(url)

def saveImageLink(url):
    ''' Save the image Link as a singe file in local .'''
    open(newImageLinkFile,'a').write(url+"\n") 

    
def saveImage(url):
    ''' Save the image File in local folder.'''
    # "http://img3.douban.com/view/group_topic/large/public/p\d+.jpg"
    templist=[]
    templist=url.split('/')
    imageName=templist[-1]
    targetFile=newImageFolder+imageName
    
    data = urllib.urlopen(url).read()
    f = file(targetFile,"wb")
    f.write(data)
    f.close()
  
def init():
    ''' init environment .'''
    if not os.path.exists(newImageFolder):
        os.mkdir(newImageFolder)   
    open(newImageLinkFile,'w').write('\n')
    os.remove(newImageLinkFile) 
    # except pass     
    
if __name__=="__main__":
    init()
    groupText=openDoubanGroup()
    topicList=findTopicLink(groupText)
    for index in range(len(topicList)):
        #print topicList[index]
        #print topicList[index]
        topicText=openTopicLink(topicList[index])
        imageList=findImageLocate(topicText)
        
        for j in range(len(imageList)):
            #print imageList[j]
            save(imageList[j])
        
    print "Job finish  ^-^ "
    
    
    
    
