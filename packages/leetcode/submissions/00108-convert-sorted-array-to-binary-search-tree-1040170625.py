# Submission title: for Convert Sorted Array to Binary Search Tree
# Submission url  : https://leetcode.com/submissions/detail/1040170625/
# Submission json : {"id": 1040170625, "status_display": "Accepted", "lang": "python3", "question_id": 108, "title_slug": "convert-sorted-array-to-binary-search-tree", "code": "# Definition for a binary tree node.\n# class TreeNode:\n#     def __init__(self, val=0, left=None, right=None):\n#         self.val = val\n#         self.left = left\n#         self.right = right\nclass Solution:\n    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:\n        nums_count = len(nums)\n        if nums_count == 0:\n            return None\n        \n        mid = nums_count // 2\n        return TreeNode(nums[mid], \n                        self.sortedArrayToBST(nums[:mid]), \n                        self.sortedArrayToBST(nums[mid+1:]))", "title": "Convert Sorted Array to Binary Search Tree", "url": "/submissions/detail/1040170625/", "lang_name": "Python3", "time": "5\u00a0months", "timestamp": 1693820641, "status": 10, "runtime": "55 ms", "is_pending": "Not Pending", "memory": "17.9 MB", "compare_result": "1111111111111111111111111111111", "has_notes": false, "flag_type": 1}


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        nums_count = len(nums)
        if nums_count == 0:
            return None

        mid = nums_count // 2
        return TreeNode(
            nums[mid],
            self.sortedArrayToBST(nums[:mid]),
            self.sortedArrayToBST(nums[mid + 1 :]),
        )
