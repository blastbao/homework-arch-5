#!/usr/bin/env python
import sys
file1 = sys.argv[1]
letters = {"a":'',"b":'',"c":'',"d":'',"e":'',"f":'',"g":'',"h":'',"i":'',"j":'',"k":'',"l":'',"m":'',"n":'',"o":'',"p":'',"q":'',"r":'',"s":'',"t":'',"u":'',"v":'',"w":'',"x":'',"y":'',"z":'',"A":'',"B":'',"C":'',"D":'',"E":'',"F":'',"G":'',"H":'',"I":'',"J":'',"K":'',"L":'',"M":'',"N":'',"O":'',"P":'',"Q":'',"R":'',"S":'',"T":'',"U":'',"V":'',"W":'',"X":'',"Y":'',"Z":'',}
num_sum = 0
with open(file1,'r') as f:
	while True:
		i = f.read(1)
		if i:
			if i in letters:
				#print i
				while True:
					i = f.read(1)
					if i:
						if i not in letters:
							num_sum += 1
							break
					else:
						break
		else:
			break
print num_sum
