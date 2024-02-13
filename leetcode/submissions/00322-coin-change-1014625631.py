# Submission title: Coin Change
# Submission url  : https://leetcode.com/problems/coin-change/description/
# Submission url  : https://leetcode.com/submissions/detail/1014625631/
# Submission json : {"id":1014625631,"status_display":"Accepted","lang":"python3","question_id":322,"title_slug":"coin-change","code":"class Solution:\n    def coinChange(self, coins: List[int], amount: int) -> int:\n        if amount == 0:\n            return 0\n        \n        @cache\n        def dp(coins_value: int) -> int:\n            if coins_value == amount:\n                return 0\n            \n            if coins_value > amount:\n                return -1\n            \n            min_coins_count = -1\n\n            for coin in coins:\n                new_count = 1 + dp(coin + coins_value)\n                if new_count == 0:\n                    continue\n                \n                if min_coins_count == -1 or new_count < min_coins_count:\n                    min_coins_count = new_count\n            \n            return min_coins_count\n\n        return dp(0)\n","title":"Coin Change","url":"/submissions/detail/1014625631/","lang_name":"Python3","time":"6 months","timestamp":1691407626,"status":10,"runtime":"704 ms","is_pending":"Not Pending","memory":"37.5 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":true,"flag_type":1}


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        @cache
        def dp(coins_value: int) -> int:
            if coins_value == amount:
                return 0

            if coins_value > amount:
                return -1

            min_coins_count = -1

            for coin in coins:
                new_count = 1 + dp(coin + coins_value)
                if new_count == 0:
                    continue

                if min_coins_count == -1 or new_count < min_coins_count:
                    min_coins_count = new_count

            return min_coins_count

        return dp(0)
