# search for a node in a given binary tree

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def search(root, data):
    if root is None:
        return False
    if root.data == data:
        return True
    
    lefts = search(root.left,data)
    if lefts:
        return True
    rights = search(root.right,data)
    if rights:
        return True
    
    