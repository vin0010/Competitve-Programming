#https://www.hackerrank.com/challenges/equality-in-a-array
import sys
T = int(input())
countmap={}
temp=0;
list=input().split(' ')
# print(list)
# sys.exit()
for i in list:
    if i in countmap:
        countmap[i] += 1
    else:
        countmap[i] = 1
max1=0
for i in countmap.keys():
    # print(isinstance(i, str))
    max1=max(max1,countmap[i])
print(T-max1)