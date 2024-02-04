# Submission title: for Counting Bits
# Submission url  : https://leetcode.com/submissions/detail/1037438619/
# Submission json : {"id": 1037438619, "status_display": "Accepted", "lang": "python3", "question_id": 338, "title_slug": "counting-bits", "code": "class Solution:\n    def countBits(self, n: int) -> List[int]:\n        ans = [0] * (n + 1)\n        for i in range(1, n + 1):\n            ans[i] = ans[i >> 1] + (i & 1)\n        return ans", "title": "Counting Bits", "url": "/submissions/detail/1037438619/", "lang_name": "Python3", "time": "5\u00a0months", "timestamp": 1693551500, "status": 10, "runtime": "72 ms", "is_pending": "Not Pending", "memory": "23 MB", "compare_result": "111111111111111", "has_notes": true, "flag_type": 1}


class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        for i in range(1, n + 1):
            ans[i] = ans[i >> 1] + (i & 1)
        return ans
