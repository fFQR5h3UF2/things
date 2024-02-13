# Submission title: Symmetric Tree
# Submission url  : https://leetcode.com/problems/symmetric-tree/description/
# Submission url  : https://leetcode.com/submissions/detail/1032234143/
# Submission json : {"id":1032234143,"status_display":"Accepted","lang":"python3","question_id":101,"title_slug":"symmetric-tree","code":"# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def isSymmetric(self, root: Optional[TreeNode]) -> bool:\n        return self.check(root.left, root.right)\n\n    def check(self, left: TreeNode, right: TreeNode) -> bool:\n        if not left and not right:\n            return True\n        \n        if not left or not right or left.val != right.val:\n            return False\n        \n        return self.check(left.left, right.right) and self.check(left.right, right.left)\n","title":"Symmetric Tree","url":"/submissions/detail/1032234143/","lang_name":"Python3","time":"5 months, 1 week","timestamp":1693052671,"status":10,"runtime":"44 ms","is_pending":"Not Pending","memory":"16.5 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.check(root.left, root.right)

    def check(self, left: TreeNode, right: TreeNode) -> bool:
        if not left and not right:
            return True

        if not left or not right or left.val != right.val:
            return False

        return self.check(left.left, right.right) and self.check(left.right, right.left)
