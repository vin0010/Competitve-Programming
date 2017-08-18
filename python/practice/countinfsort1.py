#https://www.hackerrank.com/challenges/countingsort1

T = int(input())
list = input().split()
countmap={}
for i in list:
    i=int(i)
    if i in countmap:
        countmap[i]+=1
    else:
        countmap[i] = 1

for i in range(100):
    if i in countmap:
        print(countmap[i], end=' ')
    else:
        print(0,end=' ')