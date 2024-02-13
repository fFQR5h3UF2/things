# Submission title: Unique Paths II
# Submission url  : https://leetcode.com/problems/unique-paths-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1015893189/
# Submission json : {"id":1015893189,"status_display":"Accepted","lang":"python3","question_id":63,"title_slug":"unique-paths-ii","code":"class Solution:\n    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:\n        row_count = len(obstacleGrid)\n        column_count = len(obstacleGrid[0])\n        # dp = [[0] * column_count for _ in range(row_count)]\n\n        # for row in range(row_count):\n        #     for column in range(column_count):\n\n        @cache\n        def dp(row: int, column: int) -> int:\n            if row == row_count or column == column_count or obstacleGrid[row][column] == 1:\n                return 0\n            \n            if row == row_count - 1 and column == column_count - 1:\n                return 1\n            \n            return dp(row + 1, column) + dp(row, column + 1)\n        \n        return dp(0, 0)","title":"Unique Paths II","url":"/submissions/detail/1015893189/","lang_name":"Python3","time":"5 months, 4 weeks","timestamp":1691516839,"status":10,"runtime":"54 ms","is_pending":"Not Pending","memory":"16.6 MB","compare_result":"11111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row_count = len(obstacleGrid)
        column_count = len(obstacleGrid[0])
        # dp = [[0] * column_count for _ in range(row_count)]

        # for row in range(row_count):
        #     for column in range(column_count):

        @cache
        def dp(row: int, column: int) -> int:
            if (
                row == row_count
                or column == column_count
                or obstacleGrid[row][column] == 1
            ):
                return 0

            if row == row_count - 1 and column == column_count - 1:
                return 1

            return dp(row + 1, column) + dp(row, column + 1)

        return dp(0, 0)
