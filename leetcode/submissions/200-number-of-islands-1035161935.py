# Submission for Number of Islands
# Submission url: https://leetcode.com/submissions/detail/1035161935/


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_count, col_count = len(grid), len(grid[0])

        island_count = 0
        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
        queue = set(
            (row, col)
            for row in range(row_count)
            for col in range(col_count)
            if grid[row][col] == 1
        )

        def remove_island(row: int, col: int) -> None:
            if not 0 <= row < row_count or not 0 <= col < col_count:
                continue

            queue.remove((row, col))

            for row_delta, col_delta in moves:
                remove_island(row + row_delta, col + col_delta)

        while queue:
            island_count += 1
            remove_island(*queue.pop())

        return island_count
