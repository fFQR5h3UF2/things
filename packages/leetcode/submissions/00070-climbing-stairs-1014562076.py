# Submission title: for Climbing Stairs
# Submission url  : https://leetcode.com/submissions/detail/1014562076/
# Submission json : {"id": 1014562076, "status_display": "Accepted", "lang": "python3", "question_id": 70, "title_slug": "climbing-stairs", "code": "class Solution:\n    def climbStairs(self, n: int) -> int:\n        if n < 3:\n            return n\n\n        minus_one, minus_two = 2, 1\n        for step in range(3, n + 1):\n            minus_one, minus_two = minus_one + minus_two, minus_one\n        \n        return minus_one", "title": "Climbing Stairs", "url": "/submissions/detail/1014562076/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1691401796, "status": 10, "runtime": "36 ms", "is_pending": "Not Pending", "memory": "16.1 MB", "compare_result": "111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        minus_one, minus_two = 2, 1
        for step in range(3, n + 1):
            minus_one, minus_two = minus_one + minus_two, minus_one

        return minus_one
