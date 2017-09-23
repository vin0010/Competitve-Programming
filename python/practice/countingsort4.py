#!/bin/python3
# https://www.hackerrank.com/challenges/countingsort4

result = dict()

n = int(input())
for i in range(n // 2):
    a, b = input().split(' ')
    result[int(a)] = result.setdefault(int(a), '') + '- '
for i in range(n // 2):
    a, b = input().split(' ')
    result[int(a)] = result.setdefault(int(a), '') + b + ' '

for key in sorted(result.keys()):
    print(result[key], end="")

"""
{
0: [('ab', 1), ('ef', 1), ('ab', 1), ('ef', 1), ('ij', 1), ('to', 2)],
6: [('cd', 1), ('gh', 1), ('cd', 1), ('gh', 1)], 
4: [('ij', 1), ('that', 2), ('is', 2), ('the', 2)], 
3: [('be', 2)], 
1: [('be', 2), ('or', 2)], 
5: [('question', 2)], 
2: [('not', 2), ('to', 2)]}
"""
