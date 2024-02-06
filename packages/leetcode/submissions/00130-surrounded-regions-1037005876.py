# Submission title: for Surrounded Regions
# Submission url  : https://leetcode.com/submissions/detail/1037005876/
# Submission json : {"id": 1037005876, "status_display": "Accepted", "lang": "python3", "question_id": 130, "title_slug": "surrounded-regions", "code": "class Solution:\n    def solve(self, board: List[List[str]]) -> None:\n        \"\"\"\n        Do not return anything, modify board in-place instead.\n        \"\"\"\n        row_count, col_count = len(board), len(board[0])\n        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))\n        ignore_stack = set()\n\n        def bfs(row: int, col: int) -> None:\n            if not 0 <= row < row_count or not 0 <= col < col_count:\n                return\n            if (row, col) in ignore_stack or board[row][col] == \"X\":\n                return\n\n            ignore_stack.add((row, col))\n            for row_delta, col_delta in moves:\n                bfs(row + row_delta, col + col_delta)\n        \n        for row, col in itertools.chain(\n            ((0, col) for col in range(col_count)),\n            ((row_count - 1, col) for col in range(col_count)),\n            ((row, 0) for row in range(row_count)),\n            ((row, col_count - 1) for row in range(row_count))\n        ):\n            bfs(row, col)\n        \n        flip_x = True\n        for row in range(1, row_count - 1):\n            for col in range(1, col_count - 1):\n                if (row, col) in ignore_stack:\n                    continue\n\n                board[row][col] = \"X\"\n        ", "title": "Surrounded Regions", "url": "/submissions/detail/1037005876/", "lang_name": "Python3", "time": "5\u00a0months", "timestamp": 1693503299, "status": 10, "runtime": "133 ms", "is_pending": "Not Pending", "memory": "18.3 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row_count, col_count = len(board), len(board[0])
        moves = ((0, 1), (0, -1), (1, 0), (-1, 0))
        ignore_stack = set()

        def bfs(row: int, col: int) -> None:
            if not 0 <= row < row_count or not 0 <= col < col_count:
                return
            if (row, col) in ignore_stack or board[row][col] == "X":
                return

            ignore_stack.add((row, col))
            for row_delta, col_delta in moves:
                bfs(row + row_delta, col + col_delta)

        for row, col in itertools.chain(
            ((0, col) for col in range(col_count)),
            ((row_count - 1, col) for col in range(col_count)),
            ((row, 0) for row in range(row_count)),
            ((row, col_count - 1) for row in range(row_count)),
        ):
            bfs(row, col)

        flip_x = True
        for row in range(1, row_count - 1):
            for col in range(1, col_count - 1):
                if (row, col) in ignore_stack:
                    continue

                board[row][col] = "X"
