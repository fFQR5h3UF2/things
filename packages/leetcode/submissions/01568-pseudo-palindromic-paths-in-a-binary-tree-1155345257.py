# Submission title: for Pseudo-Palindromic Paths in a Binary Tree
# Submission url  : https://leetcode.com/submissions/detail/1155345257/
# Submission json : {"id": 1155345257, "status_display": "Accepted", "lang": "python3", "question_id": 1568, "title_slug": "pseudo-palindromic-paths-in-a-binary-tree", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:\n        if not root:\n            return 0\n        \n        num_count = defaultdict(int)\n        perm_count = 0\n\n        def traverse(node: TreeNode) -> int:\n            val, left, right = node.val, node.left, node.right\n            num_count[val] += 1\n            res = 0\n            if not left and not right:\n                non_even = 0\n                for num in num_count.values():\n                    if num % 2 == 0:\n                        continue\n                    if non_even == 1:\n                        break\n                    non_even += 1\n                else:\n                    res += 1\n            if left:\n                res += traverse(left)\n            if right: \n                res += traverse(right)\n            num_count[val] = max(0, num_count[val] - 1)\n            return res \n\n        return traverse(root)", "title": "Pseudo-Palindromic Paths in a Binary Tree", "url": "/submissions/detail/1155345257/", "lang_name": "Python3", "time": "1\u00a0week, 4\u00a0days", "timestamp": 1706081967, "status": 10, "runtime": "415 ms", "is_pending": "Not Pending", "memory": "43.9 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


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
            val, left, right = node.val, node.left, node.right
            num_count[val] += 1
            res = 0
            if not left and not right:
                non_even = 0
                for num in num_count.values():
                    if num % 2 == 0:
                        continue
                    if non_even == 1:
                        break
                    non_even += 1
                else:
                    res += 1
            if left:
                res += traverse(left)
            if right:
                res += traverse(right)
            num_count[val] = max(0, num_count[val] - 1)
            return res

        return traverse(root)
