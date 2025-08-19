''' 
Given the root of a binary tree, determine if it is a complete binary tree.

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
from collections import deque
def solution1(root):
    if root is None:
        return True
    q = deque([root])
    flag = False
    while q:
        current = q.popleft()
        if current.left:
            if flag:
                return False
            q.append(current.left)
        else:
            flag = True
        if current.right:
            if flag:
                return False
            q.append(current.right)
        else:
            flag = True
    return True

def solution2(root):
    if root is None:
        return True
    q = deque([root])
    null = False
    while q:
        current = q.popleft()
        if current is None:
            null = True
        else:
            if null:
                return False
            
            q.append(current.left)
            q.append(current.right)
    return True
