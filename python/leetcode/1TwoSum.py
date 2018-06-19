# https://leetcode.com/problems/two-sum/description/
from re import search


def twoSum(nums, target):
    map = dict()
    for i in range(0, len(nums)):
        tup = map.setdefault(nums[i], (0, []))
        x = tup[0]+1
        tup[1].append(i)
        map[nums[i]] = (x, tup[1])
    for i in map.keys():
        print(i, map[i])
    for i in range(0, len(nums)):
        #remove from map
        tup = map[nums[i]]
        print("--->",tup)
        print(tup[0]-1, tup[1].pop(0))
        #new_tup = (tup[0]-1, tup[1])


#print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 3], 9))
