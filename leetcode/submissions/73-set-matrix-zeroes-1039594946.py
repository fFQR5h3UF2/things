# Submission for Set Matrix Zeroes
# Submission url: https://leetcode.com/submissions/detail/1039594946/


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        side_length = len(matrix)
        flip_rows, flip_cols = set(), set()

        for row in range(side_length):
            for col in range(side_length):
                if col in flip_cols:
                    continue

                if matrix[row][col] == 0:
                    flip_rows.add(row)
                    flip_cols.add(col)

        while flip_rows:
            row = flip_rows.pop()
            for col in range(side_length):
                if matrix[row][col] == 1:
                    matrix[row][col] = 0

        while flip_cols:
            col = flip_cols.pop()
            for row in range(side_length):
                if matrix[row][col] == 1:
                    matrix[row][col] = 0
