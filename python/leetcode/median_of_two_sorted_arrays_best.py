
"""
    https://leetcode.com/problems/median-of-two-sorted-arrays/
    Problem:
        Find median of two sorted arrays
    Edge cases

    Solution
        if two arrays not overlaps, then mid element is median(mid + next mid in case of array with even number of cells)
        if overlap, there are 4 possibilities
        1.      _______________
                    ______
            compare start1 with start2 

        2.          ______
                _______________

        3.      ________________
                    ________________

        4.          ________________
                ________________

"""