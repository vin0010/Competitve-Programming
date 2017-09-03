#!/bin/python3
# https://www.hackerrank.com/challenges/countingsort4
import sys
result=dict()
arr=[]
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val=val


def process_dict(i):
    if i:
        process_dict(i.left)
        # print(i.val)
        for tuple in result[i.val]:
            if tuple[1] == 1:
                arr.append("-")
            else:
                arr.append(tuple[0])
        process_dict(i.right)


# def inorder(i):
#     if i:
#         inorder(i.left)
#         print(i.val)
#         inorder(i.right)


def insert(i, val):
    if i:
        if i.val>val:
            i.left=insert(i.left,val)
            # print("Left set to {}".format(i.left.val))
        else:
            i.right = insert(i.right, val)
            # print("Right set to {}".format(i.right.val))
    else:
        i=Node(val)

    return i

root=None

n = int(input())
for i in range(n//2):
    a, b = input().split(' ')
    result[int(a)] = result.setdefault(int(a),[])+[(b,1)]
for i in range(n//2):
    a, b = input().split(' ')
    result[int(a)] = result.setdefault(int(a), []) + [(b, 2)]

for i in list(result.keys()):
    root=insert(root, i)

process_dict(root)
# for key in sorted(result.keys()):


print(" ".join(arr))
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