# Submission for Sum of All Subset XOR Totals
# Submission url: https://leetcode.com/submissions/detail/1056218717/


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        return reduce(operator.or_, nums) * 1 << (len(nums) - 1)
