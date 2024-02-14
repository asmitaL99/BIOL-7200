#!/usr/bin/env python3
import argparse 
import re 
argparser=argparse.ArgumentParser()
argparser.add_argument("-i", help ="this is my input file")
argparser.add_argument("-f",'-FOLD', type=int, default=70)
arg=argparser.parse_args() 

def sam2fasta(file):
	#lists
	sequence=[]
	cnt=0 
	new={}
	with open(file,'r') as f:
		for line in f:
			if (re.search(pattern='@',string=line)== NULL):
				col=lin.rstrip().split("\t")
				for i in col:
					new["name"] = ('>' + col[0])
					new["seq"] = (col[9])
				sequence.append(new)			
	return sequence,cnt



with open(str(arg.i),'r') as input1:
	f1=input1.readline()
	checkmatch=re.search(pattern='@SQ',string=f1)
	if(checkmatch is True):
		print("WE got sam")
		sequence,counts = sam2fasta(str(arg.i))



