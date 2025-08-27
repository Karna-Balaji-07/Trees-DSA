# Kth smallest element in BST

def solution(root,k):
    arr = []
    def inorder(root,arr):
        if root is None:
            return 
        inorder(root.left, arr)
        arr.append(root.val)
        inorder(root.right, arr)
    inorder(root,arr)
    return arr[k-1]