# Submission title: Game of Life
# Submission url  : https://leetcode.com/problems/game-of-life/description/
# Submission url  : https://leetcode.com/submissions/detail/1039615645/
# Submission json : {"id":1039615645,"status_display":"Accepted","lang":"python3","question_id":289,"title_slug":"game-of-life","code":"class Solution:\n    def gameOfLife(self, board: List[List[int]]) -> None:\n        \"\"\"\n        Do not return anything, modify board in-place instead.\n        \"\"\"\n        rows_count, cols_count = len(board), len(board[0])\n        moves = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))\n        flip_cells = set()\n        \n        for row in range(rows_count):\n            for col in range(cols_count):\n                live_neighbors = 0\n                is_alive = board[row][col] == 1\n\n                for row_delta, col_delta in moves:\n                    new_row, new_col = row + row_delta, col + col_delta\n                    if not 0 <= new_row < rows_count or not 0 <= new_col < cols_count:\n                        continue\n                    if board[new_row][new_col] == 1:\n                        live_neighbors += 1\n\n                if (is_alive and (live_neighbors < 2 or live_neighbors > 3)) or (\n                    not is_alive and live_neighbors == 3\n                ):\n                    flip_cells.add((row, col))\n        \n        while flip_cells:\n            row, col = flip_cells.pop()\n            board[row][col] = 0 if board[row][col] == 1 else 1","title":"Game of Life","url":"/submissions/detail/1039615645/","lang_name":"Python3","time":"5 months","timestamp":1693760789,"status":10,"runtime":"44 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"1111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows_count, cols_count = len(board), len(board[0])
        moves = ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))
        flip_cells = set()

        for row in range(rows_count):
            for col in range(cols_count):
                live_neighbors = 0
                is_alive = board[row][col] == 1

                for row_delta, col_delta in moves:
                    new_row, new_col = row + row_delta, col + col_delta
                    if not 0 <= new_row < rows_count or not 0 <= new_col < cols_count:
                        continue
                    if board[new_row][new_col] == 1:
                        live_neighbors += 1

                if (is_alive and (live_neighbors < 2 or live_neighbors > 3)) or (
                    not is_alive and live_neighbors == 3
                ):
                    flip_cells.add((row, col))

        while flip_cells:
            row, col = flip_cells.pop()
            board[row][col] = 0 if board[row][col] == 1 else 1
