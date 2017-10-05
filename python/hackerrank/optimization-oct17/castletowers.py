n = int(input())
arr = list(map(int, input().split()))
maxi=0
count=0
maxcount=0
for i in arr:
    if i > maxi:
        maxi=i
        maxcount=max(maxcount, count)
        count=1
    elif i==maxi:
        count+=1

print(count)
# print(maxi)


