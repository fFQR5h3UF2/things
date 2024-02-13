# Submission title: Running Sum of 1d Array
# Submission url  : https://leetcode.com/problems/running-sum-of-1d-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1000087386/
# Submission json : {"id":1000087386,"status_display":"Accepted","lang":"python3","question_id":1603,"title_slug":"running-sum-of-1d-array","code":"class Solution:\r\n    def runningSum(self, nums: List[int]) -> List[int]:\r\n        for i in range(1, len(nums)):\r\n            nums[i] += nums[i-1]\r\n        return nums","title":"Running Sum of 1d Array","url":"/submissions/detail/1000087386/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1689934985,"status":10,"runtime":"48 ms","is_pending":"Not Pending","memory":"16.7 MB","compare_result":"11111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
