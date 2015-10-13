import re 

import time 
read_len = 1 
end_str = " "
count = 0 
f = open("test.txt")
def read_file(f, read_len=read_len):
    words = f.read(read_len)
    while words:
        while not words.endswith(end_str) and words:
            str1 = f.read(1)
            'read end break'
            if not str1:
                break 
            words += str1
        yield  words
        words = f.read(read_len)

for words in read_file(f):
    words = re.split(r"(?:\s)\s*", words.strip())
    count += len(words)
print count 
