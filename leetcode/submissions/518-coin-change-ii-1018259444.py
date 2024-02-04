# Submission for Coin Change II
# Submission url: https://leetcode.com/submissions/detail/1018259444/


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins_count = len(coins)
        memo = [[-1] * (amount + 1) for _ in range(coins_count)]

        def dp(i: int, amount: int) -> int:
            if amount == 0:
                return 1
            if i == coins_count:
                return 0
            if memo[i][amount] != -1:
                return memo[i][amount]

            diff = amount - coins[i]
            value = dp(i + 1, amount) + dp(i, diff) if diff >= 0 else 0
            memo[i][amount] = value
            return value

        return dp(0, amount)
