# Insertion in Binary search Tree

def solution(root,key):
    if root is None:
        return Node(key)

    if root.data < key:
        root.right = solution(root.right, key)
    else:
        root.left = solution(root.left, key)
    
    return root

def iterative(root, key):
    temp = Node(key)
    if root is None:
        return temp
    
    parent = None
    curr = root
    while curr is not None:
        parent = curr
        if curr.data > key:
            curr = curr.left
        elif curr.data < key:
            curr = curr.right
        else:
            return root
        
        if parent.data > key:
            parent.left = temp
        else:
            parent.right = temp
    return root

