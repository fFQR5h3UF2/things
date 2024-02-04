# Submission for Combination Sum IV
# Submission url: https://leetcode.com/submissions/detail/1044518246/


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        def backtrack(cur_sum) -> int:
            if cur_sum == target:
                return 1
            if cur_sum > target:
                return 0

            return sum(backtrack(cur_sum + num) for num in nums)

        return backtrack(0)
