# Submission title: Longest Increasing Subsequence
# Submission url  : https://leetcode.com/problems/longest-increasing-subsequence/description/
# Submission url  : https://leetcode.com/submissions/detail/1137494224/
# Submission json : {"id":1137494224,"status_display":"Accepted","lang":"python3","question_id":300,"title_slug":"longest-increasing-subsequence","code":"class Solution:\n    def lengthOfLIS(self, nums: List[int]) -> int:\n        if not nums:\n            return 0\n\n        n = len(nums)\n        dp = [1] * n\n\n        for i in range(1, n):\n            for j in range(i):\n                if nums[i] > nums[j]:\n                    dp[i] = max(dp[i], dp[j] + 1)\n\n        return max(dp)\n\n","title":"Longest Increasing Subsequence","url":"/submissions/detail/1137494224/","lang_name":"Python3","time":"1 month","timestamp":1704448848,"status":10,"runtime":"1779 ms","is_pending":"Not Pending","memory":"17.8 MB","compare_result":"1111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        dp = [1] * n

        for i in range(1, n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)
