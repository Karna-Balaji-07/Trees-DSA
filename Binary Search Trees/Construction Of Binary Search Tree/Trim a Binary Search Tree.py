# Trim a binary search tree

def solution(root, start, end):
    if not root:
        return None
    
    if root.data < start:
        return solution(root.right, start, end)
    if root.data >  end:
        return solution(root.left, start, end)
    
    root.left = solution(root.left, start, end)
    root.right = solution(root.right, start, end)

    return root