# Submission title: Maximum Product Difference Between Two Pairs
# Submission url  : https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/
# Submission url  : https://leetcode.com/submissions/detail/1122499093/"


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return nums[-1] * nums[-2] - nums[0] * nums[1]
