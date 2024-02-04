# Submission for House Robber
# Submission url: https://leetcode.com/submissions/detail/1152838255/


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)

        def dp(i: int) -> int:
            if i >= length:
                return 0
            val = nums[i]
            return max(dp(i + 1), val + dp(i + 2))

        return dp(0)
