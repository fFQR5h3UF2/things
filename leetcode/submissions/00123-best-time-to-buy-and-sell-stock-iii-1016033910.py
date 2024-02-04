# Submission title: for Best Time to Buy and Sell Stock III
# Submission url  : https://leetcode.com/submissions/detail/1016033910/
# Submission json : {"id": 1016033910, "status_display": "Accepted", "lang": "python3", "question_id": 123, "title_slug": "best-time-to-buy-and-sell-stock-iii", "code": "class Solution:\n\tdef maxProfit(self, prices: List[int]) -> int:\n\t\t\t\t\n\t\t'''\n\t\tdp_2_hold: max profit with 2 transactions, and in hold state\n\t\tdp_2_not_hold: max profit with 2 transactions, and not in hold state\n\t\t\n\t\tdp_1_hold: max profit with 1 transaction, and in hold state\n\t\tdp_1_not_hold: max profit with 1 transaction, and not in hold state\n\t\t\n\t\tNote: it is impossible to have stock in hand and sell on first day, therefore -infinity is set as initial profit value for hold state\n\t\t'''\n\t\t\n\t\tdp_2_hold, dp_2_not_hold = -float('inf'), 0\n\t\tdp_1_hold, dp_1_not_hold = -float('inf'), 0\n\t\t\n\t\tfor stock_price in prices:\n\t\t\t\t\n\t\t\t# either keep being in not-hold state, or sell with stock price today\n\t\t\tdp_2_not_hold = max( dp_2_not_hold, dp_2_hold + stock_price )\n\t\n\t\t\t# either keep being in hold state, or just buy with stock price today ( add one more transaction )\n\t\t\tdp_2_hold = max( dp_2_hold, dp_1_not_hold - stock_price )\n\t\t\t\t\n\t\t\t# either keep being in not-hold state, or sell with stock price today\n\t\t\tdp_1_not_hold = max( dp_1_not_hold, dp_1_hold + stock_price )\n\t\n\t\t\t# either keep being in hold state, or just buy with stock price today ( add one more transaction )\n\t\t\tdp_1_hold = max( dp_1_hold, 0 - stock_price )\n\t\t\t\t\n\t\treturn dp_2_not_hold", "title": "Best Time to Buy and Sell Stock III", "url": "/submissions/detail/1016033910/", "lang_name": "Python3", "time": "5\u00a0months, 4\u00a0weeks", "timestamp": 1691527250, "status": 10, "runtime": "859 ms", "is_pending": "Not Pending", "memory": "30.5 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        dp_2_hold: max profit with 2 transactions, and in hold state
        dp_2_not_hold: max profit with 2 transactions, and not in hold state

        dp_1_hold: max profit with 1 transaction, and in hold state
        dp_1_not_hold: max profit with 1 transaction, and not in hold state

        Note: it is impossible to have stock in hand and sell on first day, therefore -infinity is set as initial profit value for hold state
        """

        dp_2_hold, dp_2_not_hold = -float("inf"), 0
        dp_1_hold, dp_1_not_hold = -float("inf"), 0

        for stock_price in prices:

            # either keep being in not-hold state, or sell with stock price today
            dp_2_not_hold = max(dp_2_not_hold, dp_2_hold + stock_price)

            # either keep being in hold state, or just buy with stock price today ( add one more transaction )
            dp_2_hold = max(dp_2_hold, dp_1_not_hold - stock_price)

            # either keep being in not-hold state, or sell with stock price today
            dp_1_not_hold = max(dp_1_not_hold, dp_1_hold + stock_price)

            # either keep being in hold state, or just buy with stock price today ( add one more transaction )
            dp_1_hold = max(dp_1_hold, 0 - stock_price)

        return dp_2_not_hold
