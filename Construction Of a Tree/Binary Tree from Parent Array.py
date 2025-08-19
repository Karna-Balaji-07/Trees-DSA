# Construct a binary tree from the given parent array representation

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def construction(arr):
    ref = []
    for i in range(len(arr)):
        temp = Node(i)
        ref.append(temp)
    
    for i in range(len(arr)):
        if arr[i] == -1:
            root = ref[i]
            
        else:
            if ref[arr[i]].left is None:
                ref[arr[i]].left = ref[i]
            else:
                ref[arr[i]].right = ref[i]
            
    return root

