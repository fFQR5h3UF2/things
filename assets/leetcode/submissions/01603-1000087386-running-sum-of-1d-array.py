# Submission title: Running Sum of 1d Array
# Submission url  : https://leetcode.com/problems/running-sum-of-1d-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1000087386/"


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums
