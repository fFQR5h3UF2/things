# Submission title: for Number of Ways to Stay in the Same Place After Some Steps
# Submission url  : https://leetcode.com/submissions/detail/1075767391/
# Submission json : {"id": 1075767391, "status_display": "Accepted", "lang": "python3", "question_id": 1398, "title_slug": "number-of-ways-to-stay-in-the-same-place-after-some-steps", "code": "class Solution:\n    def numWays(self, steps: int, arrLen: int) -> int:\n        @cache\n        def dp(curr, remain):\n            if remain == 0:\n                if curr == 0:\n                    return 1\n                \n                return 0\n            \n            ans = dp(curr, remain - 1)\n            if curr > 0:\n                ans = (ans + dp(curr - 1, remain - 1)) % MOD\n            \n            if curr < arrLen - 1:\n                ans = (ans + dp(curr + 1, remain - 1)) % MOD\n                \n            return ans\n        \n        MOD = 10 ** 9 + 7\n        return dp(0, steps)", "title": "Number of Ways to Stay in the Same Place After Some Steps", "url": "/submissions/detail/1075767391/", "lang_name": "Python3", "time": "3\u00a0months, 3\u00a0weeks", "timestamp": 1697364328, "status": 10, "runtime": "396 ms", "is_pending": "Not Pending", "memory": "108.6 MB", "compare_result": "111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


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

        MOD = 10**9 + 7
        return dp(0, steps)
