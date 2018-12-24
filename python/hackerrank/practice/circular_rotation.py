"""
    https://www.hackerrank.com/challenges/circular-array-rotation/problem
"""

n, rotations, queries = map(int, input().split())
arr = list(map(int, input().split()))
# k = n % rotations if n > rotations else rotations % n
k = rotations % n
print(arr)

print("k:", k)
while queries:
    index = int(input())
    print("res:", abs(index - k))
    print(arr[abs(index - k)])


def get_index(i, shift, l):
    res = l - i
    return res

# def getIndex(i, r):
#     return
