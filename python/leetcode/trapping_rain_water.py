"""
    https://leetcode.com/problems/trapping-rain-water/
    https://www.geeksforgeeks.org/trapping-rain-water/

    edge cases:
        0, 0, 0, 1, 2, 3, 2, 1, 0
        0, 3, 0, 0 , 4, 0, 0, 10
        3, 0, 0, 2, 0
        5, 0, 4, 0, 3, 0, 2, 0, 0

    Sollution:
        For any bar find biggest on the left and biggest on the right - how can you find solution from this point?

        I have to find
            How to find the trapped water.
                If you find subsequent increasing number

        Is it something related to kadane's algorithm?
        Longest sum subarray


            If I am not sure about the trapped length, how to adjust it.
        Input: arr[] = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
        Output: 6
        XXXXXXXXXX|
        XXX|XXX||X|
        _|_||_||||||

                X   -   -   -   -   -   -   -   -
                X   -   X   -   -   -   -   -   -
                X   -   X   -   X   -   -   -   -
                X   -   X   -   X   -   X   -   -
                X   -   X   -   X   -   X   -   X
                __________________________________
                5   0   4   0   3   0   2   0   1
        Left:   0   5   5   5   5   5   5   5   5
        Right:  5   4   4   3   3   2   2   1   1

        Simple variation of above scenario

                X   -   -   -   -   -   -   -   -   X
                X   -   X   -   -   -   -   -   -   X
                X   -   X   -   X   -   -   -   -   X
                X   -   X   -   X   -   X   -   -   X
                X   -   X   -   X   -   X   -   X   X
                _____________________________________
                5   0   4   0   3   0   3   0   2   5
        Left:   0   5   5   5   5   5   5   5   5   5
        Right:  4   4   3   3   2   2   1   1   5   0

        -   -   -   -   -   -   X   -   -   -   -
        -   -   X   -   -   -   X   X   -   X   -
        X   -   X   X   -   -   X   X   X   X   X
        -----------------------------------------
        1   0   2   1   0   1   3   2   1   2   1

        To find water trapped in particular cell, find left big and right big, find smallest(two)-i.
left :
"""

def small(a, b):
    return a if a<b else b

def trap(arr):
    """
    :type height: List[int]
    :rtype: int
    """
    if len(arr) <= 2:
        return 0
    left = []
    lmax = arr[0]
    rmax = arr[-1]
    right = [None] * len(arr)
    l = 0
    r = len(arr) - 1
    while l < len(arr) and r > -1:
        if arr[l] > lmax:
            lmax = arr[l]
        left.append(lmax)
        if arr[r] > rmax:
            rmax = arr[r]
        right[r] = rmax
        l += 1
        r -= 1

    result = 0
    for i in range(len(arr)-1):
        result += small(left[i], right[i]) - arr[i]
    print("Result : ", result)
    print(left)
    print(right)


trap([5, 0, 4, 0, 3, 0, 2, 0, 1, 5])
