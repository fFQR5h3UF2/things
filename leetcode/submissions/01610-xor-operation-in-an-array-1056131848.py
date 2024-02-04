# Submission for XOR Operation in an Array
# Submission url: https://leetcode.com/submissions/detail/1056131848/


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda total, i: total ^ (start + 2 * i), chain((0,), range(n)))
