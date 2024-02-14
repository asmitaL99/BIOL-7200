#!/usr/bin/env python3
import argparse 
#reading the input file 
argparser=argparse.ArgumentParser()
argparser.add_argument("-i", help ="this is my BED input file")
arg=argparser.parse_args()
#Now we need to read this file
#Lets put it into lists 
bedlist=[]
with open(arg.i,'r') as bedfile:
	for line in bedfile:
		columns=line.rstrip().split("\t")
		bedlist.append(columns)
print(len(bedlist))
# lets assign a few counters now 
count=0 
#Need one more list to count it properly 
counter=[]
#1 is end chromo 
#-1 is start chromo 
while count < len(bedlist):
	counter.append((int(bedlist[count][1]),-1))
	counter.append((int(bedlist[count][2]), 1))
	count+=1
#sorting will help in getting it in order
counter.sort()
#print(counter) 
count_1= 1
for i in range(1,len(counter)):
	count=0
	while count<len(bedlist):
		chromosome= bedlist[count][0]
		start = int(bedlist[count][1])
		stop = int(bedlist[count][2])
		if counter[i - 1][0] != counter[i][0]:
			print(chromosome, counter[i - 1][0], counter[i][0], count_1, '\t')
			if counter[i][1] == -1:
				count_1 += 1
			else:
				count_1 -= 1 
		count+=1 
