#   Binary tree paths

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def TreePaths(root):
    def sol(root, path, paths):
        if root is None:
            return paths
        
        path.append(root.data)
        if not root.left and not root.right:
            paths.append(list(path))
        else:
            sol(root.left, path, paths)
            sol(root.right, path, paths)
        
        path.pop()
        
    paths = []
    path = []
    sol(root, path, paths)
    return paths