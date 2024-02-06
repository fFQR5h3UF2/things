# Submission title: for Pseudo-Palindromic Paths in a Binary Tree
# Submission url  : https://leetcode.com/submissions/detail/1155337065/
# Submission json : {"id": 1155337065, "status_display": "Accepted", "lang": "python3", "question_id": 1568, "title_slug": "pseudo-palindromic-paths-in-a-binary-tree", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:\n        if not root:\n            return 0\n        \n        num_count = defaultdict(int)\n        perm_count = 0\n\n        def traverse(node: TreeNode) -> int:\n            if not node:\n                return 0\n            val, left, right = node.val, node.left, node.right\n            num_count[val] += 1\n            res = 0\n            if not left and not right:\n                non_even = 0\n                for num in num_count.values():\n                    if num % 2 == 0:\n                        continue\n                    non_even += 1\n                    if non_even > 1:\n                        break\n                else:\n                    res += 1\n            res += traverse(left) + traverse(right)\n            num_count[val] = max(0, num_count[val] - 1)\n            return res \n\n        return traverse(root)", "title": "Pseudo-Palindromic Paths in a Binary Tree", "url": "/submissions/detail/1155337065/", "lang_name": "Python3", "time": "1\u00a0week, 4\u00a0days", "timestamp": 1706081228, "status": 10, "runtime": "443 ms", "is_pending": "Not Pending", "memory": "44.5 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        num_count = defaultdict(int)
        perm_count = 0

        def traverse(node: TreeNode) -> int:
            if not node:
                return 0
            val, left, right = node.val, node.left, node.right
            num_count[val] += 1
            res = 0
            if not left and not right:
                non_even = 0
                for num in num_count.values():
                    if num % 2 == 0:
                        continue
                    non_even += 1
                    if non_even > 1:
                        break
                else:
                    res += 1
            res += traverse(left) + traverse(right)
            num_count[val] = max(0, num_count[val] - 1)
            return res

        return traverse(root)
