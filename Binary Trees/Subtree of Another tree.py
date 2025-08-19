# Subtree of another tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def solution(root, node):
    def same(root,node):
        if not root and not node:
            return  True
        if not root or not node:
            return False
        
        return root.data == node.data and same(root.left, node.left) and same(root.right, node.right)

    if not node:
        return True
    if not root:
        return False
    
    if same(root,node):
        return True
    return solution(root.left, node) or solution(root.right, node)

