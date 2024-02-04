# Submission for 132 Pattern
# Submission url: https://leetcode.com/submissions/detail/1062843573/


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        min_i = inf
        for j in range(len(nums) - 1):
            min_i = min(min_i, nums[j])
            for k in range(j + 1, len(nums)):
                if min_i < nums[k] < nums[j]:
                    return True
        return False
