counter=0
class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val=val


def inorder(i):
    if i:
        inorder(i.left)
        global counter
        if counter==n//2:
            print(i.val)
        counter+=1
        inorder(i.right)


def insert(i, val):
    if i:
        if i.val>val:
            i.left=insert(i.left,val)
        else:
            i.right = insert(i.right, val)
    else:
        i=Node(val)

    return i

root=None
n = int(input())
arr=input().split(' ')
for i in arr:
    root=insert(root, int(i))
inorder(root)