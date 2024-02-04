# Submission for 'Factorial Trailing Zeroes'
# Submission url: https://leetcode.com/submissions/detail/1057802784/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        a, b, zeros = 1, 5, 0
        while (5**a) <= n:
            zeros += n // b
            a += 1
            b *= 5
        return zeros
