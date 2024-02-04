# Submission for Minimum Falling Path Sum
# Submission url: https://leetcode.com/submissions/detail/1150532886/


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        length = len(matrix)

        deltas = ((1, 0), (1, 1), (1, -1))

        @cache
        def dp(row: int, col: int) -> int:
            val = matrix[row][col]
            min_cost = None
            for delta_row, delta_col in deltas:
                new_row, new_col = row + delta_row, col + delta_col
                if new_row >= length or new_col >= length:
                    continue
                new_cost = dp(new_row, new_col)
                if min_cost is None:
                    min_cost = new_cost
                else:
                    min_cost = min(min_cost, new_cost)
            return val + (min_cost if min_cost is not None else 0)

        return min(dp(0, col) for col in range(length))
