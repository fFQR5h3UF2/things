# Submission title: Missing Number
# Submission url  : https://leetcode.com/problems/missing-number/description/"
# Submission url  : https://leetcode.com/submissions/detail/1181061860/"

import operator


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(
            operator.xor,
            nums,
            reduce(operator.xor, tuple(range(len(nums) + 1)), 0),
        )
