#!/usr/bin/env python
size = 10
#size = 1024*1024

f=open('novel.txt')

cnt = 0 
while True:
    read_per = f.read(size)
    if not read_per:
        break

    else:
        if read_per.endswith(' '):
            list_per = read_per.rstrip(' ').split(' ')
            cnt += len(list_per)
           # cnt -= list_per.count('')
        else:
            list_per = read_per.split(' ')
            cnt += len(list_per)
            #cnt -= list_per.count('')
            n = f.read(1)
            if not n  == ' ':
                cnt -= 1
f.seek(-2,2)
if f.read(1) == ' ':
    cnt -= 1
cnt= cnt+1
print cnt
