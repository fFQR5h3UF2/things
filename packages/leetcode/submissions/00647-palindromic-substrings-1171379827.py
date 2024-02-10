# Submission title: for Palindromic Substrings
# Submission url  : https://leetcode.com/submissions/detail/1171379827/
# Submission json : {"id": 1171379827, "status_display": "Accepted", "lang": "python3", "question_id": 647, "title_slug": "palindromic-substrings", "code": "class Solution:\n    def countSubstrings(self, s: str) -> int:\n        n = len(s)\n        palindrome = [[False] * n for _ in range(n)]\n        ans = 0\n\n        for i in range(n):\n            palindrome[i][i] = True\n            ans += 1\n\n        for i in range(n - 1):\n            if s[i] == s[i + 1]:\n                palindrome[i][i + 1] = True\n                ans += 1\n\n        for length in range(3, n + 1):\n            for i in range(n - length + 1):\n                if s[i] == s[i + length - 1] and palindrome[i + 1][i + length - 2]:\n                    palindrome[i][i + length - 1] = True\n                    ans += 1\n\n        return ans", "title": "Palindromic Substrings", "url": "/submissions/detail/1171379827/", "lang_name": "Python3", "time": "18\u00a0minutes", "timestamp": 1707567173, "status": 10, "runtime": "159 ms", "is_pending": "Not Pending", "memory": "24.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        palindrome = [[False] * n for _ in range(n)]
        ans = 0

        for i in range(n):
            palindrome[i][i] = True
            ans += 1

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                palindrome[i][i + 1] = True
                ans += 1

        for length in range(3, n + 1):
            for i in range(n - length + 1):
                if s[i] == s[i + length - 1] and palindrome[i + 1][i + length - 2]:
                    palindrome[i][i + length - 1] = True
                    ans += 1

        return ans
