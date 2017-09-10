class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val=val


def inorder(i):
    if i:
        inorder(i.left)
        print(i.val)
        inorder(i.right)


def insert(i, val):
    if i:
        if i.val>val:
            i.left=insert(i.left,val)
            # print("Left set to {}".format(i.left.val))
        else:
            i.right = insert(i.right, val)
            # print("Right set to {}".format(i.right.val))
    else:
        i=Node(val)

    return i

root=None
for i in [9,8,7,6,5,4,3,2,1]:
    root=insert(root, i)
# root=insert(root, 13)
# root=insert(root, 4)
# root=insert(root, 7)
# root=insert(root, 1)
# root=insert(root, 3)

# print("Root{}".format(root.val))
inorder(root)
