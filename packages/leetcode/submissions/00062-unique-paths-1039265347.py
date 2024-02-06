# Submission title: for Unique Paths
# Submission url  : https://leetcode.com/submissions/detail/1039265347/
# Submission json : {"id": 1039265347, "status_display": "Accepted", "lang": "python3", "question_id": 62, "title_slug": "unique-paths", "code": "class Solution:\n    def uniquePaths(self, m: int, n: int) -> int:\n\n        @cache\n        def dp(row: int, col: int) -> int:\n            if not 0 <= row < m or not 0 <= col < n:\n                return 0\n            \n            if row == m - 1 and col == n - 1:\n                return 1\n            \n            return dp(row + 1, col) + dp(row, col + 1)\n\n        return dp(0, 0)", "title": "Unique Paths", "url": "/submissions/detail/1039265347/", "lang_name": "Python3", "time": "5\u00a0months", "timestamp": 1693729437, "status": 10, "runtime": "45 ms", "is_pending": "Not Pending", "memory": "16.5 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def dp(row: int, col: int) -> int:
            if not 0 <= row < m or not 0 <= col < n:
                return 0

            if row == m - 1 and col == n - 1:
                return 1

            return dp(row + 1, col) + dp(row, col + 1)

        return dp(0, 0)
