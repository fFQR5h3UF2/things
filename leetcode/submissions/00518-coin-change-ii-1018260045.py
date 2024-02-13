# Submission title: Coin Change II
# Submission url  : https://leetcode.com/problems/coin-change-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1018260045/
# Submission json : {"id":1018260045,"status_display":"Accepted","lang":"python3","question_id":518,"title_slug":"coin-change-ii","code":"class Solution:\n    def change(self, amount: int, coins: List[int]) -> int:\n        n = len(coins)\n        dp = [[0] * (amount + 1) for _ in range(n + 1)]\n        for i in range(n):\n            dp[i][0] = 1\n\n        for i in range(n - 1, -1, -1):\n            for j in range(1, amount + 1):\n                if coins[i] > j:\n                    dp[i][j] = dp[i + 1][j]\n                else:\n                    dp[i][j] = dp[i + 1][j] + dp[i][j - coins[i]]\n\n        return dp[0][amount]","title":"Coin Change II","url":"/submissions/detail/1018260045/","lang_name":"Python3","time":"5 months, 3 weeks","timestamp":1691741854,"status":10,"runtime":"270 ms","is_pending":"Not Pending","memory":"25.9 MB","compare_result":"1111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        dp = [[0] * (amount + 1) for _ in range(n + 1)]
        for i in range(n):
            dp[i][0] = 1

        for i in range(n - 1, -1, -1):
            for j in range(1, amount + 1):
                if coins[i] > j:
                    dp[i][j] = dp[i + 1][j]
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - coins[i]]

        return dp[0][amount]
