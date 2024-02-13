# Submission title: Arithmetic Slices II - Subsequence
# Submission url  : https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/
# Submission url  : https://leetcode.com/submissions/detail/1139388730/
# Submission json : {"id":1139388730,"status_display":"Accepted","lang":"python3","question_id":446,"title_slug":"arithmetic-slices-ii-subsequence","code":"class Solution:\n    def numberOfArithmeticSlices(self, nums: List[int]) -> int:\n        n = len(nums)\n        total_count = 0  \n        dp = [defaultdict(int) for _ in range(n)]\n\n        for i in range(1, n):\n            for j in range(i):\n                diff = nums[i] - nums[j]\n                dp[i][diff] += 1  \n                if diff in dp[j]:\n                    dp[i][diff] += dp[j][diff]\n                    total_count += dp[j][diff]\n\n        return total_count","title":"Arithmetic Slices II - Subsequence","url":"/submissions/detail/1139388730/","lang_name":"Python3","time":"4 weeks","timestamp":1704619384,"status":10,"runtime":"385 ms","is_pending":"Not Pending","memory":"55.6 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total_count += dp[j][diff]

        return total_count
