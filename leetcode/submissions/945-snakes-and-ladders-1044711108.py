# Submission for Snakes and Ladders
# Submission url: https://leetcode.com/submissions/detail/1044711108/


class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        side_length = len(board)
        square_count = side_length**2

        @cache
        def get_square(square: int) -> int:
            quotient, remainder = divmod(square - 1, side_length)
            col = remainder if quotient % 2 == 0 else side_length - remainder - 1
            row = side_length - quotient - 1
            return board[row][col]

        @cache
        def dp(square: int) -> int:
            if square >= square_count:
                return 0
            target = get_square(square)
            if target == square_count:
                return 0
            if target != -1 and target < square:
                return -1
            elif target != -1:
                square = target

            min_move_count = -1
            for move in range(1, 7):
                move_count = 1 + dp(square + move)
                if move_count > 0 and (
                    min_move_count == -1 or move_count < min_move_count
                ):
                    min_move_count = move_count
            return min_move_count

        return dp(1)
