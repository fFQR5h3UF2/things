# Submission for Single Number
# Submission url: https://leetcode.com/submissions/detail/1046655572/


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(xor, nums)
