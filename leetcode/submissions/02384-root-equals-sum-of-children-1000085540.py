# Submission title: Root Equals Sum of Children
# Submission url  : https://leetcode.com/problems/root-equals-sum-of-children/description/
# Submission url  : https://leetcode.com/submissions/detail/1000085540/
# Submission json : {"id":1000085540,"status_display":"Accepted","lang":"python3","question_id":2384,"title_slug":"root-equals-sum-of-children","code":"# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def checkTree(self, root: Optional[TreeNode]) -> bool:\n        return root.val == (root.left.val + root.right.val)","title":"Root Equals Sum of Children","url":"/submissions/detail/1000085540/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1689934794,"status":10,"runtime":"45 ms","is_pending":"Not Pending","memory":"16.1 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val == (root.left.val + root.right.val)
