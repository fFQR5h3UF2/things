# Submission for House Robber
# Submission url: https://leetcode.com/submissions/detail/1014573008/


class Solution:
    def rob(self, nums: List[int]) -> int:
        house_count = len(nums)

        dp = [0 for _ in range(house_count + 1)]
        dp[1] = nums[0]

        for house in range(2, house_count + 1):
            dp[house] = max(dp[house - 2] + nums[house], dp[house - 1])

        return dp[-1]
