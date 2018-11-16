"""
    https://leetcode.com/problems/merge-k-sorted-lists/
    Problem : merge k sorted linked lists
    Edge cases:

    Solution:
        Best solution is to merge 2 lists, then merge it with another etc..
"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

def print_list_node(l1):
    while l1:
        print(l1.val, end="->")
        l1 = l1.next

def merge_k_lists(lists):
    """
    :type lists: List[ListNode]
    :rtype: ListNode
    """
    result = []
    for i in range(len(lists)):

        print("started")


n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n1.next = n2
n2.next = n3
print_list_node(n1)
lists = [n1]
lists.append(n2)
lists.append(n1)
merge_k_lists(lists)