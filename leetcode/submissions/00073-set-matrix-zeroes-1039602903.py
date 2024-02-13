# Submission title: Set Matrix Zeroes
# Submission url  : https://leetcode.com/problems/set-matrix-zeroes/description/
# Submission url  : https://leetcode.com/submissions/detail/1039602903/
# Submission json : {"id":1039602903,"status_display":"Accepted","lang":"python3","question_id":73,"title_slug":"set-matrix-zeroes","code":"class Solution:\n    def setZeroes(self, matrix: List[List[int]]) -> None:\n        \"\"\"\n        Do not return anything, modify matrix in-place instead.\n        \"\"\"\n        rows_count, cols_count = len(matrix), len(matrix[0])\n        flip_rows, flip_cols = set(), set()\n\n        for row in range(rows_count):\n            for col in range(cols_count):\n                if matrix[row][col] == 0:\n                    flip_rows.add(row)\n                    flip_cols.add(col)\n\n        while flip_rows:\n            row = flip_rows.pop()\n            for col in range(cols_count):\n                if matrix[row][col] != 0:\n                    matrix[row][col] = 0\n        \n        while flip_cols:\n            col = flip_cols.pop()\n            for row in range(rows_count):\n                if matrix[row][col] != 0:\n                    matrix[row][col] = 0\n        \n            \n","title":"Set Matrix Zeroes","url":"/submissions/detail/1039602903/","lang_name":"Python3","time":"5 months","timestamp":1693759778,"status":10,"runtime":"121 ms","is_pending":"Not Pending","memory":"17.3 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows_count, cols_count = len(matrix), len(matrix[0])
        flip_rows, flip_cols = set(), set()

        for row in range(rows_count):
            for col in range(cols_count):
                if matrix[row][col] == 0:
                    flip_rows.add(row)
                    flip_cols.add(col)

        while flip_rows:
            row = flip_rows.pop()
            for col in range(cols_count):
                if matrix[row][col] != 0:
                    matrix[row][col] = 0

        while flip_cols:
            col = flip_cols.pop()
            for row in range(rows_count):
                if matrix[row][col] != 0:
                    matrix[row][col] = 0
