# Submission title: Missing Number
# Submission url  : https://leetcode.com/problems/missing-number/description/"
# Submission url  : https://leetcode.com/submissions/detail/1180911196/"


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        def xor(total: int, i: int) -> int:
            return total ^ nums[i] ^ (i + 1)

        return reduce(xor, chain((0,), range(len(nums))))
