"""
    https://www.hackerrank.com/challenges/contacts/problem
    Problem:
        contact add and search operation
"""

# !/bin/python3

import os
import sys


#
# Complete the contacts function below.
#
def find(trie, z):
    res = 0
    current_dict = trie
    for i in z:
        if i in current_dict:
            res = current_dict[i][0]
            current_dict = current_dict[i][1]
        else:
            return 0
    return res


def update_trie(trie, name):
    current_dict = trie
    for char in name:
        if char in current_dict:
            tup = current_dict[char]  # TODO
            new_tup = (tup[0] + 1, tup[1])
            current_dict[char] = new_tup
        else:
            tup = (1, dict())
            current_dict[char] = tup
        current_dict = current_dict[char][1]
    return trie


def create_trie(trie, names):
    for name in names:
        current_dict = trie
        for char in name:
            if char in current_dict:
                tup = current_dict[char]  # TODO
                new_tup = (tup[0] + 1, tup[1])
                current_dict[char] = new_tup
            else:
                tup = (1, dict())
                current_dict[char] = tup
            current_dict = current_dict[char][1]
    return trie


def contacts(queries):
    my_trie = dict()
    # print(queries)
    for x in queries:
        if x[0]=='add':
            my_trie = update_trie(my_trie, x[1])
        else :
            print(find(my_trie, x[1]))
    #
    # Write your code here.
    #

# contacts([['add', 'hack'], ['add', 'hackerrank'], ['find', 'hac'], ['find', 'hak']])

queries_rows = int(input())
queries = []

for _ in range(queries_rows):
    queries.append(input().rstrip().split())

contacts(queries)

# result = create_trie(['ask', 'add', 'bad', 'adder', 'ads'])
# print(result)
# # print(create_trie(['add', 'ads', 'act', 'bad']))
# # print(find(result, 'add'))
# print(find(result, 'a'))
