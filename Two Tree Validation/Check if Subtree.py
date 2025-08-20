# check if S is present as a subtree in T

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def subtree(t,s):
    arr1  = inorder(t,[])
    arr2 = inorder(s,[])
    arrs1 = preorder(t,[])
    arrs2 = preorder(s,[])
    if arr2 in arr1 or arrs2 in arrs1:
        return True
    else:
        return  False

    
def inorder(root,arr):
    if root is None:
        return arr

    inorder(root.left,arr)
    arr.append(root.data)
    print(root.data,end=' ')
    inorder(root.right,arr)
    return arr

def preorder(root,arr):
    if root is None:
        return arr
    
    arr.append(root.data)
    preorder(root.left,arr)
    preorder(root.right,arr)
    return arr
