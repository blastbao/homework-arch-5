#!/usr/bin/env python
#coding:utf8
import sys
import re



def countwords(list1,newlist,count):
	newword1=len([x for x in newlist if x.strip()])
	if count==1:
		list1.append(newlist)
		return newword1
	else:
		if newlist[-1] == "" and newlist[0] == "":
			list1[0]=newlist
			return newword1

		if not list1[0][-1] == "" and not newlist[0] == "":
			list1[0]=newlist
			return newword1-1

		elif  list1[0][-1] == "" and not newlist[0] == "":
			list1[0]=newlist
			return newword1

		elif newlist[0] == "":
			list1[0]=newlist
			return newword1

def getwords(vfile):
	with open(vfile,"r+") as f:
		list1=[]
		count=1
		words=0
		while True:
			getdata=f.read(1024)
			if getdata=="":
				break
			newlist = re.split('[ \n\t]',getdata)
			cc=countwords(list1,newlist,count)
			words+=cc
			count+=1
	print words
try:
	filename = sys.argv[1]
	getwords(filename)

except IndexError:
	print "Please input a filename!!"

except IOError:
	print "File does not exist!!"


