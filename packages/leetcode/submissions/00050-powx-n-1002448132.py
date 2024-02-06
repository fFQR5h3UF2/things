# Submission title: for Pow(x, n)
# Submission url  : https://leetcode.com/submissions/detail/1002448132/
# Submission json : {"id": 1002448132, "status_display": "Accepted", "lang": "python3", "question_id": 50, "title_slug": "powx-n", "code": "class Solution:\n    def myPow(self, x: float, n: int) -> float:\n        if n == 0:\n            return 1\n\n        if n < 0:\n            n *= -1\n            x = 1 / x\n\n        result = 1\n        while n:\n            if n % 2:\n                result *= x\n                n -= 1\n            x *= x\n            n //= 2\n        \n        return result", "title": "Pow(x, n)", "url": "/submissions/detail/1002448132/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690186380, "status": 10, "runtime": "47 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1

        if n < 0:
            n *= -1
            x = 1 / x

        result = 1
        while n:
            if n % 2:
                result *= x
                n -= 1
            x *= x
            n //= 2

        return result
