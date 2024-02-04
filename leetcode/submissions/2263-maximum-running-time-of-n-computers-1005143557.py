# Submission for Maximum Running Time of N Computers
# Submission url: https://leetcode.com/submissions/detail/1005143557/


class Solution:
    # n = 2, batteries = [3,3,3], Output: 4
    # [3,2,2], [2,1,2], [1,1,1], [0,1,0]
    # n = 2, batteries = [1,1,1,1], Output: 2
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        length = len(batteries)
        if length < n:
            return 0

        if length == n:
            return min(batteries)

        batteries = sorted(batteries)
        minutes = 0
        while n:
            for i in range(length - 1, length - n - 1, -1):
                if batteries[i] == 0:
                    return minutes
                batteries[i] -= 1
            batteries.sort()
            minutes += 1

        return minutes
