# Submission for 'Sum of All Subset XOR Totals'
# Submission url: https://leetcode.com/submissions/detail/1056216664/

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsets_count = 2**(len(nums) - 1)
        return reduce(operator.or_, nums) * subsets_count
