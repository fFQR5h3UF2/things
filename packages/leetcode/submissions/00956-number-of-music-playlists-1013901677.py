# Submission title: for Number of Music Playlists
# Submission url  : https://leetcode.com/submissions/detail/1013901677/
# Submission json : {"id": 1013901677, "status_display": "Accepted", "lang": "python3", "question_id": 956, "title_slug": "number-of-music-playlists", "code": "class Solution:\n    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:\n        MOD = 10**9 + 7\n\n        # Initialize the DP table\n        dp = [[0 for _ in range(n + 1)] for _ in range(goal + 1)]\n        dp[0][0] = 1\n\n        for i in range(1, goal + 1):\n            for j in range(1, min(i, n) + 1):\n                # The i-th song is a new song\n                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % MOD\n                # The i-th song is a song we have played before\n                if j > k:\n                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD\n\n        return dp[goal][n]", "title": "Number of Music Playlists", "url": "/submissions/detail/1013901677/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1691332676, "status": 10, "runtime": "66 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def numMusicPlaylists(self, n: int, goal: int, k: int) -> int:
        MOD = 10**9 + 7

        # Initialize the DP table
        dp = [[0 for _ in range(n + 1)] for _ in range(goal + 1)]
        dp[0][0] = 1

        for i in range(1, goal + 1):
            for j in range(1, min(i, n) + 1):
                # The i-th song is a new song
                dp[i][j] = dp[i - 1][j - 1] * (n - j + 1) % MOD
                # The i-th song is a song we have played before
                if j > k:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j] * (j - k)) % MOD

        return dp[goal][n]
