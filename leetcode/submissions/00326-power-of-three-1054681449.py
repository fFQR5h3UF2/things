# Submission for Power of Three
# Submission url: https://leetcode.com/submissions/detail/1054681449/


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #                3 ** 20
        return n > 0 and 3486784401 % n == 0
