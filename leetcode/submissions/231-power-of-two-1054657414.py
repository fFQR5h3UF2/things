# Submission for Power of Two
# Submission url: https://leetcode.com/submissions/detail/1054657414/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n == 0 or n & (n - 1) == 0
