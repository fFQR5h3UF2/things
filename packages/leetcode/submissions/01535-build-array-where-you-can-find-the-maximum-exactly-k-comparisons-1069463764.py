# Submission title: for Build Array Where You Can Find The Maximum Exactly K Comparisons
# Submission url  : https://leetcode.com/submissions/detail/1069463764/
# Submission json : {"id": 1069463764, "status_display": "Accepted", "lang": "python3", "question_id": 1535, "title_slug": "build-array-where-you-can-find-the-maximum-exactly-k-comparisons", "code": "class Solution:\n    def numOfArrays(self, n: int, m: int, k: int) -> int:\n        @cache\n        def dp(i, max_so_far, remain):\n            if i == n:\n                if remain == 0:\n                    return 1\n                \n                return 0\n            \n            ans = (max_so_far * dp(i + 1, max_so_far, remain)) % MOD\n            for num in range(max_so_far + 1, m + 1):\n                ans = (ans + dp(i + 1, num, remain - 1)) % MOD\n                \n            return ans\n        \n        MOD = 10 ** 9 + 7\n        return dp(0, 0, k)", "title": "Build Array Where You Can Find The Maximum Exactly K Comparisons", "url": "/submissions/detail/1069463764/", "lang_name": "Python3", "time": "3\u00a0months, 4\u00a0weeks", "timestamp": 1696697290, "status": 10, "runtime": "867 ms", "is_pending": "Not Pending", "memory": "43.5 MB", "compare_result": "1111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        @cache
        def dp(i, max_so_far, remain):
            if i == n:
                if remain == 0:
                    return 1

                return 0

            ans = (max_so_far * dp(i + 1, max_so_far, remain)) % MOD
            for num in range(max_so_far + 1, m + 1):
                ans = (ans + dp(i + 1, num, remain - 1)) % MOD

            return ans

        MOD = 10**9 + 7
        return dp(0, 0, k)
