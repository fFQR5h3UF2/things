# Submission title: for Best Time to Buy and Sell Stock IV
# Submission url  : https://leetcode.com/submissions/detail/1016554386/
# Submission json : {"id": 1016554386, "status_display": "Accepted", "lang": "python3", "question_id": 188, "title_slug": "best-time-to-buy-and-sell-stock-iv", "code": "class Solution:\n    def maxProfit(self, k: int, prices: List[int]) -> int:\n        # no transaction, no profit\n        if k == 0: return 0\n        # dp[k][0] = min cost you need to spend at most k transactions\n        # dp[k][1] = max profit you can achieve at most k transactions\n        dp = [[1000, 0] for _ in range(k + 1)]\n        for price in prices:\n            for i in range(1, k + 1):\n                # price - dp[i - 1][1] is how much you need to spend\n                # i.e use the profit you earned from previous transaction to buy the stock\n                # we want to minimize it\n                dp[i][0] = min(dp[i][0], price - dp[i - 1][1])\n                # price - dp[i][0] is how much you can achieve from previous min cost\n                # we want to maximize it\n                dp[i][1] = max(dp[i][1], price - dp[i][0])\n        # return max profit at most k transactions\n\t\t# or you can write `return dp[-1][1]`\n        return dp[k][1]", "title": "Best Time to Buy and Sell Stock IV", "url": "/submissions/detail/1016554386/", "lang_name": "Python3", "time": "5\u00a0months, 4\u00a0weeks", "timestamp": 1691583208, "status": 10, "runtime": "99 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # no transaction, no profit
        if k == 0:
            return 0
        # dp[k][0] = min cost you need to spend at most k transactions
        # dp[k][1] = max profit you can achieve at most k transactions
        dp = [[1000, 0] for _ in range(k + 1)]
        for price in prices:
            for i in range(1, k + 1):
                # price - dp[i - 1][1] is how much you need to spend
                # i.e use the profit you earned from previous transaction to buy the stock
                # we want to minimize it
                dp[i][0] = min(dp[i][0], price - dp[i - 1][1])
                # price - dp[i][0] is how much you can achieve from previous min cost
                # we want to maximize it
                dp[i][1] = max(dp[i][1], price - dp[i][0])
        # return max profit at most k transactions
        # or you can write `return dp[-1][1]`
        return dp[k][1]
