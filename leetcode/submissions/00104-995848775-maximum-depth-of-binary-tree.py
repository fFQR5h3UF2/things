# Submission title: Maximum Depth of Binary Tree
# Submission url  : https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
# Submission url  : https://leetcode.com/submissions/detail/995848775/"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth: int = 0) -> int:
        if not root:
            return depth

        return max(
            self.maxDepth(root.left, depth + 1),
            self.maxDepth(root.right, depth + 1),
        )
