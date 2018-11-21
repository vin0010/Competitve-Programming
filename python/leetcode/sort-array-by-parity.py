"""
    https://leetcode.com/problems/sort-array-by-parity/
    Problem:
        Move even to left and odd to right
    Solution:
        in a while loop, set left and right pointer and swap or move until both becomes same
"""


def sort_array_by_parity(A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    i = 0
    j = len(A) - 1

    while i < j and i < len(A) and j > -1:
        a = A[i] % 2 == 0
        b = A[j] % 2 == 1
        if a and b:
            i += 1
            j -= 1
        elif a:
            i += 1
        elif b:
            j -= 1
        else:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    return A


sort_array_by_parity([3, 1, 2, 4])
