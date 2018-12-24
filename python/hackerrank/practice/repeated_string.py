"""
    https://www.hackerrank.com/challenges/repeated-string/problem
"""

s = input()
n = int(input())

arr = list()

current_count: int = 0
for i in range(len(s)):
    if s[i] == 'a':
        current_count += 1
        arr[i] = current_count
    print(s[i])
