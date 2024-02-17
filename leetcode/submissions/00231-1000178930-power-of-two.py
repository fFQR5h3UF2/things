# Submission title: Power of Two
# Submission url  : https://leetcode.com/problems/power-of-two/description/"
# Submission url  : https://leetcode.com/submissions/detail/1000178930/"


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True

        while n > 2 and not n % 2:
            n //= 2
        return n == 2
