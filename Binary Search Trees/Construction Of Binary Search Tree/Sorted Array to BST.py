# Convert sorted array to binary search tree

def solution(arr):
    def sol(arr,start,end):
        if start  > end:
            return None
        
        mid = (start+end)//2
        root = Node(arr[mid])
        root.left = sol(arr,start,mid-1)
        root.right = sol(arr,mid+1,end)
    
        return root
    
    return sol(arr,0,len(arr)-1)
