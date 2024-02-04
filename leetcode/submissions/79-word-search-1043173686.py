# Submission for Word Search
# Submission url: https://leetcode.com/submissions/detail/1043173686/


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row_count, col_count = len(board), len(board[0])
        word_length = len(word)
        visited = set()
        delta = ((0, 1), (0, -1), (1, 0), (-1, 0))

        if word_length == 1:
            return any(word in row for row in board)

        def backtrack(row: int, col: int, target: int) -> bool:
            if (
                (row, col) in visited
                or not 0 <= row < row_count
                or not 0 <= col < col_count
            ):
                return False

            is_valid = board[row][col] == word[target]
            if target == word_length - 1:
                return is_valid

            visited.add((row, col))
            for delta_row, delta_col in delta:
                new_row, new_col = row + delta_row, col + delta_col
                try_next = is_valid and backtrack(new_row, new_col, target + 1)
                try_start = backtrack(new_row, new_col, 0)
                if try_next or try_start:
                    return True

            visited.remove((row, col))
            return False

        return backtrack(0, 0, 0)
