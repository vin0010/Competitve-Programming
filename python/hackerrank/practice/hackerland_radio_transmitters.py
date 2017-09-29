n, k = map(int, input().split())
arr = list(map(int, input().split()))
# arr=[1,7,8,15,16,18,19,21,23]
# n=9
# k=2
# sorted_arr = sorted(arr)
sorted_arr = []
coverage = (2 * k)
my_set = set()
for i in arr:
    my_set.add(i)

for i in my_set:
    sorted_arr.append(i)


# 7   2   4   6   5   9   12  11                          - input representation of indexes
#   1   2   3   4   5   6   7   8   9   10  11  12          -
#   -   2   -   3
# instead of binary search get next big element t
# print(sorted_arr)
def binary_search(l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        # print(mid, '---', n)
        if mid==0:
            return -2
        if sorted_arr[mid] == x:
            return mid + 1
        elif sorted_arr[mid] < x and sorted_arr[mid + 1] > x:
            return mid + 1
        elif sorted_arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -2


count = 1
# for i in sorted_arr:
index = 0
while index <= n - 1:
    next_range = binary_search(0, len(sorted_arr) - 2, sorted_arr[index] + coverage)
    # print(index, '---', sorted_arr[index], ' -- ', next_range)
    if next_range == -2:
        break
    else:
        index = next_range
    count += 1

print(count)





# while True:
#     # print("current index:{}".format(index))
#     index += coverage
#     count += 1
#     nextrange = get_next_range(index)
#     # print("next range:{}".format(nextrange))
#     if nextrange < 0:
#         # if index < n-1:
#         #     print("coming here")
#         #     count += 1
#         break
# print(count)
