# Submission title: Number of 1 Bits
# Submission url  : https://leetcode.com/problems/number-of-1-bits/description/"
# Submission url  : https://leetcode.com/submissions/detail/1057806680/"


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1 != 0:
                count += 1
            n >>= 1
        return count
