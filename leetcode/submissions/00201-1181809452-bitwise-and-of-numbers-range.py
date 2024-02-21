# Submission title: Bitwise AND of Numbers Range
# Submission url  : https://leetcode.com/problems/bitwise-and-of-numbers-range/description/
# Submission url  : https://leetcode.com/submissions/detail/1181809452/"


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        shift = 0
        while left != right:
            left >>= 1
            right >>= 1
            shift += 1
        return left << shift
