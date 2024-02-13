# Submission title: Out of Boundary Paths
# Submission url  : https://leetcode.com/problems/out-of-boundary-paths/description/
# Submission url  : https://leetcode.com/submissions/detail/1157205765/
# Submission json : {"id":1157205765,"status_display":"Accepted","lang":"python3","question_id":576,"title_slug":"out-of-boundary-paths","code":"class Solution:\n\n    def findPaths(self, m: int, n: int, N: int, x: int, y: int) -> int:\n\n        M = 1000000000 + 7\n\n        dp = [[0] * n for _ in range(m)]\n\n        dp[x][y] = 1\n\n        count = 0\n\n\n\n        for moves in range(1, N + 1):\n\n            temp = [[0] * n for _ in range(m)]\n\n\n\n            for i in range(m):\n\n                for j in range(n):\n\n                    if i == m - 1:\n\n                        count = (count + dp[i][j]) % M\n\n                    if j == n - 1:\n\n                        count = (count + dp[i][j]) % M\n\n                    if i == 0:\n\n                        count = (count + dp[i][j]) % M\n\n                    if j == 0:\n\n                        count = (count + dp[i][j]) % M\n\n                    temp[i][j] = (\n\n                        ((dp[i - 1][j] if i > 0 else 0) + (dp[i + 1][j] if i < m - 1 else 0)) % M +\n\n                        ((dp[i][j - 1] if j > 0 else 0) + (dp[i][j + 1] if j < n - 1 else 0)) % M\n\n                    ) % M\n\n\n\n            dp = temp\n\n\n\n        return count\n\n\n\n\n\n","title":"Out of Boundary Paths","url":"/submissions/detail/1157205765/","lang_name":"Python3","time":"1 week, 2 days","timestamp":1706256135,"status":10,"runtime":"107 ms","is_pending":"Not Pending","memory":"16.7 MB","compare_result":"1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:

    def findPaths(self, m: int, n: int, N: int, x: int, y: int) -> int:

        M = 1000000000 + 7

        dp = [[0] * n for _ in range(m)]

        dp[x][y] = 1

        count = 0

        for moves in range(1, N + 1):

            temp = [[0] * n for _ in range(m)]

            for i in range(m):

                for j in range(n):

                    if i == m - 1:

                        count = (count + dp[i][j]) % M

                    if j == n - 1:

                        count = (count + dp[i][j]) % M

                    if i == 0:

                        count = (count + dp[i][j]) % M

                    if j == 0:

                        count = (count + dp[i][j]) % M

                    temp[i][j] = (
                        (
                            (dp[i - 1][j] if i > 0 else 0)
                            + (dp[i + 1][j] if i < m - 1 else 0)
                        )
                        % M
                        + (
                            (dp[i][j - 1] if j > 0 else 0)
                            + (dp[i][j + 1] if j < n - 1 else 0)
                        )
                        % M
                    ) % M

            dp = temp

        return count
