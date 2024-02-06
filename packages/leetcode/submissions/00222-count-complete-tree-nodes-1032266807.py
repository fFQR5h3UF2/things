# Submission title: for Count Complete Tree Nodes
# Submission url  : https://leetcode.com/submissions/detail/1032266807/
# Submission json : {"id": 1032266807, "status_display": "Accepted", "lang": "python3", "question_id": 222, "title_slug": "count-complete-tree-nodes", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def countNodes(self, root: Optional[TreeNode]) -> int:\n        if not root:\n            return 0\n        \n        def left_height(root: TreeNode) -> int:\n            return 0 if not root else 1 + left_height(root.left)\n        \n        def right_height(root: TreeNode) -> int:\n            return 0 if not root else 1+ right_height(root.right)\n        \n        left, right = left_height(root), right_height(root)\n        if left > right:\n            return 1 + self.countNodes(root.left) + self.countNodes(root.right)\n        \n        return 2**left - 1\n\n        ", "title": "Count Complete Tree Nodes", "url": "/submissions/detail/1032266807/", "lang_name": "Python3", "time": "5\u00a0months, 1\u00a0week", "timestamp": 1693055806, "status": 10, "runtime": "67 ms", "is_pending": "Not Pending", "memory": "23.7 MB", "compare_result": "111111111111111111", "has_notes": true, "flag_type": 1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def left_height(root: TreeNode) -> int:
            return 0 if not root else 1 + left_height(root.left)

        def right_height(root: TreeNode) -> int:
            return 0 if not root else 1 + right_height(root.right)

        left, right = left_height(root), right_height(root)
        if left > right:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        return 2**left - 1
