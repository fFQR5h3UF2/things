# Submission title: Minimum Depth of Binary Tree
# Submission url  : https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
# Submission url  : https://leetcode.com/submissions/detail/1046639098/"


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            return 1 + min(
                (
                    depth
                    for depth in (dfs(node.left), dfs(node.right))
                    if depth > 0
                ),
                default=0,
            )

        return dfs(root)
