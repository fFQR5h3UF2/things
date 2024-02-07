# Submission title: for Repeated Substring Pattern
# Submission url  : https://leetcode.com/submissions/detail/1027362193/
# Submission json : {"id": 1027362193, "status_display": "Accepted", "lang": "python3", "question_id": 459, "title_slug": "repeated-substring-pattern", "code": "class Solution:\n    def repeatedSubstringPattern(self, s: str) -> bool:\n        length = len(s)\n        for i in range(1, length // 2 + 1):\n            if length % i != 0:\n                continue\n            \n            if s == s[:i] * (length // i):\n                return True\n        \n        return False", "title": "Repeated Substring Pattern", "url": "/submissions/detail/1027362193/", "lang_name": "Python3", "time": "5\u00a0months, 2\u00a0weeks", "timestamp": 1692599394, "status": 10, "runtime": "43 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(1, length // 2 + 1):
            if length % i != 0:
                continue

            if s == s[:i] * (length // i):
                return True

        return False