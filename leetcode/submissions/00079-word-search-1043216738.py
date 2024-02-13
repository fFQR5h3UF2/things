# Submission title: Word Search
# Submission url  : https://leetcode.com/problems/word-search/description/
# Submission url  : https://leetcode.com/submissions/detail/1043216738/
# Submission json : {"id":1043216738,"status_display":"Accepted","lang":"python3","question_id":79,"title_slug":"word-search","code":"class Solution:\n    def exist(self, board: List[List[str]], word: str) -> bool:\n        row_count, col_count = len(board), len(board[0])\n        word_length = len(word)\n        delta = ((0, 1), (0, -1), (1, 0), (-1, 0))\n\n        if word_length == 1:\n            return any(word in row for row in board)\n        if word_length > row_count * col_count:\n            return False\n\n        visited = set()\n\n        def backtrack(row: int, col: int, target: int) -> bool:\n            if target == word_length:\n                return True\n            if not 0 <= row < row_count or not 0 <= col < col_count or (\n                (row, col) in visited or board[row][col] != word[target]\n            ):\n                return False\n\n            visited.add((row, col))\n            answer = any(backtrack(row + delta_row, col + delta_col, target + 1)\n                         for delta_row, delta_col in delta)\n            visited.remove((row, col))\n            return answer\n\n        return any(backtrack(row, col, 0) \n                   for row in range(row_count) \n                   for col in range(col_count))","title":"Word Search","url":"/submissions/detail/1043216738/","lang_name":"Python3","time":"4 months, 4 weeks","timestamp":1694106543,"status":10,"runtime":"9244 ms","is_pending":"Not Pending","memory":"16.5 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_count, col_count = len(board), len(board[0])
        word_length = len(word)
        delta = ((0, 1), (0, -1), (1, 0), (-1, 0))

        if word_length == 1:
            return any(word in row for row in board)
        if word_length > row_count * col_count:
            return False

        visited = set()

        def backtrack(row: int, col: int, target: int) -> bool:
            if target == word_length:
                return True
            if (
                not 0 <= row < row_count
                or not 0 <= col < col_count
                or ((row, col) in visited or board[row][col] != word[target])
            ):
                return False

            visited.add((row, col))
            answer = any(
                backtrack(row + delta_row, col + delta_col, target + 1)
                for delta_row, delta_col in delta
            )
            visited.remove((row, col))
            return answer

        return any(
            backtrack(row, col, 0)
            for row in range(row_count)
            for col in range(col_count)
        )
