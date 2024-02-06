# Submission title: for Reverse Words in a String
# Submission url  : https://leetcode.com/submissions/detail/997596378/
# Submission json : {"id": 997596378, "status_display": "Accepted", "lang": "python3", "question_id": 151, "title_slug": "reverse-words-in-a-string", "code": "class Solution:\n    def reverseWords(self, s: str) -> str:\n        return \" \".join(s.split()[::-1])", "title": "Reverse Words in a String", "url": "/submissions/detail/997596378/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689687700, "status": 10, "runtime": "60 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
