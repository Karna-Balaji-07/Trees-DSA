# Balance a binary search tree

def inorder(root,arr):
    if root is None:
        return 
    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)
    
def soln(root):
    arr = []
    inorder(root,arr)
    
    def sol(arr, left, right):
        if left > right:
            return None
        mid = (left+right)//2
        root = Node(arr[mid])
        root.left = sol(arr, left, mid-1)
        root.right = sol(arr,mid+1, right)
        return root
    
    return sol(arr,0,len(arr)-1)
    