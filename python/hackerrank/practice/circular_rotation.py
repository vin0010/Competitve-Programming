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


# def getIndex(i, r):
#     return

# print(get_index(0, 6, 8))
# exit(0)
n, rotations, queries = map(int, input().split())
arr = list(map(int, input().split()))
# k = n % rotations if n > rotations else rotations % n
k = rotations % n
# print(arr)

# print("k:", k)
while queries:
    index = int(input())
    # print("res:", abs(index - k))
    print(arr[get_index(index, rotations, len(arr))])
