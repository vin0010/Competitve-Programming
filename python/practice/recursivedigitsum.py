# https://www.hackerrank.com/challenges/recursive-digit-sum/problem
n, k = map(int, input().split())
temp = n*k%9
if temp:
    print(temp)
else:
    print(9)