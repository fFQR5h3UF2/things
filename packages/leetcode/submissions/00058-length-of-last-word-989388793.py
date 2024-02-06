# Submission title: for Length of Last Word
# Submission url  : https://leetcode.com/submissions/detail/989388793/
# Submission json : {"id": 989388793, "status_display": "Accepted", "lang": "python3", "question_id": 58, "title_slug": "length-of-last-word", "code": "class Solution:\n    def lengthOfLastWord(self, s: str) -> int:\n        return len(s.split()[-1])", "title": "Length of Last Word", "url": "/submissions/detail/989388793/", "lang_name": "Python3", "time": "7\u00a0months", "timestamp": 1688829939, "status": 10, "runtime": "36 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
