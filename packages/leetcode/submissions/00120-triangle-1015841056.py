# Submission title: for Triangle
# Submission url  : https://leetcode.com/submissions/detail/1015841056/
# Submission json : {"id": 1015841056, "status_display": "Accepted", "lang": "python3", "question_id": 120, "title_slug": "triangle", "code": "class Solution:\n    def minimumTotal(self, triangle: List[List[int]]) -> int:\n        row_count = len(triangle)\n        dp = [[0] * row_count for _ in range(row_count)]\n        dp[0][0] = triangle[0][0]\n\n        for row in range(1, row_count):\n            dp[row][0] = triangle[row][0] + dp[row-1][0]\n            dp[row][row] = triangle[row][row] + dp[row-1][row-1]\n\n            for column in range(1, row):\n                dp[row][column] = triangle[row][column] + min(\n                    dp[row-1][column], dp[row-1][column-1]\n                )\n\n        return min(dp[-1])", "title": "Triangle", "url": "/submissions/detail/1015841056/", "lang_name": "Python3", "time": "5\u00a0months, 4\u00a0weeks", "timestamp": 1691513630, "status": 10, "runtime": "77 ms", "is_pending": "Not Pending", "memory": "17.8 MB", "compare_result": "11111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        row_count = len(triangle)
        dp = [[0] * row_count for _ in range(row_count)]
        dp[0][0] = triangle[0][0]

        for row in range(1, row_count):
            dp[row][0] = triangle[row][0] + dp[row - 1][0]
            dp[row][row] = triangle[row][row] + dp[row - 1][row - 1]

            for column in range(1, row):
                dp[row][column] = triangle[row][column] + min(
                    dp[row - 1][column], dp[row - 1][column - 1]
                )

        return min(dp[-1])
