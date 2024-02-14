#!/usr/bin/env python3
#we doing kmer bitches
import sys 
k = int(sys.argv[1])
file = open(sys.argv[2],'r')
first_line=file.readline()
print(first_line)
sequence = file.read()
seq = ''.join(sequence.splitlines())
#print(seq)
#sequence='ATGCATGCATGCATGCATGC' 
dict1={}
for i in range(len(seq) - k + 1):
    kmer = seq[i:i+k]
    if kmer in dict1:
       dict1[kmer] += 1
    else:
        dict1[kmer] =1
sort = sorted(dict1.items())
sorted_dict = dict(sort)
#print(sort_data_dict)

for elements in sorted_dict:
    print("{}   {}".format(elements, sorted_dict[elements]))
#print(len(sequence))
#print(len(sequence) -k +1)
#print(len(sequence) -k)
