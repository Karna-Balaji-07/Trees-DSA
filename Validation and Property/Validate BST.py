# Validate binary search tree

def soln(root, low = float('-inf'), high  = float('inf')):
    if root is None:
        return True
    
    if not (low < root.val < high):
        return False
    return (soln(root.left, low, root.val) and soln(root.right, root.val, high))
