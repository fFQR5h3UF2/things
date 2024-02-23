# Submission title: Power of Four
# Submission url  : https://leetcode.com/problems/power-of-four/description/
# Submission url  : https://leetcode.com/submissions/detail/1054631891/"


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if the number is greater than zero and is a power of two
        if n > 0 and (n & (n - 1)) == 0:
            # Check if the number is of the form 4^x
            return n & 0x55555555 == n
        else:
            return False
