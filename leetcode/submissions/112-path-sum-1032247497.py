# Submission for Path Sum
# Submission url: https://leetcode.com/submissions/detail/1032247497/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def check(node: TreeNode, target: int) -> bool:
            if not node:
                return target == 0

            new_target = target - node.val
            if new_target < 0:
                return False

            return check(node.left, new_target) or check(node.right, new_target)

        return check(root, targetSum)
