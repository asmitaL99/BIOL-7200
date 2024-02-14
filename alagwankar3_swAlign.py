#!bin/bash/env python3
import sys 
#input the fasta files 
seq_1 = sys.argv[1]
seq_2 = sys.argv[2]
#open both fasta files and read it properly 
#print("reading files")
file_1 = ""
file_2 = "" 
with open(seq_1) as f:
	for line in f.readlines():
		if line.startswith(">"):
			continue
		else:
			file_1 += line
file_1 = file_1.rstrip("\n") 
#print(file_1)
with open(seq_2) as f:
	for line in f.readlines():
		if line.startswith(">"):
			continue
		else:
			file_2 += line
file_2 = file_2.rstrip("\n")
#print(file_2) 
#Now I need to input the matrix rules
#find the length of the sequences to start filling the matrix
len1 = len(file_1)
len2 = len(file_2)
#print(len1," is length 1")
#print(len2,"is length 2")
#Assigning the scoring system 

match = 1 
mismatch = -1 
gap = -1 
matrix = []

#Now we need to work on backtracking 
def backtrack(matrix):
	file_1_align=""
	file_2_align=""
	num = 0
	temp=[] 

	for m in range(1,len1+1):
		for n in range(1,len2+1):
			if num < matrix[m][n]:
			   num = matrix[m][n] 
			   i= m 
			   j = n 

	while matrix[i][j] != 0:
		#writing for match 
		if file_1[i-1] == file_2[j-1]:
			file_1_align += file_1[i-1]
			file_2_align += file_2[j-1]
			i -= 1
			j -= 1
		elif file_1[i-1] != file_2[j-1]:
			temp = [matrix[i-1][j-1], matrix[i-1][j], matrix[i][j-1]]

			if max(temp) == temp[0]:
				file_1_align+=file_1[i-1]
				file_2_align+=file_2[j-1]
				i-=1
				j-=1
			elif max(temp) == temp[1]:
				file_1_align+=file_1[i-1]
				file_2_align+="-"
				i-=1
			elif max(temp) == temp[-1]:
				file_1_align+="-"
				file_2_align+= file_2[j-1]
				j-=1 
			else:
				print("exit")

	#Reversed the strings 
	file_1_align=file_1_align[::-1]
	file_2_align=file_2_align[::-1]
	return temp,file_1_align,file_2_align


#match part for output purpose
def matchstr(file_1_align,file_2_align):
	matchstr=""
	for i in range(len(file_1_align)):
		if file_1_align[i] == file_2_align[i]:
			matchstr+="|"
		elif file_1_align[i] != file_2_align[i]:
			if(file_1_align[i]== "-" or file_2_align[i] == "-"):
				matchstr+=" "
			else:
				matchstr += "*"
	return matchstr 


#Calculate the score
def count(matchstr):
	cnt =0
	for i in range(len(matchstr)):
		if matchstr[i] =="|":
			cnt+= 1
		else:
			cnt+= -1
	return cnt


# to add the fasta sequences in the list matrix 
#We will need a 2d list 
for i in range(len1 + 1):
	list1 = []
	for j in range(len2+1):
		list1.append(0)
	matrix.append(list1)
#print(matrix)
#print(list1) 
#print("Initialize first column")
for i in range(len1+1):
	matrix[i][0]=-1*i 
#print("Initialize first row")
for j in range(len2+1): 
    matrix[0][j] = -1*j
#print(matrix) 
#Now we need to start filling the matrix 
for i in range(1,len1+1):
	#print(i)
	for j in range(1,len2+1):
		#print(j)
		if file_1[i-1] == file_2[j-1]:
			matrix[i][j] = max(matrix[i-1][j]+gap, matrix[i][j-1]+gap, matrix[i-1][j-1]+match)
		else:
			matrix[i][j] = max(matrix[i-1][j]+gap, matrix[i][j-1]+gap, matrix[i-1][j-1]+mismatch)
#print(matrix)

temp,file_2_align,file_1_align = backtrack(matrix)
matchstr = matchstr(file_1_align,file_2_align)
cnt = count(matchstr)

#printing final output
#print("Final output ")
print(file_1_align)
print(matchstr)
print(file_2_align)
print("Alignment score :" ,cnt) 
