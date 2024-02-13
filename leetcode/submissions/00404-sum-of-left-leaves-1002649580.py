# Submission title: Sum of Left Leaves
# Submission url  : https://leetcode.com/problems/sum-of-left-leaves/description/
# Submission url  : https://leetcode.com/submissions/detail/1002649580/
# Submission json : {"id":1002649580,"status_display":"Accepted","lang":"python3","question_id":404,"title_slug":"sum-of-left-leaves","code":"# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:\n        nodes = set([root])\n        result = 0\n\n        while nodes:\n            node = nodes.pop()\n            \n            if node.left and not node.left.left and not node.left.right:\n                result += node.left.val\n            elif node.left:\n                nodes.add(node.left)\n            \n            if node.right:\n                nodes.add(node.right)\n            \n        return result","title":"Sum of Left Leaves","url":"/submissions/detail/1002649580/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1690205533,"status":10,"runtime":"47 ms","is_pending":"Not Pending","memory":"16.6 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        nodes = set([root])
        result = 0

        while nodes:
            node = nodes.pop()

            if node.left and not node.left.left and not node.left.right:
                result += node.left.val
            elif node.left:
                nodes.add(node.left)

            if node.right:
                nodes.add(node.right)

        return result
