# Submission for House Robber
# Submission url: https://leetcode.com/submissions/detail/1152839694/


class Solution:
    def rob(self, nums: List[int]) -> int:
        length = len(nums)
        cache = {}

        def dp(i: int) -> int:
            if i >= length:
                return 0
            val = nums[i]
            if val in cache:
                return cache[val]
            res = max(dp(i + 1), val + dp(i + 2))
            cache[val] = res
            return res

        return dp(0)
