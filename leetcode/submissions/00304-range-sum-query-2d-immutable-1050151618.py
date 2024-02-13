# Submission title: Range Sum Query 2D - Immutable
# Submission url  : https://leetcode.com/problems/range-sum-query-2d-immutable/description/
# Submission url  : https://leetcode.com/submissions/detail/1050151618/
# Submission json : {"id":1050151618,"status_display":"Accepted","lang":"python3","question_id":304,"title_slug":"range-sum-query-2d-immutable","code":"class NumMatrix:\n\n    def __init__(self, matrix: List[List[int]]):\n        self.dp=[[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]\n        \n\t\t# calculate prefix sum\n        for r in range(len(self.dp)-1):\n            for c in range(len(self.dp[0])-1):\n                self.dp[r+1][c+1]=matrix[r][c] + self.dp[r][c+1] + self.dp[r+1][c] - self.dp[r][c]\n        \n    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:\n        return self.dp[row2+1][col2+1] - self.dp[row1][col2+1] - self.dp[row2+1][col1] + self.dp[row1][col1]\n                ","title":"Range Sum Query 2D - Immutable","url":"/submissions/detail/1050151618/","lang_name":"Python3","time":"4 months, 3 weeks","timestamp":1694786879,"status":10,"runtime":"1162 ms","is_pending":"Not Pending","memory":"26.9 MB","compare_result":"1111111111111111111111","has_notes":false,"flag_type":1}


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.dp = [[0] * (len(matrix[0]) + 1) for _ in range(len(matrix) + 1)]

        # calculate prefix sum
        for r in range(len(self.dp) - 1):
            for c in range(len(self.dp[0]) - 1):
                self.dp[r + 1][c + 1] = (
                    matrix[r][c] + self.dp[r][c + 1] + self.dp[r + 1][c] - self.dp[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.dp[row2 + 1][col2 + 1]
            - self.dp[row1][col2 + 1]
            - self.dp[row2 + 1][col1]
            + self.dp[row1][col1]
        )
