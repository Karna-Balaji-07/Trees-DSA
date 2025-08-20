# Sum root to leaf nodes

class Node:
    def __init__(self,data):
        self.data = data
        self.left  = None
        self.right = None
        
        
def solution(root):
    if root is None:
        return 0
    
    def dfs(root, path, paths):
        if root is None:
            return []
        path.append(root.data)
        if root.left is None and root.right is None:
            paths.append(list(path))
        dfs(root.left, path, paths)
        dfs(root.right, path, paths)
        path.pop()
    
    path = []
    paths = []
    dfs(root, path, paths)
    num = 0
    for i in paths:
        num += int("".join(map(str, i)))
    return num
        