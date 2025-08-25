# Convert sorted linked list to binary search tree

def solution(head):
    def middle(start,end):
        slow = start
        fast = start
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow 
    
    def soln(left,right):
        if left == right:
            return None
        mid = middle(left,right)
        root = Node(mid.val)
        root.left = soln(left,mid)
        root.right = soln(mid.next,right)
        
        
        return root
    
    return soln(head,None)
    