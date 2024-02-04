# Submission title: for Factorial Trailing Zeroes
# Submission url  : https://leetcode.com/submissions/detail/1057804154/
# Submission json : {"id": 1057804154, "status_display": "Accepted", "lang": "python3", "question_id": 172, "title_slug": "factorial-trailing-zeroes", "code": "class Solution:\n    def trailingZeroes(self, n: int) -> int:\n        zeros = 0\n        while n != 0:\n            new_n = n // 5\n            zeros += new_n\n            n = new_n\n        return zeros\n        \n", "title": "Factorial Trailing Zeroes", "url": "/submissions/detail/1057804154/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695548826, "status": 10, "runtime": "34 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def trailingZeroes(self, n: int) -> int:
        zeros = 0
        while n != 0:
            new_n = n // 5
            zeros += new_n
            n = new_n
        return zeros
