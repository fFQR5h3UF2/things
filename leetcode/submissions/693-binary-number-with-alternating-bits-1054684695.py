# Submission for Binary Number with Alternating Bits
# Submission url: https://leetcode.com/submissions/detail/1054684695/


class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        return n & 0x55555555 == n or n & 0xAAAAAAAA == n
