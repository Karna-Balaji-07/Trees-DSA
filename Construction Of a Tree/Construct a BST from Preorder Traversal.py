# Construct a BST from Preorder traversal

def solution(arr):
    def sol(arr,low,high):
        if low > high:
            return None
        
        root  = Node(arr[low])
        if low == high:
            return root
        
        i = low +1
        while i <= high and arr[i] <= root.data:
            i +=1
        
        root.left = sol(arr,low+1, i-1)
        root.right = sol(arr,i,high)
        
    return sol(arr,0,len(arr)-1)