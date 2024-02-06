# Submission title: for XOR Operation in an Array
# Submission url  : https://leetcode.com/submissions/detail/1056131848/
# Submission json : {"id": 1056131848, "status_display": "Accepted", "lang": "python3", "question_id": 1610, "title_slug": "xor-operation-in-an-array", "code": "class Solution:\n    def xorOperation(self, n: int, start: int) -> int:\n        return reduce(lambda total, i: total ^ (start + 2 * i), chain((0, ), range(n)))", "title": "XOR Operation in an Array", "url": "/submissions/detail/1056131848/", "lang_name": "Python3", "time": "4\u00a0months, 2\u00a0weeks", "timestamp": 1695371035, "status": 10, "runtime": "38 ms", "is_pending": "Not Pending", "memory": "16 MB", "compare_result": "111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        return reduce(lambda total, i: total ^ (start + 2 * i), chain((0,), range(n)))
