# Convert BST to greater tree

def solution(root):
    total = 0
    def reversal(root):
        if root is None:
            return
        reversal(root.right)
        total += root.data
        root.data = total
        reversal(root.left)
    reversal(root)
    