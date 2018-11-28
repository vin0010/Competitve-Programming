"""
    https://www.hackerrank.com/challenges/contacts/problem
    Problem:
        contact add and search operation
"""

def find(trie, z):
    res = 0
    current_dict = trie
    for i in z:
        if i in current_dict:
            res = current_dict[i][0]
            current_dict = current_dict[i][1]
        else :
            return 0
    return res


def create_trie(names):
    trie = dict()
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

result = create_trie(['add', 'bad', 'adder', 'ads'])
print(result)
# print(create_trie(['add', 'ads', 'act', 'bad']))
# print(find(result, 'add'))
print(find(result, 'ad'))