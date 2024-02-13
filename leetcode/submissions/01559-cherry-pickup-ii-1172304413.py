# Submission title: Cherry Pickup II
# Submission url  : https://leetcode.com/problems/cherry-pickup-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1172304413/
# Submission json : {"id":1172304413,"status_display":"Accepted","lang":"python3","question_id":1559,"title_slug":"cherry-pickup-ii","code":"class Solution:\n    def cherryPickup(self, grid: List[List[int]]) -> int:\n        n = len(grid)\n        m = len(grid[0])\n\n        # Create 3D DP table with initial values of 0\n        dp = [[[0] * m for _ in range(m)] for _ in range(n)]\n\n        # Set the starting point value (top-left and top-right corner)\n        cherries = 0\n        dp[0][0][m - 1] = grid[0][0] + grid[0][m - 1]\n\n        # Iterate through each row from second onwards\n        for i in range(1, n):\n            # Iterate through each column for robot 1\n            for j in range(m):\n                # Iterate through each column for robot 2\n                for k in range(m):\n                    # Skip invalid states:\n                    # - Both robots in the same row (j > i)\n                    # - Robot 2 left of robot 1 (k < m - i - 1)\n                    # - Robot 1 further right than robot 2 (j > k)\n                    if j > i or k < m - i - 1 or j > k:\n                        continue\n                    # Base case: no moves possible, use previous state\n                    dp[i][j][k] = dp[i - 1][j][k]\n                    # Explore moves for robot 1:\n                    # - Up-diagonal with robot 2 at same position\n                    if j - 1 >= 0:\n                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k])\n                    # - Up-diagonal with robot 2 one step left/right\n                    if j - 1 >= 0 and k - 1 >= 0:\n                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k - 1])\n                    if j - 1 >= 0 and k + 1 < m:\n                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k + 1])\n                    # Explore moves for robot 2:\n                    # - Up-diagonal with robot 1 at same position\n                    if j + 1 < m:\n                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k])\n                    # - Up-diagonal with robot 1 one step left/right\n                    if j + 1 < m and k - 1 >= 0:\n                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k - 1])\n                    if j + 1 < m and k + 1 < m:\n                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k + 1])\n                    # Explore horizontal moves for both robots:\n                    # - Both robots move left\n                    if k - 1 >= 0:\n                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1])\n                    # - Both robots move right\n                    if k + 1 < m:\n                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k + 1])\n                    # Add cherries only if robots are in different positions\n                    if j != k:\n                        dp[i][j][k] += grid[i][j] + grid[i][k]\n                    else:\n                        dp[i][j][k] += grid[i][j]  # Only one robot picks if they land in the same cell\n                    # Update maximum cherries collected so far\n                    cherries = max(cherries, dp[i][j][k])\n\n        return cherries\n","title":"Cherry Pickup II","url":"/submissions/detail/1172304413/","lang_name":"Python3","time":"3 minutes","timestamp":1707657627,"status":10,"runtime":"498 ms","is_pending":"Not Pending","memory":"22.6 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        # Create 3D DP table with initial values of 0
        dp = [[[0] * m for _ in range(m)] for _ in range(n)]

        # Set the starting point value (top-left and top-right corner)
        cherries = 0
        dp[0][0][m - 1] = grid[0][0] + grid[0][m - 1]

        # Iterate through each row from second onwards
        for i in range(1, n):
            # Iterate through each column for robot 1
            for j in range(m):
                # Iterate through each column for robot 2
                for k in range(m):
                    # Skip invalid states:
                    # - Both robots in the same row (j > i)
                    # - Robot 2 left of robot 1 (k < m - i - 1)
                    # - Robot 1 further right than robot 2 (j > k)
                    if j > i or k < m - i - 1 or j > k:
                        continue
                    # Base case: no moves possible, use previous state
                    dp[i][j][k] = dp[i - 1][j][k]
                    # Explore moves for robot 1:
                    # - Up-diagonal with robot 2 at same position
                    if j - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k])
                    # - Up-diagonal with robot 2 one step left/right
                    if j - 1 >= 0 and k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k - 1])
                    if j - 1 >= 0 and k + 1 < m:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k + 1])
                    # Explore moves for robot 2:
                    # - Up-diagonal with robot 1 at same position
                    if j + 1 < m:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k])
                    # - Up-diagonal with robot 1 one step left/right
                    if j + 1 < m and k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k - 1])
                    if j + 1 < m and k + 1 < m:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j + 1][k + 1])
                    # Explore horizontal moves for both robots:
                    # - Both robots move left
                    if k - 1 >= 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k - 1])
                    # - Both robots move right
                    if k + 1 < m:
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k + 1])
                    # Add cherries only if robots are in different positions
                    if j != k:
                        dp[i][j][k] += grid[i][j] + grid[i][k]
                    else:
                        dp[i][j][k] += grid[i][
                            j
                        ]  # Only one robot picks if they land in the same cell
                    # Update maximum cherries collected so far
                    cherries = max(cherries, dp[i][j][k])

        return cherries
