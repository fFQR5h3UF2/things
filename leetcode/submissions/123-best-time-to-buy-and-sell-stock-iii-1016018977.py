# Submission for Best Time to Buy and Sell Stock III
# Submission url: https://leetcode.com/submissions/detail/1016018977/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        days_count = len(prices)

        @cache
        def dp(bought_day: int, transactions: int) -> int:
            if bought_day == days_count or transactions == 0:
                return 0

            max_profit = 0
            bought_price = prices[bought_day]

            for day in range(bought_day + 1, days_count):
                profit = prices[day] - bought_price
                max_profit = max(
                    max_profit,
                    (profit + dp(day + 1, transactions - 1)) if profit > 0 else 0,
                    dp(day, transactions),
                )

            return max_profit

        return dp(0, 2)
