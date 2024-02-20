# Submission title: House Robber
# Submission url  : https://leetcode.com/problems/house-robber/description/
# Submission url  : https://leetcode.com/submissions/detail/1014573838/"


class Solution:
    def rob(self, nums: List[int]) -> int:
        house_count = len(nums)

        dp = [0 for _ in range(house_count + 1)]
        dp[1] = nums[0]

        for house in range(1, house_count):
            dp[house + 1] = max(dp[house - 1] + nums[house], dp[house])

        return dp[-1]
