####wc.py novel.txt
import sys

def wc(filename):
    f = open(filename)                  
    result = 0
    buf_size = 1024 * 1024
    read_f = f.read # loop optimization

    buf = f.read(buf_size)
    endwithspace = buf.endswith(' ') or (buf.endswith('\n'))
    while buf:
        result += len(buf.split())
        buf = read_f(buf_size)
        if ((not endwithspace) and (not buf.startswith(' '))): result -= 1
        endwithspace = buf.endswith(' ') or (buf.endswith('\n'))
    print result
    return result

def main(argv):
    if len(argv) == 1:
        print "Not enough arguments"
        return
    else:
        wc(argv[1])
	
if __name__ == "__main__":
    main(sys.argv)