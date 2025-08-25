# Path sum 2

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        

def pathsum2(root,target):
    def sol(root, target, sums, path, paths):
        if root is None:
            return []
        
        sums += root.data
        path.append(root.data)
        if sums == target and not root.left and not root.right:
            paths.append(list(path))
        sol(root.left, target, sums,path, paths)
        sol(root.right, target, sums, path, paths)
        path.pop()
        
    path = []
    paths = []
    sol(root,target,0,path, paths)
    return paths
##