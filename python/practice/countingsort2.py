#!/bin/python3
# https://www.hackerrank.com/challenges/countingsort2
import sys

def count_sort(arr):
    result=dict()
    for s in arr:
        result[int(s)]=result.setdefault(int(s),0)+1
    return result

n = int(input())
arr=input().split(' ')
result=count_sort(arr)
for i in sorted(result.keys()):
    for temp in range(result[i]):
        print(i, end=' ')