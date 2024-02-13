# Submission title: Minimum Absolute Difference in BST
# Submission url  : https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/
# Submission url  : https://leetcode.com/submissions/detail/1033280927/
# Submission json : {"id":1033280927,"status_display":"Accepted","lang":"python3","question_id":530,"title_slug":"minimum-absolute-difference-in-bst","code":"# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:\n        values = []\n        def fall(node: TreeNode) -> None:\n            if not node:\n                return\n            values.append(node.val)\n            if node.left:\n                fall(node.left)\n            if node.right:\n                fall(node.right)\n        \n        fall(root)\n        values.sort()\n        min_diff = abs(values[1] - values[0])\n        for i in range(1, len(values) - 1):\n            min_diff = min(min_diff, abs(values[i] - values[i+1]))\n        \n        return min_diff","title":"Minimum Absolute Difference in BST","url":"/submissions/detail/1033280927/","lang_name":"Python3","time":"5 months, 1 week","timestamp":1693148603,"status":10,"runtime":"65 ms","is_pending":"Not Pending","memory":"18.7 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []

        def fall(node: TreeNode) -> None:
            if not node:
                return
            values.append(node.val)
            if node.left:
                fall(node.left)
            if node.right:
                fall(node.right)

        fall(root)
        values.sort()
        min_diff = abs(values[1] - values[0])
        for i in range(1, len(values) - 1):
            min_diff = min(min_diff, abs(values[i] - values[i + 1]))

        return min_diff
