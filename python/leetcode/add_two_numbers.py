"""
    https://leetcode.com/problems/add-two-numbers/
    Add two linked list numbers with different length
    edge cases:
        different length - since they are in reverse order dont worry about starting from first
        l1 is big
        l2 is big

    (2 -> 4 -> 3) + (5 -> 6 -> 4) = 7 -> 0 -> 8
    342 + 465 = 807
    while i in l1 and while  j in l2:
            add i and j
            create a node
            set value to the node(divide by 10)
            keep reminder

    123789          923789
       321           97312
    ------          ------
    987321
       123
    ------
    987444

"""
from hmac import new


def add_two_numbers(self, l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    

def print_list_node(l1):
    while l1:
        print(l1.val, end="->")
        l1 = l1.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


print("-----")
node1 = ListNode(2)
node2 = ListNode(4)
node3 = ListNode(3)
node1.next = node2
node2.next = node3

n1 = ListNode(5)
n2 = ListNode(6)
n3 = ListNode(4)
n1.next = n2
n2.next = n3
