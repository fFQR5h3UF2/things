# Submission for Path Sum
# Submission url: https://leetcode.com/submissions/detail/1032254546/


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
            if new_target < 0:
                continue
            if not node.left and not node.right and target == 0:
                return True
            if node.left:
                node_stack.append((node.left, new_target))
            if node.right:
                node_stack.append((node.right, new_target))

        return False
