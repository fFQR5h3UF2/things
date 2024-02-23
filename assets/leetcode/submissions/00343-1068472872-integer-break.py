# Submission title: Integer Break
# Submission url  : https://leetcode.com/problems/integer-break/description/
# Submission url  : https://leetcode.com/submissions/detail/1068472872/"


class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(num: int) -> int:
            if num <= 3:
                return num
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp(num - i))
            return ans

        return dp(n) if n > 3 else n - 1
