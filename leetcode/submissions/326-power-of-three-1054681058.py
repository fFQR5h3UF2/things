# Submission for Power of Three
# Submission url: https://leetcode.com/submissions/detail/1054681058/


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        #                           3 ** 20
        return n not in (0, -1) and 3486784401 % n == 0
