# Submission title: Merge Sorted Array
# Submission url  : https://leetcode.com/problems/merge-sorted-array/description/
# Submission url  : https://leetcode.com/submissions/detail/992867297/
# Submission json : {"id":992867297,"status_display":"Accepted","lang":"python3","question_id":88,"title_slug":"merge-sorted-array","code":"class Solution:\n    # have three indexes: nums1 (end of array 1), nums2 (from the end), \n    # and current (nums1 from the end) \n    # if nums2 number is bigger or equal than nums1 number, put the number at the current index,\n    # move both indexes\n    # if nums1 number is smaller than nums2 number, put the number at the current index, \n    # move both indexes  \n    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:\n        \"\"\"\n        Do not return anything, modify nums1 in-place instead.\n        \"\"\"\n\n        nums1_i, nums2_i = m - 1, n - 1\n        for i in range(m + n - 1, -1, -1):\n            nums1_number  = nums1[nums1_i] if nums1_i >= 0 else nums2[0] - 1\n            nums2_number = nums2[nums2_i] if nums2_i >= 0 else nums1[0] - 1\n            if nums1_number >= nums2_number:\n                nums1[i] = nums1_number\n                nums1_i -= 1\n                continue\n            \n            nums1[i] = nums2_number\n            nums2_i -= 1","title":"Merge Sorted Array","url":"/submissions/detail/992867297/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689183240,"status":10,"runtime":"42 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    # have three indexes: nums1 (end of array 1), nums2 (from the end),
    # and current (nums1 from the end)
    # if nums2 number is bigger or equal than nums1 number, put the number at the current index,
    # move both indexes
    # if nums1 number is smaller than nums2 number, put the number at the current index,
    # move both indexes
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        nums1_i, nums2_i = m - 1, n - 1
        for i in range(m + n - 1, -1, -1):
            nums1_number = nums1[nums1_i] if nums1_i >= 0 else nums2[0] - 1
            nums2_number = nums2[nums2_i] if nums2_i >= 0 else nums1[0] - 1
            if nums1_number >= nums2_number:
                nums1[i] = nums1_number
                nums1_i -= 1
                continue

            nums1[i] = nums2_number
            nums2_i -= 1
