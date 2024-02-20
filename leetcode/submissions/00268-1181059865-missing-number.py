# Submission title: Missing Number
# Submission url  : https://leetcode.com/problems/missing-number/description/"
# Submission url  : https://leetcode.com/submissions/detail/1181059865/"

import operator


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.extend(range(len(nums) + 1))
        return reduce(operator.xor, nums, 0)
