"""
    https://www.hackerrank.com/challenges/mini-max-sum/problem
"""


arr = list(map(int, input().split()))

mini = arr[0]
maxi = arr[0]

theSum = 0
for i in arr:
    mini = min(mini, i)
    maxi = max(maxi, i)
    theSum = theSum + i


print(theSum-maxi, theSum-mini)