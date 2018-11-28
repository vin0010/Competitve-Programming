"""
    https://www.hackerrank.com/challenges/no-prefix-set/problem

"""

def update_trie(names):
    trie = dict()
    # current_dict = trie
    for name in names:
        current_dict = trie
        for char in name:
            if char in current_dict:
                current_dict = current_dict.setdefault(char, {})
            else:
                tup = (1, dict())
                current_dict[char] = tup

        current_dict = current_dict[char][1]
    return trie


my_trie = dict()

print(update_trie(my_trie, 'add'))