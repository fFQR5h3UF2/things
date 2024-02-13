# Submission title: Minimum Operations to Reduce X to Zero
# Submission url  : https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
# Submission url  : https://leetcode.com/submissions/detail/1054343833/
# Submission json : {"id":1054343833,"status_display":"Accepted","lang":"python3","question_id":1776,"title_slug":"minimum-operations-to-reduce-x-to-zero","code":"class Solution:\n    def minOperations(self, nums: List[int], x: int) -> int:\n        target, length = sum(nums) - x, len(nums)\n        max_len = cur_sum = left = 0\n        \n        if target == 0:\n            return length\n        \n        for right, val in enumerate(nums):\n            cur_sum += val\n            while left <= right and cur_sum > target:\n                cur_sum -= nums[left]\n                left += 1\n            if cur_sum == target:\n                max_len = max(max_len, right - left + 1)\n        \n        return length - max_len if max_len else -1","title":"Minimum Operations to Reduce X to Zero","url":"/submissions/detail/1054343833/","lang_name":"Python3","time":"4 months, 2 weeks","timestamp":1695199644,"status":10,"runtime":"946 ms","is_pending":"Not Pending","memory":"30.2 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target, length = sum(nums) - x, len(nums)
        max_len = cur_sum = left = 0

        if target == 0:
            return length

        for right, val in enumerate(nums):
            cur_sum += val
            while left <= right and cur_sum > target:
                cur_sum -= nums[left]
                left += 1
            if cur_sum == target:
                max_len = max(max_len, right - left + 1)

        return length - max_len if max_len else -1
