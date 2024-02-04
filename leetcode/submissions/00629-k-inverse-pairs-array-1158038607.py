# Submission title: for K Inverse Pairs Array
# Submission url  : https://leetcode.com/submissions/detail/1158038607/
# Submission json : {"id": 1158038607, "status_display": "Accepted", "lang": "python3", "question_id": 629, "title_slug": "k-inverse-pairs-array", "code": "class Solution:\n    def kInversePairs(self, n: int, k: int) -> int:\n        MOD = 10**9 + 7\n        dp = [[0] * (k + 1) for _ in range(n + 1)]\n\n        for i in range(1, n + 1):\n            for j in range(k + 1):\n                if j == 0:\n                    dp[i][j] = 1\n                else:\n                    val = (dp[i - 1][j] + MOD - (dp[i - 1][j - i] if j - i >= 0 else 0)) % MOD\n                    dp[i][j] = (dp[i][j - 1] + val) % MOD\n\n        return (dp[n][k] + MOD - (dp[n][k - 1] if k > 0 else 0)) % MOD\n", "title": "K Inverse Pairs Array", "url": "/submissions/detail/1158038607/", "lang_name": "Python3", "time": "1\u00a0week, 1\u00a0day", "timestamp": 1706339151, "status": 10, "runtime": "342 ms", "is_pending": "Not Pending", "memory": "55.6 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0] * (k + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(k + 1):
                if j == 0:
                    dp[i][j] = 1
                else:
                    val = (
                        dp[i - 1][j] + MOD - (dp[i - 1][j - i] if j - i >= 0 else 0)
                    ) % MOD
                    dp[i][j] = (dp[i][j - 1] + val) % MOD

        return (dp[n][k] + MOD - (dp[n][k - 1] if k > 0 else 0)) % MOD
