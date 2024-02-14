#!/usr/bin/env python3
list1= [3,4,5]
n1=3
#n1 = int(input("How many elements do you want in list 1? "))
#for i in range(0, n1):
#    element = int(input())
#    list1.append(element) 
print(list1) 
list2= [5,6,7,8,9]
n2=5
#n2 = int(input("How many elements do you want? "))
#for i in range(0, n2):
#    element = int(input())
#    list2.append(element) 
print(list2) 
#find median
sum1=sum(list1)
sum2=sum(list2)
median1bycalc= sum1/n1
median2bycalc =sum2/n2
#print(median1bycalc)
#print(median2bycalc)
#print('i just printed the medians by calculating manually')
list3=[]
for i in list1:
   if(i==median1bycalc):
     list3.append(i)
for i in list2:
   if(i==median2bycalc):
      list3.append(i)
print('Now I am printing the medians from the list')       
print(list3)

