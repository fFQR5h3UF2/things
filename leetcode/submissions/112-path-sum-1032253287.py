# Submission for Path Sum
# Submission url: https://leetcode.com/submissions/detail/1032253287/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        node_stack = [(root, targetSum)]
        while node_stack:
            node, target = node_stack.pop()
            if not node:
                continue

            new_target = target - node.val
            if not node.left and node.right and target == 0:
                return True
            if new_target < 0:
                continue
            node_stack.extend(((node.left, new_target), (node.right, new_target)))

        return False
