# Searching in BSt

def searching(root,key):
    if root is None or root.data == key:
        return root
    
    if root.data < key:
        return searching(root.right, key)
    else:
        return searching(root.left, key)
    