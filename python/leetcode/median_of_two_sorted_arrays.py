
"""
    https://leetcode.com/problems/median-of-two-sorted-arrays/
    Problem:
        Find median of two sorted arrays
    Edge cases

    Solution
        if two arrays overlaps, then mid element is median(mid + next mid in case of array with even number of cells)
        if non overlap

"""


def find_median_sorted_arrays(nums1, nums2):
    result_list = []
    len1 = len(nums1)
    len2 = len(nums2)
    i = j = 0
    while i < len1 and j < len2:
        if nums1[i] < nums2[j]:
            print("less", nums1[i])
            result_list.append(nums1[i])
            i += 1
        else:
            print("more", nums2[j])
            result_list.append(nums2[j])
            j += 1

    while i < len1:
        result_list.append(nums1[i])
        i += 1
    while j < len2:
        result_list.append(nums2[j])
        j += 1
    n = len(result_list)
    if n % 2 == 0:
        print(result_list[(n//2)-1], result_list[n//2])
    else:
        print(result_list[(n//2)-1])
    print(result_list)


find_median_sorted_arrays([1, 3, 5, 7, 9], [2, 4, 6, 8, 10])