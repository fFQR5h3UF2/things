# Submission title: Single Number
# Submission url  : https://leetcode.com/problems/single-number/description/
# Submission url  : https://leetcode.com/submissions/detail/1057806889/"


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
