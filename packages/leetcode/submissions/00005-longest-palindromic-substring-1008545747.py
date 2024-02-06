# Submission title: for Longest Palindromic Substring
# Submission url  : https://leetcode.com/submissions/detail/1008545747/
# Submission json : {"id": 1008545747, "status_display": "Accepted", "lang": "python3", "question_id": 5, "title_slug": "longest-palindromic-substring", "code": "class Solution:\n    def longestPalindrome(self, s: str) -> str:\n        n = len(s)\n        dp = [[False] * n for _ in range(n)]\n        ans = [0, 0]\n        \n        for i in range(n):\n            dp[i][i] = True\n        \n        for i in range(n - 1):\n            if s[i] == s[i + 1]:\n                dp[i][i + 1] = True\n                ans = [i, i + 1]\n\n        for diff in range(2, n):\n            for i in range(n - diff):\n                j = i + diff\n                if s[i] == s[j] and dp[i + 1][j - 1]:\n                    dp[i][j] = True\n                    ans = [i, j]\n\n        i, j = ans\n        return s[i:j + 1]", "title": "Longest Palindromic Substring", "url": "/submissions/detail/1008545747/", "lang_name": "Python3", "time": "6\u00a0months, 1\u00a0week", "timestamp": 1690813065, "status": 10, "runtime": "2069 ms", "is_pending": "Not Pending", "memory": "24.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i : j + 1]
