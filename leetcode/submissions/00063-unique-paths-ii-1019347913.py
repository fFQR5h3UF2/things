# Submission title: Unique Paths II
# Submission url  : https://leetcode.com/problems/unique-paths-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1019347913/
# Submission json : {"id":1019347913,"status_display":"Accepted","lang":"python3","question_id":63,"title_slug":"unique-paths-ii","code":"class Solution:\n    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:\n        row_count = len(obstacleGrid)\n        column_count = len(obstacleGrid[0])\n        \n        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:\n            return 0\n\n        dp = [[0] * column_count for _ in range(row_count)]\n        dp[0][0] = 1\n\n        for column in range(1, column_count):\n            if obstacleGrid[0][column] == 1:\n                break\n\n            dp[0][column] = dp[0][column-1]\n\n        for row in range(1, row_count):\n            if obstacleGrid[row][0] == 0:\n                dp[row][0] = dp[row-1][0]\n\n            for column in range(1, column_count):\n                if obstacleGrid[row][column] == 1:\n                    continue\n                \n                dp[row][column] = dp[row-1][column] + dp[row][column-1]\n                     \n        return dp[-1][-1]","title":"Unique Paths II","url":"/submissions/detail/1019347913/","lang_name":"Python3","time":"5 months, 3 weeks","timestamp":1691851840,"status":10,"runtime":"44 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"11111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        row_count = len(obstacleGrid)
        column_count = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0

        dp = [[0] * column_count for _ in range(row_count)]
        dp[0][0] = 1

        for column in range(1, column_count):
            if obstacleGrid[0][column] == 1:
                break

            dp[0][column] = dp[0][column - 1]

        for row in range(1, row_count):
            if obstacleGrid[row][0] == 0:
                dp[row][0] = dp[row - 1][0]

            for column in range(1, column_count):
                if obstacleGrid[row][column] == 1:
                    continue

                dp[row][column] = dp[row - 1][column] + dp[row][column - 1]

        return dp[-1][-1]
