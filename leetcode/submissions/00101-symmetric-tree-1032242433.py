# Submission title: Symmetric Tree
# Submission url  : https://leetcode.com/problems/symmetric-tree/description/
# Submission url  : https://leetcode.com/submissions/detail/1032242433/
# Submission json : {"id":1032242433,"status_display":"Accepted","lang":"python3","question_id":101,"title_slug":"symmetric-tree","code":"# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def isSymmetric(self, root: Optional[TreeNode]) -> bool:\n        comparison_stack = [(root.left, root.right)]\n        while comparison_stack:\n            left, right = comparison_stack.pop()\n            \n            if not left and not right:\n                continue\n            if not left or not right or left.val != right.val:\n                return False\n\n            comparison_stack.extend(((left.left, right.right), (left.right, right.left)))\n        \n        return True\n\n","title":"Symmetric Tree","url":"/submissions/detail/1032242433/","lang_name":"Python3","time":"5 months, 1 week","timestamp":1693053491,"status":10,"runtime":"43 ms","is_pending":"Not Pending","memory":"16.5 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        comparison_stack = [(root.left, root.right)]
        while comparison_stack:
            left, right = comparison_stack.pop()

            if not left and not right:
                continue
            if not left or not right or left.val != right.val:
                return False

            comparison_stack.extend(
                ((left.left, right.right), (left.right, right.left))
            )

        return True
