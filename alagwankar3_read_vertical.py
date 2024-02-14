#!/usr/bin/env python3
import sys
k = int(sys.argv[1])
#file = open(sys.argv[2], 'r')
#sequence = file.read()
newtable=[]
r=0
w=0
c=0
with open(sys.argv[2],'r') as file:
       
        # reading each line    
            for line in file:
                newtable.append(line.split())
                r+=1
                for i in newtable[0]:
                    w+=1
c=w/r
print(c)
if k == 0:
    print("ERROR")
elif k > c:
    print("ERROR")
else:
    for i in range(r-1):
        print(newtable[i][k-1])
