# Submission title: Sum of Values at Indices With K Set Bits
# Submission url  : https://leetcode.com/problems/sum-of-values-at-indices-with-k-set-bits/description/"
# Submission url  : https://leetcode.com/submissions/detail/1054836434/"


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        return sum(num for i, num in enumerate(nums) if i.bit_count() == k)
