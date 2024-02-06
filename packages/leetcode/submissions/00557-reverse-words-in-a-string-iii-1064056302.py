# Submission title: for Reverse Words in a String III
# Submission url  : https://leetcode.com/submissions/detail/1064056302/
# Submission json : {"id": 1064056302, "status_display": "Accepted", "lang": "python3", "question_id": 557, "title_slug": "reverse-words-in-a-string-iii", "code": "class Solution:\n    def reverseWords(self, s: str) -> str:\n        return ' '.join(map(lambda word: word[::-1], s.split()))\n", "title": "Reverse Words in a String III", "url": "/submissions/detail/1064056302/", "lang_name": "Python3", "time": "4\u00a0months", "timestamp": 1696166948, "status": 10, "runtime": "28 ms", "is_pending": "Not Pending", "memory": "17 MB", "compare_result": "11111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(map(lambda word: word[::-1], s.split()))
