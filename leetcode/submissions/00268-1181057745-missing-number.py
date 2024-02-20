# Submission title: Missing Number
# Submission url  : https://leetcode.com/problems/missing-number/description/
# Submission url  : https://leetcode.com/submissions/detail/1181057745/"

import operator


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        length = len(nums)
        return reduce(
            operator.xor, range(length), reduce(operator.xor, nums, length)
        )
