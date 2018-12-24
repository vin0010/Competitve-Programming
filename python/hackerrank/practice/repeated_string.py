"""
    https://www.hackerrank.com/challenges/repeated-string/problem
"""

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
# print("a: {0}".format(a))
# print("b: {0}".format(b))
sum=a+b;
# print("((int)(n/len(s))*acount) : {0}".format(a))
# print("(countlist[n%len(s)]) if (n%len(s))>0 else 0 : {0}".format(b))
print(sum)
# print(countlist)
# print(((int)(n/len(s))*acount)+(countlist[n%len(s)]) if (n%len(s))>0 else 0) why its zero?
