# python lesson01 homework
# coding: utf-8
# 统计某50G大小的英文文本中，单词的总数
# 提示：
# 1.文本可能不会换行；
# 2.可以分段读取，累计单词数；
# 3.如果开始为空格，则单词总数不便；否则单词总数-1；
# author：kang.cunhua 
# update：2015.10.17 18:00 调试通过：)



import re
fileName = "WillamShakespeare.txt"
wordsCount = 0

with open(fileName, 'r') as f:
	# 文件不以空格开头
	chunk = f.read(1000)
	if chunk[0]==' ': wordsCount+=1
	# 按块处理文件，累加计数器
	while chunk:
		#if not chunk:break
		if chunk[0]==' ': wordsCount-=1
		match = re.findall(r'[^a-zA-Z0-9]+', chunk) # 只要英文单词，删掉其他字符
        
		for i in match:chunk = chunk.replace(i, ' ')
		chunk_list = chunk.split()
		wordsCount += len(chunk_list)
		chunk = f.read(1000)
print 'words_count is', wordsCount
#1.第一次调通运行输出：
# buffer = 1000
#words_count is 1652698
#[Finished in 103.1s]
#因为print放while循环里了；
#2.第二次调通运行输出：
# buffer = 1000
#words_count is 1652698
#[Finished in 11.5s]
#把print放while循环外；

#3.第三次调通运行输出：
# buffer = 1000
# words_count is 1650501
# [Finished in 9.3s]
