# Submission title: Single Number
# Submission url  : https://leetcode.com/problems/single-number/description/"
# Submission url  : https://leetcode.com/submissions/detail/1046649051/"


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda total, element: total ^ element, nums)
