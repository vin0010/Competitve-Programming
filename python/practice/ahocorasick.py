# https://www.hackerrank.com/challenges/two-two/problem
root = dict()
_end = '_end_'

def make_trie(word):
    i = root
    current_dict = i
    for letter in word:
        current_dict = current_dict.setdefault(letter, {})
    current_dict[_end] = [word]
    return i


def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return False
    else:
        if _end in current_dict:
            return True
        else:
            return False


T=['he','she','his','hers']
for i in T:
    make_trie(i)

for i in root:
    print(root[i])

print(root)