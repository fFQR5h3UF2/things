# Submission for Minimum Replacements to Sort the Array
# Submission url: https://leetcode.com/submissions/detail/1036078106/


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
                max_val = num
                continue

            mod = num % max_val
            operations_count += num // max_val - 1
            if mod:
                operations_count += 1
                max_val = (max_val + mod) // 2

        return operations_count
