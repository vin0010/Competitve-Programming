S = input()
k=int(input())

countmap={}
for i in S:
    if i in countmap:
        countmap[i]+=1
    else:
        countmap[i] = 1

t=''
for i in S:
    if i in countmap:
        if countmap[i] >= k:
            t+=i

print(t)