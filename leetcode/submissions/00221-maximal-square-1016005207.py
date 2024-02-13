# Submission title: Maximal Square
# Submission url  : https://leetcode.com/problems/maximal-square/description/
# Submission url  : https://leetcode.com/submissions/detail/1016005207/
# Submission json : {"id":1016005207,"status_display":"Accepted","lang":"python3","question_id":221,"title_slug":"maximal-square","code":"class Solution:\n    def maximalSquare(self, matrix: List[List[str]]) -> int:\n        row_count, column_count = len(matrix), len(matrix[0])\n        \n        dp = [[0] * column_count for _ in range(row_count)]\n        \n        max_size = 0\n        for column in range(column_count):\n            if matrix[0][column] == \"0\":\n                continue\n            dp[0][column] = 1\n            max_size = 1\n\n        for row in range(row_count):\n            if matrix[row][0] == \"0\":\n                continue\n            dp[row][0] = 1\n            max_size = 1\n        \n        for row in range(1, row_count):\n            for column in range(1, column_count):\n                if matrix[row][column] == \"0\":\n                    continue\n                \n                value = min(dp[row-1][column], dp[row][column-1], dp[row-1][column-1]) + 1\n                dp[row][column] = value\n                max_size = max(max_size, value)\n        \n        return max_size * max_size\n","title":"Maximal Square","url":"/submissions/detail/1016005207/","lang_name":"Python3","time":"5 months, 4 weeks","timestamp":1691524596,"status":10,"runtime":"584 ms","is_pending":"Not Pending","memory":"19.1 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        row_count, column_count = len(matrix), len(matrix[0])

        dp = [[0] * column_count for _ in range(row_count)]

        max_size = 0
        for column in range(column_count):
            if matrix[0][column] == "0":
                continue
            dp[0][column] = 1
            max_size = 1

        for row in range(row_count):
            if matrix[row][0] == "0":
                continue
            dp[row][0] = 1
            max_size = 1

        for row in range(1, row_count):
            for column in range(1, column_count):
                if matrix[row][column] == "0":
                    continue

                value = (
                    min(
                        dp[row - 1][column],
                        dp[row][column - 1],
                        dp[row - 1][column - 1],
                    )
                    + 1
                )
                dp[row][column] = value
                max_size = max(max_size, value)

        return max_size * max_size
