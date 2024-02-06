# Submission title: for Integer Break
# Submission url  : https://leetcode.com/submissions/detail/1068472872/
# Submission json : {"id": 1068472872, "status_display": "Accepted", "lang": "python3", "question_id": 343, "title_slug": "integer-break", "code": "class Solution:\n    def integerBreak(self, n: int) -> int:\n        @cache\n        def dp(num: int) -> int:\n            if num <= 3:\n                return num\n            ans = num\n            for i in range(2, num):\n                ans = max(ans, i * dp(num - i))\n            return ans\n\n        return dp(n) if n > 3 else n - 1", "title": "Integer Break", "url": "/submissions/detail/1068472872/", "lang_name": "Python3", "time": "4\u00a0months", "timestamp": 1696584249, "status": 10, "runtime": "39 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "11111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def integerBreak(self, n: int) -> int:
        @cache
        def dp(num: int) -> int:
            if num <= 3:
                return num
            ans = num
            for i in range(2, num):
                ans = max(ans, i * dp(num - i))
            return ans

        return dp(n) if n > 3 else n - 1
