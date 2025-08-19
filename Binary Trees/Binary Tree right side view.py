# Binary Tree right side view

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
from collections import deque
def rightView(root):
    if root is None:
        return None
    
    q = deque()
    result = []
    q.append(root)
    while q:
        l = len(q)
        for i in range(l):
            node = q.popleft()
            if i == l-1:
                result.append(node.data)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
                
    return result