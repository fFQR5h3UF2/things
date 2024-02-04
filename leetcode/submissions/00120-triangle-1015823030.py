# Submission title: for Triangle
# Submission url  : https://leetcode.com/submissions/detail/1015823030/
# Submission json : {"id": 1015823030, "status_display": "Accepted", "lang": "python3", "question_id": 120, "title_slug": "triangle", "code": "class Solution:\n    def minimumTotal(self, triangle: List[List[int]]) -> int:\n        row_count = len(triangle)\n\n\n        @cache\n        def dp(row: int, column: int) -> int:\n            if row == row_count or column == row + 1:\n                return 0\n        \n            return triangle[row][column] + min(dp(row + 1, column), dp(row + 1, column + 1))\n\n        return dp(0, 0)", "title": "Triangle", "url": "/submissions/detail/1015823030/", "lang_name": "Python3", "time": "5\u00a0months, 4\u00a0weeks", "timestamp": 1691512487, "status": 10, "runtime": "73 ms", "is_pending": "Not Pending", "memory": "20.2 MB", "compare_result": "11111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row_count = len(triangle)

        @cache
        def dp(row: int, column: int) -> int:
            if row == row_count or column == row + 1:
                return 0

            return triangle[row][column] + min(
                dp(row + 1, column), dp(row + 1, column + 1)
            )

        return dp(0, 0)
