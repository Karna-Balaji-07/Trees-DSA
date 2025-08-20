# Path sum

# Binary tree paths

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def pathsum(root,target,sums =0):
    if root is None:
        return False
    
    sums += root.data   
    if sums == target and root.left is None and root.right is None:
        return True
    return pathsum(root.left, target, sums) or pathsum(root.right, target, sums)
    