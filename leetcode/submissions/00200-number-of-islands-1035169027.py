# Submission title: for Number of Islands
# Submission url  : https://leetcode.com/submissions/detail/1035169027/
# Submission json : {"id": 1035169027, "status_display": "Accepted", "lang": "python3", "question_id": 200, "title_slug": "number-of-islands", "code": "class Solution:\n    def numIslands(self, grid: List[List[str]]) -> int:\n        row_count, col_count = len(grid), len(grid[0])\n        island_count = 0\n        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))\n        queue = set((row, col) \n                    for row in range(row_count) \n                    for col in range(col_count) \n                    if grid[row][col] == \"1\")\n\n        def remove_island(row: int, col: int) -> None:\n            if not 0 <= row < row_count or not 0 <= col < col_count or (row, col) not in queue:\n                return\n\n            queue.remove((row, col))\n\n            for row_delta, col_delta in moves:\n                remove_island(row + row_delta, col + col_delta)    \n\n        while queue:\n            remove_island(*next(iter(queue)))\n            island_count += 1\n\n        return island_count\n\n            ", "title": "Number of Islands", "url": "/submissions/detail/1035169027/", "lang_name": "Python3", "time": "5\u00a0months, 1\u00a0week", "timestamp": 1693323857, "status": 10, "runtime": "871 ms", "is_pending": "Not Pending", "memory": "26.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_count, col_count = len(grid), len(grid[0])
        island_count = 0
        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
        queue = set(
            (row, col)
            for row in range(row_count)
            for col in range(col_count)
            if grid[row][col] == "1"
        )

        def remove_island(row: int, col: int) -> None:
            if (
                not 0 <= row < row_count
                or not 0 <= col < col_count
                or (row, col) not in queue
            ):
                return

            queue.remove((row, col))

            for row_delta, col_delta in moves:
                remove_island(row + row_delta, col + col_delta)

        while queue:
            remove_island(*next(iter(queue)))
            island_count += 1

        return island_count
