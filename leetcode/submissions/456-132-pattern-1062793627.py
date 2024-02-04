# Submission for 132 Pattern
# Submission url: https://leetcode.com/submissions/detail/1062793627/


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        for i in range(3, len(nums)):
            if nums[i] > nums[i - 1] > nums[i - 2]:
                return True
        return False
