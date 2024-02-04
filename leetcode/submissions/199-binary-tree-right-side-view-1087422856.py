# Submission for Binary Tree Right Side View
# Submission url: https://leetcode.com/submissions/detail/1087422856/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        while root:
            answer.append(root.val)
            root = root.right
        return answer
