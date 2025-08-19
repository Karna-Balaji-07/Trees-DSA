# Find the diameter of the binary tree

class Node:
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None
        
def Diameter(root):
    diameter  =0 
    def solution(root):
        if root is None:
            return -1
        diameter = 0
        lefts = solution(root.left)
        rights = solution(root.right)
        diamter = max(diameter, lefts+rights)
        return 1 + max(lefts,rights)
    solution(root)
    return diameter
