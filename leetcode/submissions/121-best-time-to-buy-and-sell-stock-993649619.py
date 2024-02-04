# Submission for Best Time to Buy and Sell Stock
# Submission url: https://leetcode.com/submissions/detail/993649619/


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

        profit, last_day = 0, length - 1
        for i, price_buy in enumerate(prices[:last_day]):
            price_sell = sorted(prices[i + 1 :])[-1]
            new_profit = price_sell - price_buy
            if new_profit > profit:
                profit = new_profit

        return profit
