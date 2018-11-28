"""
    https://www.hackerrank.com/challenges/no-prefix-set/problem
7
aab
defgab
abcde
abc
cedaaa
bbbbbbbbbb
jabjjjad

"""


def update_trie(names):
    trie = dict()
    _end_ = '_end_'
    # current_dict = trie
    for name in names:
        current_dict = trie
        flag = True
        for i in range(len(name)):
            if name[i] in current_dict:
                current_dict = current_dict[name[i]]
            else:
                flag = False
                current_dict[name[i]] = dict()
                current_dict = current_dict[name[i]]
            # current_dict = current_dict.setdefault(name[i], dict())

            if _end_ in current_dict:
                # print(current_dict)
                print('BAD SET')
                print(name)
                return
        if flag:
            print('BAD SET')
            print(name)
            return
        current_dict[_end_] = _end_
    # print(trie)
    print('GOOD SET')
    # print(name[:i+1]) if _end_ in current_dict else 0


my_trie = dict()

# update_trie(['add', 'act', 'adder'])

queries_rows = int(input())
queries = []

for _ in range(queries_rows):
    queries.append(input())

update_trie(queries)
