"""
https://leetcode.com/problems/two-sum/description/
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Plan
    prepare map(int, (count, [indices]))
    for every element
        if it exist in map, increase count and update indices

    For every element
        if 2*i gives result and count>1 return first 2 elements of indices.
        else search for the reminder and get the first index and return
"""
# TODO improvise with setdefault


def get_count_map(nums):
    """
    :rtype: dict
    """
    count_map = dict()
    for i in range(0, len(nums)):
        if nums[i] in count_map:
            temp = count_map[nums[i]]
            temp[1].append(i)
            temp = (temp[0]+1, temp[1])
            count_map[nums[i]] = temp
        else:
            count_map[nums[i]] = (1, [i])
    return count_map


def print_indices(count_map, k):
    for i in count_map:
        if 2*i == k:
            print(count_map[i][1][0], count_map[i][1][1])
            break
        else:
            if k-i in count_map:
                print(count_map[i][1][0], count_map[k-i][1][0])
                break


# print(get_count_map([2, 7, 11, 11, 11, 15]))

# print_indices(get_count_map([2, 7, 11, 11, 11, 15]), 17)


nums = list(map(int, input().replace("[", "").replace("]", "").replace(",", " ").split()))
k = int(input())
print_indices(get_count_map(nums), k)