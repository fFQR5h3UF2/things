# Submission title: Range Sum of BST
# Submission url  : https://leetcode.com/problems/range-sum-of-bst/description/"
# Submission url  : https://leetcode.com/submissions/detail/1140526976/"


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0

            current_val = 0
            if low <= node.val <= high:
                current_val = node.val

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            return current_val + left_sum + right_sum

        return dfs(root)
