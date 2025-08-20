# Binary tree maximum paths sum

def solution(root):
    maxsum = float('-inf')
     
    def dfs(root):
        nonlocal maxsum
        if not root:
            return 0
        
        left_sum = max(dfs(root.left),0)
        right_sum = max(dfs(root.right),0)
        prices = root.data + left_sum + right_sum
        maxsum = max(maxsum,prices)
        return root.data + max(left_sum,right_sum)
    