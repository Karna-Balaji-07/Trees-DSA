# Remove half nodes

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
def printInorder(root):
    if root is not None:
        printInorder(root.left)
        print (root.data,end=" ")
        printInorder(root.right)

def removal(root):
    if root is None:
        return None
    
    root.left = removal(root.left)
    root.right = removal(root.right)
    if root.left is None and root.right is None:
        return root
    
    if root.left is None:
        new_root = root.right
        temp = root
        root = None
        del(temp)
        return new_root
    
    if root.right is None:
        new_root = root.left
        temp = root
        root = None
        del(temp)
        return new_root
    
    return root 

root = Node(2)
root.left = Node(7)
root.right = Node(5)
root.left.right = Node(6)
root.left.right.left = Node(1)
root.left.right.right = Node(11)
root.right.right = Node(9)
root.right.right.left = Node(4)

print ("Inorder traversal of given tree")
printInorder(root)
NewRoot = removal(root)
print ("\nInorder traversal of the modified tree")
printInorder(NewRoot)