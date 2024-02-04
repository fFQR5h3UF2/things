# Submission title: for Invert Binary Tree
# Submission url  : https://leetcode.com/submissions/detail/1032231368/
# Submission json : {"id": 1032231368, "status_display": "Accepted", "lang": "python3", "question_id": 226, "title_slug": "invert-binary-tree", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:\n        if root:\n            root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)\n        return root ", "title": "Invert Binary Tree", "url": "/submissions/detail/1032231368/", "lang_name": "Python3", "time": "5\u00a0months, 1\u00a0week", "timestamp": 1693052407, "status": 10, "runtime": "41 ms", "is_pending": "Not Pending", "memory": "16.1 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            root.left, root.right = self.invertTree(root.right), self.invertTree(
                root.left
            )
        return root
