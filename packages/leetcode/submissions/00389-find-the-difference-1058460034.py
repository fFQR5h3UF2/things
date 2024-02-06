# Submission title: for Find the Difference
# Submission url  : https://leetcode.com/submissions/detail/1058460034/
# Submission json : {"id": 1058460034, "status_display": "Accepted", "lang": "python3", "question_id": 389, "title_slug": "find-the-difference", "code": "class Solution:\n    def findTheDifference(self, s: str, t: str) -> str:\n        count = Counter(s)\n        for char in t:\n            count[char] -= 1\n            if count[char] == -1:\n                return char", "title": "Find the Difference", "url": "/submissions/detail/1058460034/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695619598, "status": 10, "runtime": "33 ms", "is_pending": "Not Pending", "memory": "16.2 MB", "compare_result": "111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(s)
        for char in t:
            count[char] -= 1
            if count[char] == -1:
                return char
