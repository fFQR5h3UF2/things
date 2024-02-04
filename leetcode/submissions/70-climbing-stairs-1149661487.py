# Submission for Climbing Stairs
# Submission url: https://leetcode.com/submissions/detail/1149661487/


class Solution:
    def climbStairs(self, n: int) -> int:
        prev, cur = 1, 2
        for i in range(2, n):
            new = prev + cur
            cur, prev = new, cur
        return cur
