# create a binary tree from inorder and preorder traversal

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def buildTree(inorder, preorder):
    dicts = {value : index for value, index in enumerate(inorder)}
    preindex = [0]
    return Tree(dicts, preorder,preindex, 0, len(inorder)-1)

def Tree(dicts, preorder, preindex,left,right):
    if left > right:
        return None
    
    rootvalue = preorder[preindex[0]]
    preindex[0] +=1
    root = Node(rootvalue)
    index = dicts[rootvalue]
    root.left = Tree(dicts, preorder, preindex, left, index-1)
    root.right = Tree(dicts, preorder, preindex, index+1, right)
    return root

