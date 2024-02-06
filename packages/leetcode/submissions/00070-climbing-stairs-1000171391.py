# Submission title: for Climbing Stairs
# Submission url  : https://leetcode.com/submissions/detail/1000171391/
# Submission json : {"id": 1000171391, "status_display": "Accepted", "lang": "python3", "question_id": 70, "title_slug": "climbing-stairs", "code": "class Solution:\n    # 1: 1\n    # 2: 2\n    # 3: 3 [2(2), 1(1)]\n    # 4: 5 [3(3), (2)]\n    def climbStairs(self, n: int) -> int:\n        if n < 3:\n            return n\n\n        count, count_prev = 2, 1\n        for number in range(3, n + 1):\n            count, count_prev = count + count_prev, count\n        return count", "title": "Climbing Stairs", "url": "/submissions/detail/1000171391/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1689943974, "status": 10, "runtime": "39 ms", "is_pending": "Not Pending", "memory": "16.1 MB", "compare_result": "111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    # 1: 1
    # 2: 2
    # 3: 3 [2(2), 1(1)]
    # 4: 5 [3(3), (2)]
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n

        count, count_prev = 2, 1
        for number in range(3, n + 1):
            count, count_prev = count + count_prev, count
        return count
