# Vertical order traversal of a binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

from collections import defaultdict, deque        
def  BFS(root):
    map = defaultdict(list)
    hd = 0
    
    q = deque([(root,0)])
    mini = 0
    maxi = 0
    
    while q :
        node, hd = q.popleft()
        map[hd].append(node.data)
        
        if node.left:
            q.append(((node.left, hd-1)))
        if node.right:
            q.append((node.right, hd+1))
        
        mini = min(mini, hd)
        maxi = max(maxi, hd)
        
    result = []
    for i in range(mini, maxi+1):
        result.append(map[i])
        
    return result


    