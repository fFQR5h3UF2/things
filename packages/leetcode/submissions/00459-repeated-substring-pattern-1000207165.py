# Submission title: for Repeated Substring Pattern
# Submission url  : https://leetcode.com/submissions/detail/1000207165/
# Submission json : {"id": 1000207165, "status_display": "Accepted", "lang": "python3", "question_id": 459, "title_slug": "repeated-substring-pattern", "code": "class Solution:\n    def repeatedSubstringPattern(self, s: str) -> bool:\n        length = len(s)\n        for i in range(length-1):\n            if length % (i + 1) != 0:\n                continue\n            \n            if s == s[:i+1] * (length // (i + 1)):\n                return True\n        \n        return False", "title": "Repeated Substring Pattern", "url": "/submissions/detail/1000207165/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1689947602, "status": 10, "runtime": "82 ms", "is_pending": "Not Pending", "memory": "16.5 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(length - 1):
            if length % (i + 1) != 0:
                continue

            if s == s[: i + 1] * (length // (i + 1)):
                return True

        return False
