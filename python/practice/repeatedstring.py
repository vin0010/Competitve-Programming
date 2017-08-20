#!/bin/python3
import sys

s = input().strip()
n = int(input().strip())
countlist=[]
acount=0
for i in s:
    if i=='a':
        acount+=1
        countlist.append(acount)
    else:
        countlist.append(acount)
a = ((int)(n/len(s))*acount)
b=(countlist[(n%len(s))-1]) if (n%len(s))>0 else 0
sum=a+b;
print(sum)