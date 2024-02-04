# Submission for Maximum Running Time of N Computers
# Submission url: https://leetcode.com/submissions/detail/1005155392/


class Solution:
    # n = 2, batteries = [3,4,5], Output: 4
    # [2,3,5], [2,2,4], [1,2,3], [0,1,3], [0,0,2]
    # [3,3,4], [3,2,3], [2,2,2], [2,1,1], [2,0,0]
    # n = 2, batteries = [1,1,1,1], Output: 2
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        minutes, current = 0, 0
        batteries = sorted(batteries)
        while len(batteries) > n:
            count = 0
            while count < n:
                if current >= len(batteries):
                    current = 0

                batteries[current] -= 1
                count += 1
                if not batteries[current]:
                    batteries[current] = batteries[-1]
                    batteries.pop()
                current += 1

            minutes += 1

        if len(batteries) < n:
            return minutes

        return minutes + min(batteries)
