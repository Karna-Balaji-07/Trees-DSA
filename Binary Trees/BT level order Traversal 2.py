# Binary tree level order traversal

from collections import deque

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
def traversal(root):
    if root is None:
        return []
    result = []
    q =deque()
    q.append(root)
    level = 0
    while q:
        lenq = len(q)
        result.append([])
        for i in range(lenq):
            node = q.popleft()
            result[level].append(node)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            
        level +=1
    return result[::-1]

