# Submission title: Maximum Difference Between Node and Ancestor
# Submission url  : https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/description/
# Submission url  : https://leetcode.com/submissions/detail/1143178340/
# Submission json : {"id":1143178340,"status_display":"Accepted","lang":"python3","question_id":1092,"title_slug":"maximum-difference-between-node-and-ancestor","code":"# Definition for a binary tree node.\n# class TreeNode(object):\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution(object):\n    def maxAncestorDiff(self, root):\n        if not root:\n            return 0\n        self.diff = 0\n        self.helper(root, root.val, root.val)\n        return self.diff\n    \n    def helper(self, root, min_val, max_val):\n        if not root:\n            return\n        self.diff = max(self.diff, max(abs(min_val - root.val), abs(max_val - root.val)))\n        min_val = min(min_val, root.val)\n        max_val = max(max_val, root.val)\n        self.helper(root.left, min_val, max_val)\n        self.helper(root.right, min_val, max_val)\n        ","title":"Maximum Difference Between Node and Ancestor","url":"/submissions/detail/1143178340/","lang_name":"Python3","time":"3 weeks, 3 days","timestamp":1704964551,"status":10,"runtime":"43 ms","is_pending":"Not Pending","memory":"19 MB","compare_result":"1111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxAncestorDiff(self, root):
        if not root:
            return 0
        self.diff = 0
        self.helper(root, root.val, root.val)
        return self.diff

    def helper(self, root, min_val, max_val):
        if not root:
            return
        self.diff = max(
            self.diff, max(abs(min_val - root.val), abs(max_val - root.val))
        )
        min_val = min(min_val, root.val)
        max_val = max(max_val, root.val)
        self.helper(root.left, min_val, max_val)
        self.helper(root.right, min_val, max_val)
