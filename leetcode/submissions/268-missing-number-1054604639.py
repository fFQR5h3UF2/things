# Submission for Missing Number
# Submission url: https://leetcode.com/submissions/detail/1054604639/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return reduce(
            lambda total, i: total ^ nums[i] ^ (i + 1), chain((0,), range(len(nums)))
        )
