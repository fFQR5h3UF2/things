# Submission for Best Time to Buy and Sell Stock
# Submission url: https://leetcode.com/submissions/detail/993664784/


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
        smallest_price, biggest_price = prices[0], prices[-1]

        while right < length:
            current_profit = prices[right] - prices[left]

            if current_profit < 0:
                left += 1
                right += 1
                continue

            if current_profit > profit:
                profit = current_profit
                right += 1

        return profit
