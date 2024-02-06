# Submission title: for Best Time to Buy and Sell Stock
# Submission url  : https://leetcode.com/submissions/detail/993666950/
# Submission json : {"id": 993666950, "status_display": "Accepted", "lang": "python3", "question_id": 121, "title_slug": "best-time-to-buy-and-sell-stock", "code": "class Solution:\n    # Input: prices = [7,1,5,3,6,4]\n    # Output: 5\n    # Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.\n    # Note that buying on day 2 and selling on day 1 is not allowed because you must buy \n    # before you sell.\n    def maxProfit(self, prices: List[int]) -> int:\n        length = len(prices)\n        if length < 2:\n            return 0\n\n        left, right, profit = 0, 1, 0\n        while right < length:\n            current_profit = prices[right] - prices[left]\n            if current_profit > 0:\n                profit = max(current_profit, profit)\n            else:\n                left = right\n            right += 1\n\n        return profit", "title": "Best Time to Buy and Sell Stock", "url": "/submissions/detail/993666950/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689268784, "status": 10, "runtime": "1009 ms", "is_pending": "Not Pending", "memory": "27.5 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    # Input: prices = [7,1,5,3,6,4]
    # Output: 5
    # Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    # Note that buying on day 2 and selling on day 1 is not allowed because you must buy
    # before you sell.
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length < 2:
            return 0

        left, right, profit = 0, 1, 0
        while right < length:
            current_profit = prices[right] - prices[left]
            if current_profit > 0:
                profit = max(current_profit, profit)
            else:
                left = right
            right += 1

        return profit
