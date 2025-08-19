# Convert the given linked list to binary tree

class LinkedList:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        
from collections import deque

def construct(head):
    if not head:
        return None
    
    q = deque()
    root = LinkedList(head.data)
    q.append(root)
    head = head.next
    
    while head:
        parent = q.popleft()
        leftchild = None
        rightchild = None
        
        if head:
            leftchild = Node(head.data)
            q.append(leftchild)
            head = head.next
        
        if head:
            rightchild = Node(head.data)
            q.append(rightchild)
            head = head.next
        
        parent.left = leftchild
        parent.right = rightchild
        
    return root
    