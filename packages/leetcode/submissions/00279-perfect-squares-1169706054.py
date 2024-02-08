# Submission title: for Perfect Squares
# Submission url  : https://leetcode.com/submissions/detail/1169706054/
# Submission json : {"id": 1169706054, "status_display": "Accepted", "lang": "python3", "question_id": 279, "title_slug": "perfect-squares", "code": "class Solution:\n    def numSquares(self, n: int) -> int:\n        dp = [float('inf')] * (n + 1)\n        dp[0] = 0\n        for i in range(1, n + 1):\n            min_val = float('inf')\n            j = 1\n            while j * j <= i:\n                min_val = min(min_val, dp[i - j * j] + 1)\n                j += 1\n            dp[i] = min_val\n        return dp[n]\n\n", "title": "Perfect Squares", "url": "/submissions/detail/1169706054/", "lang_name": "Python3", "time": "1\u00a0minute", "timestamp": 1707396603, "status": 10, "runtime": "2443 ms", "is_pending": "Not Pending", "memory": "16.6 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            min_val = float("inf")
            j = 1
            while j * j <= i:
                min_val = min(min_val, dp[i - j * j] + 1)
                j += 1
            dp[i] = min_val
        return dp[n]
