import heapq


def insert(leftmaxq, rightminq, i):
    if not leftmaxq and not rightminq:
        heapq.heappush(leftmaxq, i)
    else:
        # print(leftmaxq, '-', rightminq)
        left = heapq.nlargest(1, leftmaxq)[0]  # heapq._heappop_max(leftq)
        if left > i:
            heapq.heappush(leftmaxq, i)
        else:
            heapq.heappush(rightminq, i)


def delete(leftmaxq, rightminq, i):
    # print('Removing', i)
    left = heapq.nlargest(1, leftmaxq)[0]  # heapq._heappop_max(leftq)
    if left >= i:
        leftmaxq.remove(i)
    else:
        rightminq.remove(i)


def balance(leftmaxq, rightminq):
    if len(leftmaxq) - len(rightminq) == 2:
        temp = heapq._heappop_max(leftmaxq)
        heapq.heappush(rightminq, temp)
    if len(rightminq) - len(leftmaxq) == 2:
        temp = heapq.heappop(rightminq)
        heapq.heappush(leftq, temp)


def getmedian(l, r):
    # print('Median:', l, '-', rightq)
    if len(l) > len(r):
        return heapq.nlargest(1, l)[0]
    elif len(l) == len(r):
        return (heapq.nlargest(1, l)[0] + heapq.nsmallest(1, r)[0]) / 2
    else:
        return heapq.nsmallest(1, r)[0]


n, k = map(int, input().split())
arr = list(map(int, input().split()))

leftq = []
rightq = []
for i in arr[:k]:
    insert(leftq, rightq, i)
    balance(leftq, rightq)

count = 0
for i in range(k, n):
    if arr[i] >= 2 * getmedian(leftq, rightq):
        count += 1
    # print(arr[i], '', getmedian(leftq, rightq))
    delete(leftq, rightq, arr[i - k])
    balance(leftq, rightq)
    insert(leftq, rightq, arr[i])
    balance(leftq, rightq)

print(count)
"""
9 5
2 3 4 2 3 6 8 4 5

10 6
2 4 1 3 8 5 11 9 3 12


    How can I stream line 2 heap update code?
    How to update my heap after every deletion?
    
"""
