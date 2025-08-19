# Top view of the binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
    
from collections import deque    
def topview(root):
    if root is None:
        return []
    dicts = {}
    result = []
    q = deque([(root,0)])
    while q:
        node, line = q.popleft()
        if line not in dicts:
            dicts[line] = node.data
            
        if node.left:
            q.append([(node.left,line-1)])
        if node.right:
            q.append([(node.right, line+1)])
    
    for value in sorted(dicts.values()):
        result.append(value[1])
    
    return result