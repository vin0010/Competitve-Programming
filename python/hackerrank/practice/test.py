def binary_search(sorted_arr, l, r, x):
    while l <= r:
        mid = l + (r - l) // 2
        if sorted_arr[mid] == x:
            return sorted_arr[mid]
        elif sorted_arr[mid] < x and sorted_arr[mid + 1] > x:
            return sorted_arr[mid]
        elif sorted_arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return -1


# arr=[2, 4, 5, 6, 7, 9, 11, 12]
arr=[2, 3 ,4, 7]
# print(binary_search(arr, 0, 7, 7))
k=4
for i in [2]:
    value=i+k
    print('Next range:{}'.format(value))
    next_range = binary_search(arr, 0, 6, 3)
    print(next_range)
