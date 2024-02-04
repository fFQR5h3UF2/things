# Submission for Minimum Falling Path Sum
# Submission url: https://leetcode.com/submissions/detail/1150538234/


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length = len(matrix)
        max_val = 101

        @cache
        def dp(row: int, col: int) -> int:
            if not 0 <= col < length:
                return max_val
            val = matrix[row][col]
            if row == length - 1:
                return val
            new_row = row + 1
            return val + min(
                dp(new_row, col + 1), dp(new_row, col), dp(new_row, col - 1)
            )

        return min(dp(0, col) for col in range(length))
