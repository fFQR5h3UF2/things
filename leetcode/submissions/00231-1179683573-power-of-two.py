# Submission title: Power of Two
# Submission url  : https://leetcode.com/problems/power-of-two/description/"
# Submission url  : https://leetcode.com/submissions/detail/1179683573/"


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0
