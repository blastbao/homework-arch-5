#!/usr/bin/env python
def cap(str):
	return str[0].islower()

if __name__=="__main__":
	a=["fda","Tdfd","dfsfd","Adfdf","lpc","Fe"]
	b=filter(cap,a)
	c=map(lambda x:len(x),b)
	d=reduce(lambda x,y:x+y,c)
	print b
	print c
	print d
