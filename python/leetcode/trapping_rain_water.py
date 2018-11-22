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
                5   0   4   0   3   0   3   0   2
        Left:   0   5   

        Simple variation of above scenario

        X   -   -   -   -   -   -   -   -   X
        X   -   X   -   -   -   -   -   -   X
        X   -   X   -   X   -   -   -   -   X
        X   -   X   -   X   -   X   -   -   X
        X   -   X   -   X   -   X   -   X   X
        _____________________________________
        5   0   4   0   3   0   3   0   2   5


        -   -   -   -   -   -   X   -   -   -   -
        -   -   X   -   -   -   X   X   -   X   -
        X   -   X   X   -   -   X   X   X   X   X
        -----------------------------------------
        1   0   2   1   0   1   3   2   1   2   1

        To find water trapped in particular cell, find left big and right big, find smallest(two)-i.
left :
"""
