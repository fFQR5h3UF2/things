# Submission title: Painting the Walls
# Submission url  : https://leetcode.com/problems/painting-the-walls/description/
# Submission url  : https://leetcode.com/submissions/detail/1075145043/"


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        @cache
        def dp(i, remain):
            if remain <= 0:
                return 0
            if i == n:
                return inf

            paint = cost[i] + dp(i + 1, remain - 1 - time[i])
            dont_paint = dp(i + 1, remain)
            return min(paint, dont_paint)

        n = len(cost)
        return dp(0, n)
