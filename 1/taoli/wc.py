__author__ = 'Mark'
dataset={}
string_prev=''
def get_real_word(raw):
    global string_prev;
    temp_string =''
    for s in raw:
        if (s!=' '):
            string_prev+=s
        else:
            if(string_prev!=''):
                dataset[string_prev] =  dataset.get(string_prev,0)+1
                string_prev = ''
    print dataset

file= open('test')

while(True):
    res = file.read(3)
    if not res:
        break
    else:
       get_real_word(res)

