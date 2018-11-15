"""
    https://leetcode.com/problems/merge-k-sorted-lists/
    Problem : merge k sorted linked lists
    Edge cases:

    Solution
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def merge_k_lists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    for list in lists:
        print("started")
