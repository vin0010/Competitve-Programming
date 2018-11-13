"""
https://leetcode.com/problems/two-sum/description/
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.


"""

def get_count_map(nums):
    """
    :rtype: dict
    """
    count_map = dict()
    for i in range(0, len(nums)):
        count_map[nums[i]] = count_map.setdefault(nums[i], (0, []))
        count_map[nums[i]] = (count_map[nums[i]])
    return count_map


print(get_count_map([2, 7, 11, 11, 11, 15]))
