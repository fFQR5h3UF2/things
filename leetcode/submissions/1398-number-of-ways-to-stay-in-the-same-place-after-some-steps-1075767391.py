# Submission for 'Number of Ways to Stay in the Same Place After Some Steps'
# Submission url: https://leetcode.com/submissions/detail/1075767391/

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        @cache
        def dp(curr, remain):
            if remain == 0:
                if curr == 0:
                    return 1

                return 0

            ans = dp(curr, remain - 1)
            if curr > 0:
                ans = (ans + dp(curr - 1, remain - 1)) % MOD

            if curr < arrLen - 1:
                ans = (ans + dp(curr + 1, remain - 1)) % MOD

            return ans

        MOD = 10 ** 9 + 7
        return dp(0, steps)
