# Minimum depth of a binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

from collections import deque        
def  minimum(root):
    if root is None:
        return 0
    level =0 
    q = deque()
    q.append(root)
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left is None and node.right is None:
                return level
            else:
                if node.left :
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        level +=1
    return level

def dfs(root):
    if root.left is None and root.right is None:
        return 1
    
    if root.left is None:
        return 1 + dfs(root.right)
    if root.right is None:
        return 1 + dfs(root.left)
    return 1 + min(dfs(root.left), dfs(root.right))

