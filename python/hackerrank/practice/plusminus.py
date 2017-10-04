n = int(input())
arr = list(map(int, input().split()))

zeros=0
positives=0
negatives=0

for i in arr:
    if i > 0:
        positives+=1
    elif i<0:
        negatives+=1
    else:
        zeros+=1
print(positives/len(arr))
print(negatives/len(arr))
print(zeros/len(arr))