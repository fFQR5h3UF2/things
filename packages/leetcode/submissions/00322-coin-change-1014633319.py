# Submission title: for Coin Change
# Submission url  : https://leetcode.com/submissions/detail/1014633319/
# Submission json : {"id": 1014633319, "status_display": "Accepted", "lang": "python3", "question_id": 322, "title_slug": "coin-change", "code": "class Solution:\n    def coinChange(self, coins: List[int], amount: int) -> int:\n        dp = [amount + 1] * (amount + 1)\n        dp[0] = 0\n\n        for current_amount in range(1, amount + 1):\n            for coin in coins:\n                diff = current_amount - coin\n                if diff < 0:\n                    continue\n                \n                dp[current_amount] = min(dp[current_amount], dp[diff] + 1)\n\n        return dp[-1] if dp[-1] != amount + 1 else -1\n", "title": "Coin Change", "url": "/submissions/detail/1014633319/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1691408344, "status": 10, "runtime": "918 ms", "is_pending": "Not Pending", "memory": "16.6 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": true, "flag_type": 1}


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0

        for current_amount in range(1, amount + 1):
            for coin in coins:
                diff = current_amount - coin
                if diff < 0:
                    continue

                dp[current_amount] = min(dp[current_amount], dp[diff] + 1)

        return dp[-1] if dp[-1] != amount + 1 else -1
