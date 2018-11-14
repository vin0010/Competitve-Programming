"""
    https://leetcode.com/problems/reverse-integer/

"""
def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x < (-2 ** 31) or x > ((2 ** 31) - 1):
        return 0
    if x > 0:
        return int(str(x)[::-1])
    else:
        v = abs(x)
        return int('-' + str(v)[::-1])