# Submission title: for Balanced Binary Tree
# Submission url  : https://leetcode.com/submissions/detail/1047278821/
# Submission json : {"id": 1047278821, "status_display": "Accepted", "lang": "python3", "question_id": 110, "title_slug": "balanced-binary-tree", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def isBalanced(self, root: Optional[TreeNode]) -> bool:\n        def get_height(node: TreeNode) -> int:\n            if not node:\n                return 0\n            \n            h_left = get_height(node.left)\n            if h_left < 0:\n                return -1\n            h_right = get_height(node.right)\n            if h_right < 0 or abs(h_left - h_right) > 1:\n                return -1\n\n            return max(h_left, h_right) + 1\n        \n        return get_height(root) >= 0", "title": "Balanced Binary Tree", "url": "/submissions/detail/1047278821/", "lang_name": "Python3", "time": "4\u00a0months, 3\u00a0weeks", "timestamp": 1694506665, "status": 10, "runtime": "38 ms", "is_pending": "Not Pending", "memory": "21.2 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def get_height(node: TreeNode) -> int:
            if not node:
                return 0

            h_left = get_height(node.left)
            if h_left < 0:
                return -1
            h_right = get_height(node.right)
            if h_right < 0 or abs(h_left - h_right) > 1:
                return -1

            return max(h_left, h_right) + 1

        return get_height(root) >= 0
