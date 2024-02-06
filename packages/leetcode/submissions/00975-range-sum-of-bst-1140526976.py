# Submission title: for Range Sum of BST
# Submission url  : https://leetcode.com/submissions/detail/1140526976/
# Submission json : {"id": 1140526976, "status_display": "Accepted", "lang": "python3", "question_id": 975, "title_slug": "range-sum-of-bst", "code": "class Solution:\n    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:\n        def dfs(node):\n            if not node:\n                return 0\n            \n            current_val = 0\n            if low <= node.val <= high:\n                current_val = node.val\n            \n            left_sum = dfs(node.left)\n            right_sum = dfs(node.right)\n            \n            return current_val + left_sum + right_sum\n        \n        return dfs(root)", "title": "Range Sum of BST", "url": "/submissions/detail/1140526976/", "lang_name": "Python3", "time": "3\u00a0weeks, 6\u00a0days", "timestamp": 1704725060, "status": 10, "runtime": "143 ms", "is_pending": "Not Pending", "memory": "24.5 MB", "compare_result": "11111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return 0

            current_val = 0
            if low <= node.val <= high:
                current_val = node.val

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            return current_val + left_sum + right_sum

        return dfs(root)
