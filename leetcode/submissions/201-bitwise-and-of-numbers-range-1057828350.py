# Submission for Bitwise AND of Numbers Range
# Submission url: https://leetcode.com/submissions/detail/1057828350/


class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        return reduce(operator.and_, range(left, right + 1))
