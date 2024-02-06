# Submission title: for Number of Islands
# Submission url  : https://leetcode.com/submissions/detail/1035172436/
# Submission json : {"id": 1035172436, "status_display": "Accepted", "lang": "python3", "question_id": 200, "title_slug": "number-of-islands", "code": "class Solution:\n    def numIslands(self, grid: List[List[str]]) -> int:\n        row_count, col_count = len(grid), len(grid[0])\n        island_count = 0\n        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))\n        queue = set((row, col) \n                    for row in range(row_count) \n                    for col in range(col_count) \n                    if grid[row][col] == \"1\")\n\n        @cache\n        def remove_island(row: int, col: int) -> None:\n            if not 0 <= row < row_count or not 0 <= col < col_count:\n                return\n\n            for row_delta, col_delta in moves:\n                new_cell = (row + row_delta, col + col_delta)\n                if new_cell in queue:\n                    queue.remove(new_cell)\n                    remove_island(*new_cell)\n\n        while queue:\n            remove_island(*queue.pop())\n            island_count += 1\n\n        return island_count\n\n            ", "title": "Number of Islands", "url": "/submissions/detail/1035172436/", "lang_name": "Python3", "time": "5\u00a0months, 1\u00a0week", "timestamp": 1693324101, "status": 10, "runtime": "299 ms", "is_pending": "Not Pending", "memory": "30.2 MB", "compare_result": "1111111111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}


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

        @cache
        def remove_island(row: int, col: int) -> None:
            if not 0 <= row < row_count or not 0 <= col < col_count:
                return

            for row_delta, col_delta in moves:
                new_cell = (row + row_delta, col + col_delta)
                if new_cell in queue:
                    queue.remove(new_cell)
                    remove_island(*new_cell)

        while queue:
            remove_island(*queue.pop())
            island_count += 1

        return island_count
