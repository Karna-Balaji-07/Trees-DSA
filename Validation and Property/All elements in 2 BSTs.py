# All elements in 2 BInary search Trees

def solution(root1, root2):
    arr1 = []
    arr2 =[]
    def inorder(root,arr):
        if not root:
            return
        inorder(root.left, arr)
        arr.append(root.val)
        inorder(root.right,arr)
    
    inorder(root1, arr1)
    inorder(root2,arr2)
    
    i = 0, j = 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] >= arr2[j]:
            merged.append(arr2[j])
            j +=1
        else:
            merged.append(arr1[i])
            i +=1
        
    merged.extend(arr1[i:])
    merged.extend(arr2[j:])
    return merged