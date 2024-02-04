# Submission for 'Missing Number'
# Submission url: https://leetcode.com/submissions/detail/1054578246/

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        return ((length + 1) * length) // 2 - sum(nums)
