"""
https://www.hackerrank.com/challenges/picking-numbers/problem
"""
n = int(input())
arr = list(map(int, input().split()))

my_dict = dict()
for i in arr:
    # print(i)
    my_dict[i] = my_dict.setdefault(i, 0) + 1

maxi=0
for key in sorted(my_dict.keys()):
    

print(my_dict)