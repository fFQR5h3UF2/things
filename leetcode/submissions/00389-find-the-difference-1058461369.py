# Submission title: for Find the Difference
# Submission url  : https://leetcode.com/submissions/detail/1058461369/
# Submission json : {"id": 1058461369, "status_display": "Accepted", "lang": "python3", "question_id": 389, "title_slug": "find-the-difference", "code": "class Solution:\n    def findTheDifference(self, s: str, t: str) -> str:\n        return chr(reduce(operator.xor, (ord(char) for char in chain(s, t))))", "title": "Find the Difference", "url": "/submissions/detail/1058461369/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695619717, "status": 10, "runtime": "40 ms", "is_pending": "Not Pending", "memory": "16.2 MB", "compare_result": "111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(reduce(operator.xor, (ord(char) for char in chain(s, t))))
