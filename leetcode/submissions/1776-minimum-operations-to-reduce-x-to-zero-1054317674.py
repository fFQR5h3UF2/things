# Submission for Minimum Operations to Reduce X to Zero
# Submission url: https://leetcode.com/submissions/detail/1054317674/


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        @cache
        def dp(left: int, right: int, x: int) -> int:
            if x < 0:
                return -1
            if x == 0:
                return 0
            if left == right:
                return 0 if nums[left] == x else -1

            results = (
                1 + dp(left + 1, right, x - nums[left]),
                1 + dp(left, right - 1, x - nums[right]),
            )
            return min((result for result in results if result > 0), default=-1)

        return dp(0, len(nums) - 1, x)
