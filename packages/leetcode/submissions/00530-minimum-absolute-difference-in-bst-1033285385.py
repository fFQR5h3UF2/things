# Submission title: for Minimum Absolute Difference in BST
# Submission url  : https://leetcode.com/submissions/detail/1033285385/
# Submission json : {"id": 1033285385, "status_display": "Accepted", "lang": "python3", "question_id": 530, "title_slug": "minimum-absolute-difference-in-bst", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:\n        \n        def min_node_diff(node: TreeNode, low: int, high: int) -> int:\n            if not node:\n                return high - low\n\n            return min(min_node_diff(node.left, low, node.val),\n                       min_node_diff(node.right, node.val, high))\n    \n        return min_node_diff(root, -maxsize, maxsize)", "title": "Minimum Absolute Difference in BST", "url": "/submissions/detail/1033285385/", "lang_name": "Python3", "time": "5\u00a0months, 1\u00a0week", "timestamp": 1693148975, "status": 10, "runtime": "58 ms", "is_pending": "Not Pending", "memory": "18.6 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:

        def min_node_diff(node: TreeNode, low: int, high: int) -> int:
            if not node:
                return high - low

            return min(
                min_node_diff(node.left, low, node.val),
                min_node_diff(node.right, node.val, high),
            )

        return min_node_diff(root, -maxsize, maxsize)
