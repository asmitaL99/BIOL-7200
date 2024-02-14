##!/usr/bin/env python3
import sys 
file1 = open(sys.argv[1], 'r')
file2 = open(sys.argv[2], 'r')
file3 = open(sys.argv[3], 'r')
file3table = []
file2table = []
file1table = []
for line in file3:
    file3table.append(line.split())
for line in file2:
    file2table.append(line.split("\t"))
#print(file2table[0])
#for genename in file3table:
#    print(genename[0])
for line in file1:
    file1table.append(line.split("\t"))
#print(file1table[0])
print('Gene CHR Start Stop')
for genename in file3table:
    for gname in file2table:
        if gname[4]==genename[0]:
             u_id=gname[0]
             for uid in file1table:
                 if uid[0]== u_id:
                    s_pos=uid[3]
                    e_pos=uid[4]
                    chromo=uid[1]                  
                    print(genename[0],chromo, s_pos, e_pos) 
