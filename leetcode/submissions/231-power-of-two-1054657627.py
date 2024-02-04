# Submission for Power of Two
# Submission url: https://leetcode.com/submissions/detail/1054657627/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
