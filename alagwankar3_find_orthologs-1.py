#!/bin/usr/python3
import sys 
import argparse
import subprocess
#Using argparse to input the files
parser = argparse.ArgumentParser()
parser.add_argument("-i1", help = "will take input file 1")
parser.add_argument("-i2", help = "will take input file 2")
parser.add_argument("-o", help = "name your output file")
parser.add_argument("-t",help = "n will be for nucleotide sequence and p will be for protein")
args = parser.parse_args()
#Now we will give this to variables
i1 = args.i1
i2 = args.i2
o = args.o
seq=args.t 
make_directory = "mkdir temp"
subprocess.call(make_directory.split())
def reciprocalblasthits(i1,i2,seq):
    if seq == "n": 
        i1_1_database = "makeblastdb -in " + str(i1) + " -dbtype nucl -out temp/i1 "
        i1_1_database_subprocess = subprocess.check_output(i1_1_database.split())

        input1_output = "blastn -db temp/i1 -query " + str(i2) + " -max_target_seqs 1 -max_hsps 1 -outfmt 6 -out temp/blastoutput1"
        input1_output_subprocess = subprocess.check_output(input1_output.split())

        i2_1_database = "makeblastdb -in " + str(i2) + " -dbtype nucl -out temp/i2 "
        i2_1_database_subprocess = subprocess.check_output(i2_1_database.split())

        input2_output = "blastn -db temp/i2 -query " + str(i1) + " -max_target_seqs 1 -max_hsps 1 -outfmt 6 -out temp/blastoutput2"
        input2_output_subprocess = subprocess.check_output(input2_output.split())
    
    elif seq == "p":
         i1_1_database = "makeblastdb -in " + str(i1) + " -dbtype prot -out temp/i1 "
         i1_1_database_subprocess = subprocess.check_output(i1_1_database.split())

         input1_output = "blastp -db temp/i1 -query " + str(i2) + " -max_target_seqs 1 -max_hsps 1 -outfmt 6 -out temp/blastoutput1"
         input1_output_subprocess = subprocess.check_output(input1_output.split())

         i2_1_database = "makeblastdb -in " + str(i2) + " -dbtype prot -out temp/i1 "
         i2_1_database_subprocess = subprocess.check_output(i2_1_database.split())

         input2_output = "blastp -db temp/i2 -query " + str(i1) + " -max_target_seqs 1 -max_hsps 1 -outfmt 6 -out temp/blastoutput2"
         input2_output_subprocess = subprocess.check_output(input2_output.split())

    else:
         print("wrong type")
#Now need to create lists 

    i1_1 = []
    i1_2 = []
    i2_1 = []
    i2_2 = []
    o1 = []
    o2 = []
    output = []
#Now we will have to add all of this in lists 

    with open("temp/blastoutput1") as file1:
        for line in file1.readlines():
            if line.startswith("lcl"):
                i1_1.append(line.split()[0])
            if line.startswith("lcl"):
                i1_2.append(line.split()[1])

    #o1.append(i1_1) 
    #o1.append(i1_2)
    #print(o1)
    for i,j in zip(i1_1,i1_2):
         o1.append(i+"\t"+j+"\n")
    
    #wordcount ="wc o1 > Readme.txt"
    #subprocess.call(wordcount.split())
    print(len(o1))

    with open("temp/blastoutput2") as file2:
        for line in file2.readlines():
            if line.startswith("lcl"):
                i2_1.append(line.split()[0])
            if line.startswith("lcl"):
                i2_2.append(line.split()[1])
    #o2.append(i2_2)
    #o2.append(i2_1) # adding the second one before so as to keep it inversed 
    #print(o2)
    for i,j in zip(i2_1,i2_2):
         o2.append(j+"\t"+i+"\n") #inversing everything to help with best hits 
    
    #wordcount1 ="wc o2 > Readme.txt"
    #subprocess.call(wordcount1.split())
    for i in o1:
        if i in o2:
           output.append(i)
           
    #wordcount2 ="wc o2 > Readme.txt"
    #subprocess.call(wordcount2.split())
    print(len(o2))
    print(len(output))
 
    return output

output_final = reciprocalblasthits(i1,i2,seq)
with open(o,'w') as op1:
    for apair in output_final:
        op1.write(apair)
remove_directory =" rm -r temp"
subprocess.call(remove_directory.split())


            





