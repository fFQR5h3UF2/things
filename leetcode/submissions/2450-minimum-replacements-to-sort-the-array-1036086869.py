# Submission for Minimum Replacements to Sort the Array
# Submission url: https://leetcode.com/submissions/detail/1036086869/


class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        nums_count = len(nums)
        operations_count = 0
        max_val = nums[-1]
        for i in reversed(range(nums_count - 1)):
            num = nums[i]
            if num < max_val:
                max_val = num
            if num <= max_val:
                continue

            mod = num % max_val
            operations_count += num // max_val - 1
            if mod:
                operations_count += 1
                max_val -= 1

        return operations_count
