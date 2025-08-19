# Find the maximum depth of a binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque        
def BFS(root):
    q = deque()
    if root is None:
        return 0
    q.append(root)
    level = 1
    while q:
        for i in range(len(q)):
            current = q.popleft()
            if current.left:
                q.append(current.left)
            if current.right:
                q.append(current.right)
            
        level +=1
    
    return level