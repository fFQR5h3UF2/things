# Submission for Minimum Replacements to Sort the Array
# Submission url: https://leetcode.com/submissions/detail/1036064128/


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        nums_count = len(nums)
        if nums_count == 1:
            return 0

        max_val = nums[-1]
        operations_count = 0
        for i in reversed(range(nums_count - 1)):
            num = nums[i]
            if num <= max_val:
                continue
            max_val = num // 2
            operations_count += 1

        return operations_count
