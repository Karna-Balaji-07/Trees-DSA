# Deletion in Binary search tree

def inorder(root):
    curr = root.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr

def solution1(root, key):
    if root is None:
        return root
    
    if root.data > key:
        root.left = solution1(root.left, key)
    elif root.data < key:
        root.right = solution1(root.right, key)
        
    else:
        if root.left is None:
            return root.right
        
        if root.right is None:
            return root.left
        
        succ = inorder(root)
        root.data = succ.data
        root.right = solution1(root.right, succ.key)
        
    return root

def solution2(root, x):
    if not root:
        return root
    
    if root.data > x:
        root.left = solution2(root.left, x)
    elif root.data < x:
        root.right = solution2(root.right,x)
    
    if root.left is None:
        return root.right
    elif root.right is None:
        return root.left
    
    parent = root
    succ = root.right
    while succ.left:
        parent = succ
        succ = succ.left
        
    root.data = succ.data
    if parent.left == succ:
        parent.left = succ.right
    else:
        parent.right =  succ.right
        
    return root