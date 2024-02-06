# Submission title: for All Possible Full Binary Trees
# Submission url  : https://leetcode.com/submissions/detail/1001849755/
# Submission json : {"id": 1001849755, "status_display": "Accepted", "lang": "python3", "question_id": 930, "title_slug": "all-possible-full-binary-trees", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def allPossibleFBT(self, n: int) -> List[TreeNode]:\n        if n % 2 == 0:\n            return []\n        if n == 1:\n            return [TreeNode()]\n\n        res = []\n        for i in range(1, n, 2):\n            left = self.allPossibleFBT(i)\n            right = self.allPossibleFBT(n - i - 1)\n\n            for l in left:\n                for r in right:\n                    root = TreeNode(0, l, r)\n                    res.append(root)\n\n        return res", "title": "All Possible Full Binary Trees", "url": "/submissions/detail/1001849755/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690120234, "status": 10, "runtime": "213 ms", "is_pending": "Not Pending", "memory": "26 MB", "compare_result": "11111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[TreeNode]:
        if n % 2 == 0:
            return []
        if n == 1:
            return [TreeNode()]

        res = []
        for i in range(1, n, 2):
            left = self.allPossibleFBT(i)
            right = self.allPossibleFBT(n - i - 1)

            for l in left:
                for r in right:
                    root = TreeNode(0, l, r)
                    res.append(root)

        return res
