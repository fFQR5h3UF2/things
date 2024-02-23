# Submission title: Power of Four
# Submission url  : https://leetcode.com/problems/power-of-four/description/
# Submission url  : https://leetcode.com/submissions/detail/1054628639/"


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n and not (n & (n - 1)) and (n & 0x55555555)
