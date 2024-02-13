# Submission title: Longest Increasing Subsequence
# Submission url  : https://leetcode.com/problems/longest-increasing-subsequence/description/
# Submission url  : https://leetcode.com/submissions/detail/1014752319/
# Submission json : {"id":1014752319,"status_display":"Accepted","lang":"python3","question_id":300,"title_slug":"longest-increasing-subsequence","code":"class Solution:\n    def lengthOfLIS(self, nums: List[int]) -> int:\n        nums_count = len(nums)\n        dp = [0] * nums_count\n        dp[0] = 1\n        for i in range(1, nums_count):\n            length = 0\n            start = nums[i]\n\n            for j in range(0, i):\n                if start > nums[j]:\n                    length = max(length, dp[j])\n\n            dp[i] = 1 + length\n            \n        return max(dp)","title":"Longest Increasing Subsequence","url":"/submissions/detail/1014752319/","lang_name":"Python3","time":"6 months","timestamp":1691418246,"status":10,"runtime":"1885 ms","is_pending":"Not Pending","memory":"16.6 MB","compare_result":"111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums_count = len(nums)
        dp = [0] * nums_count
        dp[0] = 1
        for i in range(1, nums_count):
            length = 0
            start = nums[i]

            for j in range(0, i):
                if start > nums[j]:
                    length = max(length, dp[j])

            dp[i] = 1 + length

        return max(dp)
