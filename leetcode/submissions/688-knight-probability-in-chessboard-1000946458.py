# Submission for Knight Probability in Chessboard
# Submission url: https://leetcode.com/submissions/detail/1000946458/


class Solution:
    # y x x
    # x x x
    # x x x 2 / 8 -> 4 / 16
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if not k:
            return 1

        if n < 3:
            return 0

        probability = float(1)
        moves = [[row, column]]
        available_moves = [
            [2, 1],
            [1, 2],
            [-2, 1],
            [-1, 2],
            [2, -1],
            [1, -2],
            [-2, -1],
            [-1, -2],
        ]

        while k:
            old_moves_count = len(moves)
            for i in range(old_moves_count):
                row, column = moves[i]
                old_move_replaced = False

                for row_add, column_add in available_moves:
                    new_row = row_add + row
                    new_column = column_add + column

                    if (
                        new_row < 0
                        or new_row >= n
                        or (new_column < 0 or new_column >= n)
                    ):
                        continue

                    if old_move_replaced:
                        moves.append([new_row, new_column])
                        continue

                    moves[i][0], moves[i][1] = new_row, new_column
                    old_move_replaced = True

            probability *= len(moves) / (old_moves_count * 8)
            k -= 1

        return probability
