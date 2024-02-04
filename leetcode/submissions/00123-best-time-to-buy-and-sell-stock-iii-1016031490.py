# Submission title: for Best Time to Buy and Sell Stock III
# Submission url  : https://leetcode.com/submissions/detail/1016031490/
# Submission json : {"id": 1016031490, "status_display": "Accepted", "lang": "python3", "question_id": 123, "title_slug": "best-time-to-buy-and-sell-stock-iii", "code": "class Solution:\n    def maxProfit(self, prices: List[int]) -> int:\n        if not prices:\n            return 0\n\n        # initialize variables for first buy, first sell, second buy, and second sell\n        buy1, buy2 = float('inf'), float('inf')\n        sell1, sell2 = 0, 0\n\n        # iterate over prices to update buy and sell values\n        for price in prices:\n            # update first buy and sell values\n            buy1 = min(buy1, price)\n            sell1 = max(sell1, price - buy1)\n            # update second buy and sell values\n            buy2 = min(buy2, price - sell1)\n            sell2 = max(sell2, price - buy2)\n\n        return sell2\n", "title": "Best Time to Buy and Sell Stock III", "url": "/submissions/detail/1016031490/", "lang_name": "Python3", "time": "5\u00a0months, 4\u00a0weeks", "timestamp": 1691527008, "status": 10, "runtime": "845 ms", "is_pending": "Not Pending", "memory": "30.6 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        # initialize variables for first buy, first sell, second buy, and second sell
        buy1, buy2 = float("inf"), float("inf")
        sell1, sell2 = 0, 0

        # iterate over prices to update buy and sell values
        for price in prices:
            # update first buy and sell values
            buy1 = min(buy1, price)
            sell1 = max(sell1, price - buy1)
            # update second buy and sell values
            buy2 = min(buy2, price - sell1)
            sell2 = max(sell2, price - buy2)

        return sell2
