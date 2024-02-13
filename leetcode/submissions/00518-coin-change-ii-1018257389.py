# Submission title: Coin Change II
# Submission url  : https://leetcode.com/problems/coin-change-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/1018257389/
# Submission json : {"id":1018257389,"status_display":"Accepted","lang":"python3","question_id":518,"title_slug":"coin-change-ii","code":"class Solution:\n    def change(self, amount: int, coins: List[int]) -> int:\n        coins_count = len(coins)\n        memo = [[-1] * (amount + 1) for _ in range(coins_count)]\n        \n        def dp(i: int, amount: int) -> int:\n            if amount == 0:\n                return 1\n            if i == coins_count:\n                return 0\n            if memo[i][amount] != -1:\n                return memo[i][amount]\n\n            value = None\n\n            if coins[i] > amount:\n                value = dp(i + 1, amount)\n            else:\n                value = dp(i, amount - coins[i]) + dp(i + 1, amount)\n\n            memo[i][amount] = value\n            return value\n\n        return dp(0, amount)","title":"Coin Change II","url":"/submissions/detail/1018257389/","lang_name":"Python3","time":"5 months, 3 weeks","timestamp":1691741550,"status":10,"runtime":"331 ms","is_pending":"Not Pending","memory":"40.6 MB","compare_result":"1111111111111111111111111111","has_notes":true,"flag_type":1}


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

            value = None

            if coins[i] > amount:
                value = dp(i + 1, amount)
            else:
                value = dp(i, amount - coins[i]) + dp(i + 1, amount)

            memo[i][amount] = value
            return value

        return dp(0, amount)
