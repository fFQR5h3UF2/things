# Submission title: Invert Binary Tree
# Submission url  : https://leetcode.com/problems/invert-binary-tree/description/
# Submission url  : https://leetcode.com/submissions/detail/1032230638/
# Submission json : {"id":1032230638,"status_display":"Accepted","lang":"python3","question_id":226,"title_slug":"invert-binary-tree","code":"# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:\n        if not root:\n            return None\n\n        self.invertTree(root.left)\n        self.invertTree(root.right) \n        root.left, root.right = root.right, root.left\n        \n        return root ","title":"Invert Binary Tree","url":"/submissions/detail/1032230638/","lang_name":"Python3","time":"5 months, 1 week","timestamp":1693052336,"status":10,"runtime":"44 ms","is_pending":"Not Pending","memory":"16.2 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        self.invertTree(root.left)
        self.invertTree(root.right)
        root.left, root.right = root.right, root.left

        return root
