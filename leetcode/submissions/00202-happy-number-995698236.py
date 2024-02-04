# Submission title: for Happy Number
# Submission url  : https://leetcode.com/submissions/detail/995698236/
# Submission json : {"id": 995698236, "status_display": "Accepted", "lang": "python3", "question_id": 202, "title_slug": "happy-number", "code": "class Solution:\n    def isHappy(self, n: int) -> bool:\n        while True:\n            sum = 0\n            while n > 0:\n                sum += (n % 10 )**2\n                n = n // 10\n            n = sum\n            if sum < 10:\n                break\n\n        return n in [1, 7]", "title": "Happy Number", "url": "/submissions/detail/995698236/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689493303, "status": 10, "runtime": "50 ms", "is_pending": "Not Pending", "memory": "16.2 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def isHappy(self, n: int) -> bool:
        while True:
            sum = 0
            while n > 0:
                sum += (n % 10) ** 2
                n = n // 10
            n = sum
            if sum < 10:
                break

        return n in [1, 7]
