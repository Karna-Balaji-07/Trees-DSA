# Check if the two trees are same or not

class Node:
    def __init__(self,data):
        self.data=data
        self.left = None
        self.right = None
        

def preorder(root,arr):
    if root is None:
        arr.append('Null')
        return 
    arr.append(root.data)
    preorder(root.left, arr)
    preorder(root.right, arr)


def solution1(root1, root2):
    tree1 = []
    tree2 = []
    preorder(root1,tree1)
    preorder(root2,tree2)
    if tree1 == tree2:
        return True
    return False

def check(root1, root2):
    if root1 is None and root2 is None:
        return True
    
    if root1 is None or root2 is None:
        return False
    
    return (root1.data == root2.data and check(root1.left, root2.left) and check(root1.right, root2.right))