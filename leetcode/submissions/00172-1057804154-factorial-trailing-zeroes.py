# Submission title: Factorial Trailing Zeroes
# Submission url  : https://leetcode.com/problems/factorial-trailing-zeroes/description/
# Submission url  : https://leetcode.com/submissions/detail/1057804154/"


class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        while n != 0:
            new_n = n // 5
            zeros += new_n
            n = new_n
        return zeros
