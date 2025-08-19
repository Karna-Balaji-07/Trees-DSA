# Construct a binary tree from inorder and postorder traversal

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def buildTree(inorder, postorder):
    dicts = {value:index for index,value in enumerate(inorder)}
    postindex = [len(postorder)-1]
    return Tree(dicts, postorder, postindex, 0, len(inorder)-1)

def Tree(dicts, postorder, postindex, left, right):
    if left > right:
        return None
    
    rootvalue = postorder[postindex[0]]
    postindex[0] -=1
    root = Node(rootvalue)
    index = dicts[rootvalue]
    
    root.right = Tree(dicts,postorder, postindex, index+1,right)
    root.left = Tree(dicts,postorder, postindex, left,index-1)
    return root