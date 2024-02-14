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

#Function for backtracking 
def backtrack(matrix): 
	len1 = len(file_1)
	len2 = len(file_2) 
	#print(len1)
	#print(file_1)
	#print(file_2)
	file_1_align=""
	file_2_align=""
	temp=[]
	while(len1>0 or len2>0):
		if file_1[len1-1] == file_2[len2-1]:
			file_1_align += file_1[len1-1]
			file_2_align +=file_2[len2-1]
			len1 -= 1
			len2 -= 1
		else: 
			temp = [matrix[len1-1][len2-1], matrix[len1-1][len2], matrix[len1][len2-1]] 
			print(temp,"hi")
			if max(temp) == temp[0]:
				file_1_align+=file_1[len1-1]
				file_2_align+=file_2[len2-1]
				len1-=1
				len2-=1
			elif max(temp) == temp[1]:
				file_1_align+=file_1[len1-1]
				file_2_align+="-"
				len1-=1
			elif max(temp) == temp[-1]:
				file_1_align+="-"
				file_2_align+= file_2[len2-1]
				len2-=1
			else:
				print("exit")
	#print(file_1_align)
	#print(file_2_align)			
	#Reverse the string 
	file_1_align=file_1_align[::-1]
	file_2_align=file_2_align[::-1]			
	return temp,file_2_align,file_1_align


#print(temp)
#print(file_1_align)
#print(file_2_align)

#Now need to write the match part for output purpose
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
	cnt = 0
	length = len(matchstr)
	for i in range(length):
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
	matrix[i][0]= -1*i 
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
			#print(max(matrix[i-1][j]+gap, matrix[i][j-1]+gap, matrix[i-1][j-1]+match))
			matrix[i][j] = max(matrix[i-1][j]+gap, matrix[i][j-1]+gap, matrix[i-1][j-1]+match)
			#print(matrix)
		else: 
			#print(max(matrix[i-1][j]+gap, matrix[i][j-1]+gap, matrix[i-1][j-1]+mismatch))
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





				



