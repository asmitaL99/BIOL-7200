#!/usr/bin/env python3 
import argparse 
import sys  
import os 
import subprocess
  
#reading the input file 
parser=argparse.ArgumentParser()
parser.add_argument("-i1", help ="this is my first BED input file")
parser.add_argument("-i2", help="this is my second BED input file")
parser.add_argument("-m", help="this is the minimum overlap")
parser.add_argument("-j", "--join", help ="joining files", action="store_true")
parser.add_argument("-o", help="this is my output file", required = True)
args=parser.parse_args()
file1=args.i1
file2=args.i2
min_overlap=args.m 
outputFile = args.o
#join 
#output
#Now we need to read this file
#Lets put it into lists 

star1=[]
stop1=[]

star2=[]
stop2=[]

te1 = {}
te2 = {}
chromosomes=[]

with open(file1,'r') as bedfile:
	for line in bedfile:
		column=line.rstrip().split("\t")
		chr1 = column[0]
		star1 = column[1]
		stop1 = column[2]
		if chr1 not in te1.keys():
			te1[chr1] =[]
			chromosomes.append(chr1)
		te1[chr1].append((int(star1), int(stop1)))



with open(file2,'r') as bedfile:
	for line in bedfile:
		column=line.rstrip().split("\t")
		chr2 = column[0]
		star2 = column[1]
		stop2 =column[2]
		if chr2 not in te2.keys():
			te2[chr2] = []
		te2[chr2].append((int(star2), int(stop2)))

output = open(outputFile, 'w')

outlist1 =[]

lenTE2 = {}

for j in te2.keys():
	lenTE2[j] = len(te2[j])

for i in te2.keys():
	count = 0
	for k in range(len(te1[i])):
		while count < lenTE2[i] and te1[i][k][0] > te2[i][count][1]:
			count += 1
		for l in range(count, lenTE2[i]):
			if (int(te2[i][l][0]) <= int(te1[i][k][1])):
				if(max(int(te2[i][l][0]), int(te1[i][k][0])) > min(int(te2[i][l][1]), int(te1[i][k][1]))):
					continue
				else:
					total = int(te1[i][k][1]) - int(te1[i][k][0])
					match = min(int(te2[i][l][1]), int(te1[i][k][1])) - max(int(te2[i][l][0]), int(te1[i][k][0]))
					percent = match / total * 100
					if percent >= int(min_overlap): 
						if args.join:
							cnt = 0 
							s = s = i + " " + str(te1[i][k][0]) + " " + str(te1[i][k][1]) + " " + " " + i + " " + str(te2[i][l][0]) + " " + str(te2[i][l][1])
							cnt +=1 
							outlist1.append(s)
							#print(s)
							output.write(s + "\n")
							break
						else: 
							cnt = 0 
							s = i + " " + str(te1[i][k][0]) + " " + str(te1[i][k][1])
							cnt+=1
							outlist1.append(s)
							#print(s)
							output.write(s + "\n")	
							break	
			else:
				break  













