"""
    https://www.hackerrank.com/challenges/contacts/problem
    Problem:
        contact add and search operation
"""


class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val


def create_trie(names):
    trie = dict()
    for name in names:
        current_dict = trie
        for char in name:
            if char in current_dict:
                tuple = current_dict[char]
            else:
                tuple = (1, dict())
            current_dict = current_dict.setdefault(char, {})
    return trie


print(create_trie(['add', 'ads', 'act']))
