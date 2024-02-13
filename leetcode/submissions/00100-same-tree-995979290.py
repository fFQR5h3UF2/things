# Submission title: Same Tree
# Submission url  : https://leetcode.com/problems/same-tree/description/
# Submission url  : https://leetcode.com/submissions/detail/995979290/
# Submission json : {"id":995979290,"status_display":"Accepted","lang":"python3","question_id":100,"title_slug":"same-tree","code":"# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:\n        if p and not q or (q and not p):\n            return False\n        \n        if not p and not q:\n            return True\n        \n        if p.val != q.val:\n            return False\n        \n        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)","title":"Same Tree","url":"/submissions/detail/995979290/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689521746,"status":10,"runtime":"49 ms","is_pending":"Not Pending","memory":"16.4 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p and not q or (q and not p):
            return False

        if not p and not q:
            return True

        if p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
