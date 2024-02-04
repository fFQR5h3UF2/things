# Submission title: for Factorial Trailing Zeroes
# Submission url  : https://leetcode.com/submissions/detail/1057802784/
# Submission json : {"id": 1057802784, "status_display": "Accepted", "lang": "python3", "question_id": 172, "title_slug": "factorial-trailing-zeroes", "code": "class Solution:\n    def trailingZeroes(self, n: int) -> int:\n        a, b, zeros = 1, 5, 0\n        while (5**a) <= n:\n            zeros += n // b\n            a += 1\n            b *= 5\n        return zeros\n", "title": "Factorial Trailing Zeroes", "url": "/submissions/detail/1057802784/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695548672, "status": 10, "runtime": "38 ms", "is_pending": "Not Pending", "memory": "16.2 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def trailingZeroes(self, n: int) -> int:
        a, b, zeros = 1, 5, 0
        while (5**a) <= n:
            zeros += n // b
            a += 1
            b *= 5
        return zeros
