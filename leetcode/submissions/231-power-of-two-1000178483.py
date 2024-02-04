# Submission for Power of Two
# Submission url: https://leetcode.com/submissions/detail/1000178483/


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        while n > 2:
            n //= 2
        return n == 2
