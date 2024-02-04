# Submission title: for Knight Probability in Chessboard
# Submission url  : https://leetcode.com/submissions/detail/1001107966/
# Submission json : {"id": 1001107966, "status_display": "Accepted", "lang": "python3", "question_id": 688, "title_slug": "knight-probability-in-chessboard", "code": "class Solution:\n    # y x x\n    # x x x\n    # x x x: (2 / 8) * (4 / 16) = 0.0625\n    #        (1/8, 1/8), (2/8, 2/8)\n    # \n    # x x x\n    # x y x\n    # x x x: 0\n    def __init__(self):\n        self.available_moves = (\n            (2, 1), (1, 2), (-2, 1), (-1, 2), (2, -1), (1, -2), \n            (-2, -1), (-1, -2)\n        )\n    \n\n    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:\n        if k < 1:\n            return 1\n        \n        if n < 3:\n            return 0\n\n        return self.calculate(row, column, n, k)\n    \n    @cache\n    def calculate(self, row: int, column: int, size: int, \n                       moves_left: int) -> float:\n       \n        if moves_left < 1:\n            return 1\n\n        probability = 0\n\n        for row_add, column_add in self.available_moves:\n            new_row = row_add + row\n            new_column = column_add + column\n\n            if new_row < 0 or new_row >= size or (\n                new_column < 0 or new_column >= size\n            ):\n                continue\n\n            probability += self.calculate(\n                new_row, new_column, size, moves_left - 1\n            ) / 8\n\n        return probability", "title": "Knight Probability in Chessboard", "url": "/submissions/detail/1001107966/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690042140, "status": 10, "runtime": "268 ms", "is_pending": "Not Pending", "memory": "27.8 MB", "compare_result": "1111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    # y x x
    # x x x
    # x x x: (2 / 8) * (4 / 16) = 0.0625
    #        (1/8, 1/8), (2/8, 2/8)
    #
    # x x x
    # x y x
    # x x x: 0
    def __init__(self):
        self.available_moves = (
            (2, 1),
            (1, 2),
            (-2, 1),
            (-1, 2),
            (2, -1),
            (1, -2),
            (-2, -1),
            (-1, -2),
        )

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        if k < 1:
            return 1

        if n < 3:
            return 0

        return self.calculate(row, column, n, k)

    @cache
    def calculate(self, row: int, column: int, size: int, moves_left: int) -> float:

        if moves_left < 1:
            return 1

        probability = 0

        for row_add, column_add in self.available_moves:
            new_row = row_add + row
            new_column = column_add + column

            if new_row < 0 or new_row >= size or (new_column < 0 or new_column >= size):
                continue

            probability += self.calculate(new_row, new_column, size, moves_left - 1) / 8

        return probability
