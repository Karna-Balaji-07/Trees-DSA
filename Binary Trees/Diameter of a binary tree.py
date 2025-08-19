# Diameter of a binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def diameters(root):
    def dfs(root):
        if root is None:
            return 0
        left = dfs(root.left)
        right = dfs(root.right)
        diameter = max(diameter, left++right)
        return 1 + max(left,right)
    
    diameter = 0
    dfs(root)
    return diameter



