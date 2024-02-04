# Submission for Convert Sorted Array to Binary Search Tree
# Submission url: https://leetcode.com/submissions/detail/1040142750/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        nums_count = len(nums)
        mid = nums_count // 2
        root = TreeNode(nums[mid])
        left_tail, right_tail = root, root
        for i in reversed(range(mid)):
            left_tail.left = TreeNode(nums[i])
            left_tail = left_tail.left

        for i in range(mid + 1, nums_count):
            right_tail.right = TreeNode(nums[i])
            right_tail = right_tail.right

        return root
