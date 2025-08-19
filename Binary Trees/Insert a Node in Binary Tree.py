# insert a node in binary tree

from collections import deque
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def insert(root, value):
    if root is None:
        root = Node(value)
        return root
    
    q = deque()
    q.append(root)
    while q:
        lenq = len(q)
        current = q.popleft()
        if current.left is not None:
            q.append(current.left)
        else:
            current.left = Node(value)
            return root
        
        if current.right is not None:
            q.append(current.right)
        else:
            current.right = Node(value)
            return root
        
    