# Submission title: for Number of Islands
# Submission url  : https://leetcode.com/submissions/detail/1035182855/
# Submission json : {"id": 1035182855, "status_display": "Accepted", "lang": "python3", "question_id": 200, "title_slug": "number-of-islands", "code": "class Solution:\n    def numIslands(self, grid: List[List[str]]) -> int:\n        row_count, col_count = len(grid), len(grid[0])\n        island_count = 0\n        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))\n\n        @cache\n        def dfs(row: int, col: int) -> None:\n            if not 0 <= row < row_count or not 0 <= col < col_count or grid[row][col] == \"0\":\n                return\n            \n            grid[row][col] = \"0\"\n            for row_delta, col_delta in moves:\n                dfs(row + row_delta, col + col_delta)\n\n        for row in range(row_count):\n            for col in range(col_count):\n                if grid[row][col] == \"0\":\n                    continue\n\n                dfs(row, col)\n                island_count += 1\n\n        return island_count\n\n            ", "title": "Number of Islands", "url": "/submissions/detail/1035182855/", "lang_name": "Python3", "time": "5\u00a0months, 1\u00a0week", "timestamp": 1693324849, "status": 10, "runtime": "321 ms", "is_pending": "Not Pending", "memory": "34.5 MB", "compare_result": "1111111111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        row_count, col_count = len(grid), len(grid[0])
        island_count = 0
        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))

        @cache
        def dfs(row: int, col: int) -> None:
            if (
                not 0 <= row < row_count
                or not 0 <= col < col_count
                or grid[row][col] == "0"
            ):
                return

            grid[row][col] = "0"
            for row_delta, col_delta in moves:
                dfs(row + row_delta, col + col_delta)

        for row in range(row_count):
            for col in range(col_count):
                if grid[row][col] == "0":
                    continue

                dfs(row, col)
                island_count += 1

        return island_count
