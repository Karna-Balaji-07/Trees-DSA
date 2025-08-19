# Count complete tree nodes in a binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
from collections import deque
def countNodes(root):
    if root is None:
        return 0 
    q = deque()
    q.append([root])
    count = 0
    while q:
        count += len(q)
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
    return count
