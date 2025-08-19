# Construct a binary tree from preorder and postorder traversals

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
        
def BuildTree(preorder, postorder):
    dicts = {value : index for index, value in enumerate(postorder)}
    preindex = [0]
    return Tree(dicts, preorder, preindex, 0, len(postorder)-1)

def Tree(dicts, preorder, preindex,left,right):
    if left > right:
        return None
    
    rootvalue = preorder[preindex[0]]
    root = Node(rootvalue)
    preindex[0] +=1
                                                               
    if left == right:
        return root
    
    leftRootvalue = preorder[preindex[0]]
    leftRootindex = dicts[leftRootvalue]
    
    root.left = Tree(dicts, preorder, preindex, left, leftRootindex)
    root.right = Tree(dicts, preorder, preindex, leftRootindex+1, right-1)
    return root