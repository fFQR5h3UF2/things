# Submission title: for Number of 1 Bits
# Submission url  : https://leetcode.com/submissions/detail/1057806680/
# Submission json : {"id": 1057806680, "status_display": "Accepted", "lang": "python3", "question_id": 191, "title_slug": "number-of-1-bits", "code": "class Solution:\n    def hammingWeight(self, n: int) -> int:\n        count = 0\n        while n > 0:\n            if n & 1 != 0:\n                count += 1\n            n >>= 1\n        return count", "title": "Number of 1 Bits", "url": "/submissions/detail/1057806680/", "lang_name": "Python3", "time": "4\u00a0months, 1\u00a0week", "timestamp": 1695549107, "status": 10, "runtime": "43 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            if n & 1 != 0:
                count += 1
            n >>= 1
        return count
