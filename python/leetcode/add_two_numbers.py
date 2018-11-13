"""
    https://leetcode.com/problems/add-two-numbers/
    Add two linked list numbers with different length
    edge cases:
        different length
        

    (2 -> 4 -> 3) + (5 -> 6 -> 4) = 7 -> 0 -> 8
    while i in l1 and while  j in l2:
            add i and j
            create a node
            set value to the node(divide by 10)
            keep reminder


"""