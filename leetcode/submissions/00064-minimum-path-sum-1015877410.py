# Submission title: for Minimum Path Sum
# Submission url  : https://leetcode.com/submissions/detail/1015877410/
# Submission json : {"id": 1015877410, "status_display": "Accepted", "lang": "python3", "question_id": 64, "title_slug": "minimum-path-sum", "code": "class Solution:\n    def minPathSum(self, grid: List[List[int]]) -> int:\n        row_count = len(grid)\n        column_count = len(grid[0]) if grid else None\n        if not row_count or not column_count:\n            return 0\n\n        dp = [[0] * column_count for _ in range(row_count)]\n        dp[0][0] = grid[0][0]\n\n        for column in range(1, column_count):\n            dp[0][column] = grid[0][column] + dp[0][column - 1]\n\n        for row in range(1, row_count):\n            dp[row][0] = grid[row][0] + dp[row - 1][0]\n\n            for column in range(1, column_count):\n                dp[row][column] = grid[row][column] + min(\n                    dp[row - 1][column], dp[row][column-1]\n                )\n\n        # @cache\n        # def dp(row: int, column: int) -> int:\n        #     if row == row_count or column == column_count:\n        #         return 0\n        #     return grid[row][column] + min(dp(row + 1, column), dp(row, column + 1))\n        #return dp(0, 0)\n\n        return dp[-1][-1]", "title": "Minimum Path Sum", "url": "/submissions/detail/1015877410/", "lang_name": "Python3", "time": "5\u00a0months, 4\u00a0weeks", "timestamp": 1691515881, "status": 10, "runtime": "88 ms", "is_pending": "Not Pending", "memory": "18 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row_count = len(grid)
        column_count = len(grid[0]) if grid else None
        if not row_count or not column_count:
            return 0

        dp = [[0] * column_count for _ in range(row_count)]
        dp[0][0] = grid[0][0]

        for column in range(1, column_count):
            dp[0][column] = grid[0][column] + dp[0][column - 1]

        for row in range(1, row_count):
            dp[row][0] = grid[row][0] + dp[row - 1][0]

            for column in range(1, column_count):
                dp[row][column] = grid[row][column] + min(
                    dp[row - 1][column], dp[row][column - 1]
                )

        # @cache
        # def dp(row: int, column: int) -> int:
        #     if row == row_count or column == column_count:
        #         return 0
        #     return grid[row][column] + min(dp(row + 1, column), dp(row, column + 1))
        # return dp(0, 0)

        return dp[-1][-1]
