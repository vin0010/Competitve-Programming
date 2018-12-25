"""
    https://www.hackerrank.com/challenges/circular-array-rotation/problem
"""


def get_index(i, shift, l):
    if i == 0:
        return l - shift
    if i >= shift:
        return i - shift
    else:
        temp = i - shift
        return l + temp


n, rotations, queries = map(int, input().split())
arr = list(map(int, input().split()))
k = rotations % n
while queries:
    index = int(input())
    # print("res:", abs(index - k))
    print(arr[get_index(index, rotations, len(arr))])
