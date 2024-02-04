# Submission for Product of Array Except Self
# Submission url: https://leetcode.com/submissions/detail/1018268771/


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        nums_count = len(nums)
        result = [1] * nums_count

        for i in range(nums_count):
            for j in range(nums_count):
                if j == i:
                    continue
                result[i] *= nums[j]

        return result
