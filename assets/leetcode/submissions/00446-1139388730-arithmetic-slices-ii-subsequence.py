# Submission title: Arithmetic Slices II - Subsequence
# Submission url  : https://leetcode.com/problems/arithmetic-slices-ii-subsequence/description/
# Submission url  : https://leetcode.com/submissions/detail/1139388730/"


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
