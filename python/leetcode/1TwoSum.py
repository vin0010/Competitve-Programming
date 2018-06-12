#https://leetcode.com/problems/two-sum/description/
from re import search


def twoSum(nums, target):
    map = dict()
    for i in range(0, len(nums)):
       map[nums[i]] = i
    print(map)
    for i in range(0, len(nums)):
        # print(nums[i])
        del map[nums[i]]
        # print("->", target-nums[i])
        if (target-nums[i]) in map:
            # print("exist")
            a = map[target - nums[i]]
            # print(i, " ", map[target-nums[i]])
            return [i, a]
        map[nums[i]] = i
print(twoSum([2, 7, 11, 15], 9 ));