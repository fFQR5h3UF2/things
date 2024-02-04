# Submission for 'Binary Number with Alternating Bits'
# Submission url: https://leetcode.com/submissions/detail/1054695718/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return n & (n >> 1) == 0 and n & (n >> 2) == n >> 2
