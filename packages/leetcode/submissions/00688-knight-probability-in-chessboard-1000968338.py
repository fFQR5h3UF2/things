# Submission title: for Knight Probability in Chessboard
# Submission url  : https://leetcode.com/submissions/detail/1000968338/
# Submission json : {"id": 1000968338, "status_display": "Accepted", "lang": "python3", "question_id": 688, "title_slug": "knight-probability-in-chessboard", "code": "class Solution:\n    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:\n        # Define possible directions for the knight's moves\n        directions = [(1, 2), (1, -2), (-1, 2), (-1, -2),\n                      (2, 1), (2, -1), (-2, 1), (-2, -1)]\n\n        # Initialize the dynamic programming table\n        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]\n        dp[0][row][column] = 1\n\n        # Iterate over the number of moves\n        for moves in range(1, k + 1):\n            # Iterate over the cells on the chessboard\n            for i in range(n):\n                for j in range(n):\n                    # Iterate over possible directions\n                    for direction in directions:\n                        prev_i, prev_j = i - direction[0], j - direction[1]\n                        # Check if the previous cell is within the chessboard\n                        if 0 <= prev_i < n and 0 <= prev_j < n:\n                            # Add the previous probability\n                            dp[moves][i][j] += dp[moves - 1][prev_i][prev_j]\n                    # Divide by 8\n                    dp[moves][i][j] /= 8\n\n        # Calculate total probability by summing probabilities for all cells\n        total_probability = sum(\n            dp[k][i][j]\n            for i in range(n)\n            for j in range(n)\n        )\n        return total_probability", "title": "Knight Probability in Chessboard", "url": "/submissions/detail/1000968338/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690036594, "status": 10, "runtime": "400 ms", "is_pending": "Not Pending", "memory": "19.1 MB", "compare_result": "1111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # Define possible directions for the knight's moves
        directions = [
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
        ]

        # Initialize the dynamic programming table
        dp = [[[0] * n for _ in range(n)] for _ in range(k + 1)]
        dp[0][row][column] = 1

        # Iterate over the number of moves
        for moves in range(1, k + 1):
            # Iterate over the cells on the chessboard
            for i in range(n):
                for j in range(n):
                    # Iterate over possible directions
                    for direction in directions:
                        prev_i, prev_j = i - direction[0], j - direction[1]
                        # Check if the previous cell is within the chessboard
                        if 0 <= prev_i < n and 0 <= prev_j < n:
                            # Add the previous probability
                            dp[moves][i][j] += dp[moves - 1][prev_i][prev_j]
                    # Divide by 8
                    dp[moves][i][j] /= 8

        # Calculate total probability by summing probabilities for all cells
        total_probability = sum(dp[k][i][j] for i in range(n) for j in range(n))
        return total_probability
