# Submission for Combination Sum IV
# Submission url: https://leetcode.com/submissions/detail/1044517658/


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        stack = []

        def backtrack(cur_sum) -> int:
            if cur_sum == target:
                return 1
            if cur_sum > target:
                return 0

            comb_count = 0

            for num in nums:
                stack.append(num)
                comb_count += backtrack(cur_sum + num)
                stack.pop()

            return comb_count

        return backtrack(0)
