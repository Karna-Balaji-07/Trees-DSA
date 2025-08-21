# Inorder successor of a BST

def leftmost(root):
    curr = root
    while root and curr.left:
        curr = curr.left
        
    return curr

def solution(root,key):
    if root is None:
        return root
    
    if root.data == key and root.right is None:
        return leftmost(root.right)    
    
    succ = None
    curr = root
    while curr:
        if key < curr.data:
            succ = curr
            curr = curr.left
        elif key >= curr.data:
            curr = curr.right
            
    return succ
