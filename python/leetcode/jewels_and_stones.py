"""
    https://leetcode.com/problems/jewels-and-stones/

"""


def find_jewels(a, b):
    x = dict()
    for i in b:
        x[i] = x.setdefault(i, 0) +1
    result =0
    for i in a:
        result += x[i] if i in x else 0
    print(result)


find_jewels(
    "x",
    "vinotttthhh"
)