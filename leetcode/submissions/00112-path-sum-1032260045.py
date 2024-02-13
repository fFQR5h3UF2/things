# Submission title: Path Sum
# Submission url  : https://leetcode.com/problems/path-sum/description/
# Submission url  : https://leetcode.com/submissions/detail/1032260045/
# Submission json : {"id":1032260045,"status_display":"Accepted","lang":"python3","question_id":112,"title_slug":"path-sum","code":"# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:\n        node_stack = [(root, 0)]\n        while node_stack:\n            node, curr_sum = node_stack.pop()\n            if not node:\n                continue\n            \n            new_sum = curr_sum + node.val\n            if new_sum == targetSum and not node.left and not node.right:\n                return True\n            \n            node_stack.extend(((node.left, new_sum), (node.right, new_sum)))\n                \n        return False","title":"Path Sum","url":"/submissions/detail/1032260045/","lang_name":"Python3","time":"5 months, 1 week","timestamp":1693055164,"status":10,"runtime":"36 ms","is_pending":"Not Pending","memory":"17.6 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        node_stack = [(root, 0)]
        while node_stack:
            node, curr_sum = node_stack.pop()
            if not node:
                continue

            new_sum = curr_sum + node.val
            if new_sum == targetSum and not node.left and not node.right:
                return True

            node_stack.extend(((node.left, new_sum), (node.right, new_sum)))

        return False
