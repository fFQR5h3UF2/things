# Submission title: Word Search
# Submission url  : https://leetcode.com/problems/word-search/description/
# Submission url  : https://leetcode.com/submissions/detail/1043205644/
# Submission json : {"id":1043205644,"status_display":"Accepted","lang":"python3","question_id":79,"title_slug":"word-search","code":"class Solution:\n    def exist(self, board: List[List[str]], word: str) -> bool:\n        row_count, col_count = len(board), len(board[0])\n        word_length = len(word)\n        delta = ((0, 1), (0, -1), (1, 0), (-1, 0))\n\n        if word_length == 1:\n            return any(word in row for row in board)\n\n        def backtrack(row: int, col: int, visited: Set, target: int) -> bool:\n            if (row, col) in visited or not 0 <= row < row_count or not 0 <= col < col_count:\n                return False\n\n            if board[row][col] != word[target]:\n                return False\n            \n            if target == word_length - 1:\n                return True\n\n            visited.add((row, col))\n            if any(backtrack(row + delta_row, col + delta_col, visited, target + 1)\n                   for delta_row, delta_col in delta):\n                return True\n            visited.remove((row, col))\n            return False\n        \n        for row in range(row_count):\n            for col in range(col_count):\n                if backtrack(row, col, set(), 0):\n                    return True\n        \n        return False","title":"Word Search","url":"/submissions/detail/1043205644/","lang_name":"Python3","time":"4 months, 4 weeks","timestamp":1694105731,"status":10,"runtime":"9148 ms","is_pending":"Not Pending","memory":"16.5 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_count, col_count = len(board), len(board[0])
        word_length = len(word)
        delta = ((0, 1), (0, -1), (1, 0), (-1, 0))

        if word_length == 1:
            return any(word in row for row in board)

        def backtrack(row: int, col: int, visited: Set, target: int) -> bool:
            if (
                (row, col) in visited
                or not 0 <= row < row_count
                or not 0 <= col < col_count
            ):
                return False

            if board[row][col] != word[target]:
                return False

            if target == word_length - 1:
                return True

            visited.add((row, col))
            if any(
                backtrack(row + delta_row, col + delta_col, visited, target + 1)
                for delta_row, delta_col in delta
            ):
                return True
            visited.remove((row, col))
            return False

        for row in range(row_count):
            for col in range(col_count):
                if backtrack(row, col, set(), 0):
                    return True

        return False
