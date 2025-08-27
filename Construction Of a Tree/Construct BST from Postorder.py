# Construct a binary search tree from postorder traversal

def solution(arr):
    def sol(arr,low,high):
        if low > high:
            return None
        
        root = Node(arr[high])
        if low == high:
            return root
        
        i = high-1
        while i >= low and arr[i] >= root.data:
            i -=1
        
        root.left = sol(arr,low,i+1)
        root.right = sol(arr,i,high)
        return root
    
    return sol(arr,0,len(arr))