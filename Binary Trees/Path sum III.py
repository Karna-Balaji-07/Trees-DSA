class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        from collections import defaultdict
        def dfs(node, curr_sum, prefix):
            if not node:
                return 0
            curr_sum += node.val
            count = prefix[curr_sum - targetSum]
            prefix[curr_sum] += 1
            count += dfs(node.left, curr_sum, prefix)
            count += dfs(node.right, curr_sum, prefix)
            prefix[curr_sum] -= 1  # Backtrack
            return count

        prefix = defaultdict(int)
        prefix[0] = 1
        return dfs(root, 0, prefix)