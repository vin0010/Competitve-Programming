"""
https://www.hackerrank.com/challenges/picking-numbers/problem
"""
n = int(input())
arr = list(map(int, input().split()))

max_value = 1
current_max = 1
arr = sorted(arr)
t = arr[0]
for i in range(1, len(arr)):
    if abs(arr[i] - t) <= 1:
        current_max += 1
    else:
        t = arr[i]
        current_max = 1
    max_value = max(max_value, current_max)

print(max_value)


# different approach
def trial():
    my_dict = dict()
    for i in arr:
        my_dict[i] = my_dict.setdefault(i, 0) + 1

    maxi = 0
    keys = sorted(my_dict.keys())

    maxi = my_dict[keys[0]]
    current_max = maxi
    for i in range(1, len(keys) - 1):
        print("Key:", i)
        if abs(keys[i] - keys[i - 1]) == 1:
            current_max += my_dict[keys[i]]
        else:
            current_max = my_dict[keys[i]]
        maxi = max(maxi, current_max)
    print(keys)
    print(my_dict)
    print(maxi)
