"""
    https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
    Problem
        Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.
        If there is no non-empty subarray with sum at least K, return -1.
    Solution
        Brute force not going to help.
        Create a sum array - traverse it
        For any item, check if sub array sum exists


"""


def get_sum(i, arr):
    return 0 if i <= 0 else arr[i - 1]


def shortest_subarray(A, K):
    """
    :type A: List[int]
    :type K: int
    :rtype: int
    """
    sum_list = []
    current_sum = 0
    for i in A:
        current_sum += i
        sum_list.append(current_sum)
    l = len(sum_list)
    for i in range(l):
        for j in range(i, l):
            if sum_list[j] - get_sum(i, sum_list) == K:
                print("Sum of {0} to {1}".format(i, j))
                return j - i + 1
            # print(sum_list[j] - get_sum(i, sum_list))
            # val = sum_list[j] - get_sum(i, sum_list)
    # print(sum_list)
    # for i in range(3):
    #     for j in range(i, 3):
    #         print("{0} and {1}".format(i, j))


print(shortest_subarray([3, 7, 9, 1, 2, 4], 23))
print(shortest_subarray([48, 99, 37, 4, -31], 140))
