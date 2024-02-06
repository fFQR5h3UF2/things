# Submission title: for Strange Printer
# Submission url  : https://leetcode.com/submissions/detail/1007875491/
# Submission json : {"id": 1007875491, "status_display": "Accepted", "lang": "python3", "question_id": 664, "title_slug": "strange-printer", "code": "class Solution:\n    def strangePrinter(self, s: str) -> int:\n        n = len(s)\n        dp = [[n] * n for _ in range(n)]\n        for length in range(1, n + 1):\n            for left in range(n - length + 1):\n                right = left + length - 1\n                j = -1\n                for i in range(left, right):\n                    if s[i] != s[right] and j == -1:\n                        j = i\n                    if j != -1:\n                        dp[left][right] = min(dp[left][right], 1 + dp[j][i] + dp[i + 1][right])\n        \n                if j == -1:\n                    dp[left][right] = 0\n\n        return dp[0][n - 1] + 1", "title": "Strange Printer", "url": "/submissions/detail/1007875491/", "lang_name": "Python3", "time": "6\u00a0months, 1\u00a0week", "timestamp": 1690737074, "status": 10, "runtime": "1399 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def strangePrinter(self, s: str) -> int:
        n = len(s)
        dp = [[n] * n for _ in range(n)]
        for length in range(1, n + 1):
            for left in range(n - length + 1):
                right = left + length - 1
                j = -1
                for i in range(left, right):
                    if s[i] != s[right] and j == -1:
                        j = i
                    if j != -1:
                        dp[left][right] = min(
                            dp[left][right], 1 + dp[j][i] + dp[i + 1][right]
                        )

                if j == -1:
                    dp[left][right] = 0

        return dp[0][n - 1] + 1
