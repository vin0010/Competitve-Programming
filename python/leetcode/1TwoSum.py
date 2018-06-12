#https://leetcode.com/problems/two-sum/description/
from re import search


def twoSum(nums, target):
    map = dict()
    map1 = dict()
    for i in range(0, len(nums)):
        if nums[i] in map:
            map1[nums[i]] = i
        else:
            map[nums[i]] = i
    # print(map)

    for i in range(0, len(nums)):
        # print(nums[i])
        a=0;
        if nums[i] in map1:
            del map1[nums[i]]
            a=0
        else:
            a=1
            del map[nums[i]]
        # print("->", target-nums[i])
        if (target-nums[i]) in map:
            # print("exist")
            a = map[target - nums[i]]
            # print(i, " ", map[target-nums[i]])
            return [i, a]
        if a==0:
            map1[nums[i]] = i
        else:
            map[nums[i]] = i
print(twoSum([2, 7, 11, 15], 9 ))