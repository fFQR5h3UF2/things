# Submission title: for Number Complement
# Submission url  : https://leetcode.com/submissions/detail/1055524154/
# Submission json : {"id": 1055524154, "status_display": "Accepted", "lang": "python3", "question_id": 476, "title_slug": "number-complement", "code": "class Solution:\n    def findComplement(self, num: int) -> int:\n        return ~num + (1 << num.bit_length())", "title": "Number Complement", "url": "/submissions/detail/1055524154/", "lang_name": "Python3", "time": "4\u00a0months, 2\u00a0weeks", "timestamp": 1695310383, "status": 10, "runtime": "40 ms", "is_pending": "Not Pending", "memory": "16.2 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def findComplement(self, num: int) -> int:
        return ~num + (1 << num.bit_length())
