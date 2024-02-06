# Submission title: for Minimum Depth of Binary Tree
# Submission url  : https://leetcode.com/submissions/detail/1046639098/
# Submission json : {"id": 1046639098, "status_display": "Accepted", "lang": "python3", "question_id": 111, "title_slug": "minimum-depth-of-binary-tree", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def minDepth(self, root: Optional[TreeNode]) -> int:\n        \n        def dfs(node: TreeNode) -> int:\n            if not node:\n                return 0\n\n            return 1 + min((depth for depth in (dfs(node.left), dfs(node.right)) if depth > 0),\n                           default=0)\n\n        return dfs(root)", "title": "Minimum Depth of Binary Tree", "url": "/submissions/detail/1046639098/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694447170, "status": 10, "runtime": "595 ms", "is_pending": "Not Pending", "memory": "58.1 MB", "compare_result": "11111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        def dfs(node: TreeNode) -> int:
            if not node:
                return 0

            return 1 + min(
                (depth for depth in (dfs(node.left), dfs(node.right)) if depth > 0),
                default=0,
            )

        return dfs(root)
