# Submission title: for Maximum Depth of Binary Tree
# Submission url  : https://leetcode.com/submissions/detail/995847615/
# Submission json : {"id": 995847615, "status_display": "Accepted", "lang": "python3", "question_id": 104, "title_slug": "maximum-depth-of-binary-tree", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def maxDepth(self, root: Optional[TreeNode], count: int = 0) -> int:\n        if not root:\n            return 0\n        \n        if not root.left and not root.right:\n            return count + 1\n\n        return max(self.maxDepth(root.left, count + 1), self.maxDepth(root.right, count + 1))\n        ", "title": "Maximum Depth of Binary Tree", "url": "/submissions/detail/995847615/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689509076, "status": 10, "runtime": "58 ms", "is_pending": "Not Pending", "memory": "18.8 MB", "compare_result": "111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode], count: int = 0) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return count + 1

        return max(
            self.maxDepth(root.left, count + 1), self.maxDepth(root.right, count + 1)
        )
