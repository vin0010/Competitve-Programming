# https://leetcode.com/problems/two-sum/description/
#Given an array of integers, return indices of the two numbers such that they add up to a specific target.
#You may assume that each input would have exactly one solution, and you may not use the same element twice.



def getCountMap(nums):
    count_map = dict()
    for i in range(0, len(nums)):
        count_map[nums[i]] = count_map.setdefault(nums[i], (0, []))
        count_map[nums[i]] = (count_map[nums[i]])
    return count_map
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
        # if tup
        # del map[nums[i]]

        #print("--->",tup)
        tup[1].pop(0)
        new_tup = (tup[0]-1, tup[1])
        #print(tup[0]-1, tup[1])
        map[nums[i]] = new_tup
        #new_tup = (tup[0]-1, tup[1])

# print(twoSum([2, 7, 11, 15], 9))
# print(twoSum([3, 3], 9))


print(getCountMap([2, 7, 11, 11, 11, 15]))