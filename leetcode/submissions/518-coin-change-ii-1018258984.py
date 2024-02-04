# Submission for Coin Change II
# Submission url: https://leetcode.com/submissions/detail/1018258984/


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins_count = len(coins)

        @cache
        def dp(i: int, amount: int) -> int:
            if amount == 0:
                return 1
            if i == coins_count:
                return 0

            diff = amount - coins[i]
            return dp(i + 1, amount) + dp(i, diff) if diff >= 0 else 0

        return dp(0, amount)
