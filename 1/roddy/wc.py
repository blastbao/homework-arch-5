#!/usr/bin/env python
#coding:utf8
import sys


#计算字符数函数
def countback(worddict):
	'''计算方法:获取循环过来的字典，通过以下方法
	进行匹配统计，然后返回一个计算值'''
	words=0
	for key,value in worddict.iteritems():
		if value[-1] == "" and value[1] == "":
			countdata=len([x for x in value if x.strip()])
			words += countdata
		else:
			try:
				if len(value[-1]) == 0 and not worddict[key-1][-1] == " ":
					countdata=len([x for x in value if x.strip()])
					words += countdata
				if len(value[-1][1]) == 0 and not worddict[key-1][-1] == " ":
					countdata=len([x for x in value if x.strip()])
					words += countdata
				if not [key+1][1] == " " and not len(value[-1]) == 0 :
					countdata=len([x for x in value if x.strip()])
					words += countdata - 1
			except KeyError:
				countdata=len([x for x in value if x.strip()])
				words += countdata

	return words


def getwords(vfile):
	with open(vfile,"r+") as f:
		wordscount=[]
		count=1
		worddict={}
		while True:
			getdata=f.read(1024)
			if getdata == "":
				break
			worddictlist = getdata.split("\n")
			list1=[]
			for word in worddictlist:
				newlist=word.split(" ")
				list1.extend(newlist)
			worddict[count] = list1
			count +=1
		wordscount=countback(worddict)
	print wordscount 

try:
	filename = sys.argv[1]
	getwords(filename)

except IndexError:
	print "Please input a filename!!"

except IOError:
	print "File does not exist!!"


