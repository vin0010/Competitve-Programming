"""
    https://leetcode.com/problems/to-lower-case/
"""


def toLowerCase(self, str):
    """
    :type str: str
    :rtype: str
    """
    result = ''
    for i in str:
        result += i.lower()
    return result
