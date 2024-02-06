# Submission title: for Is Subsequence
# Submission url  : https://leetcode.com/submissions/detail/1056031768/
# Submission json : {"id": 1056031768, "status_display": "Accepted", "lang": "python3", "question_id": 392, "title_slug": "is-subsequence", "code": "class Solution:\n    def isSubsequence(self, s: str, t: str) -> bool:\n        i = 0\n        length = len(s)\n        for char in t:\n            if i == length:\n                break\n            if s[i] == char:\n                i += 1\n            \n        return i == length", "title": "Is Subsequence", "url": "/submissions/detail/1056031768/", "lang_name": "Python3", "time": "4\u00a0months, 2\u00a0weeks", "timestamp": 1695362226, "status": 10, "runtime": "38 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        length = len(s)
        for char in t:
            if i == length:
                break
            if s[i] == char:
                i += 1

        return i == length
