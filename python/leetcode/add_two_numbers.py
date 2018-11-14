"""
    https://leetcode.com/problems/add-two-numbers/
    Add two linked list numbers with different length
    edge cases:
        different length - since they are in reverse order dont worry about starting from first
        l1 is big
        l2 is big
    missed edge cases


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

193
329
---



"""
from hmac import new


def add_two_numbers(l1, l2):
    """
    :type l1: ListNode
    :type l2: ListNode
    :rtype: ListNode
    """
    result = i = ListNode(0)
    reminder = 0
    while l1 and l2:
        total = l1.val + l2.val + reminder
        # print("-->>", total)
        node = ListNode(total % 10)
        i.next = node
        reminder = 0 if total < 10 else total // 10
        # print("reminder:", reminder)
        l1 = l1.next
        l2 = l2.next
        i = i.next
    print_list_node(result.next)
    # print()
    while l1:  # l1 is not empty
        total = l1.val + reminder
        # print("total:", total)
        node = ListNode(total % 10)
        i.next = node
        reminder = 0 if total < 10 else total // 10
        i = i.next
        l1 = l1.next
    while l2:  # l2 is not empty
        total = l2.val + reminder
        node = ListNode(total % 10)
        i.next = node
        reminder = 0 if total < 10 else total // 10
        l2 = l2.next
        i = i.next
    print(reminder)
    if reminder > 0:
        i.next = ListNode(reminder)
    return result.next


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
node1 = ListNode(9)
node2 = ListNode(9)
node3 = ListNode(9)
node4 = ListNode(4)

node1.next = node2
node2.next = node3
node3.next = node4

n1 = ListNode(2)
n2 = ListNode(1)
# n3 = ListNode(4)
n1.next = n2
# n2.next = n3

print_list_node(node1)
print()
print_list_node(n1)
print()
print_list_node(add_two_numbers(node1, n1))
