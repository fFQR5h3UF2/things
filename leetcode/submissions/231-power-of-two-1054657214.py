# Submission for Power of Two
# Submission url: https://leetcode.com/submissions/detail/1054657214/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n - 1) == 0
