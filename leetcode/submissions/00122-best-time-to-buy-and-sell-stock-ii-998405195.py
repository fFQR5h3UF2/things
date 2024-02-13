# Submission title: Best Time to Buy and Sell Stock II
# Submission url  : https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/
# Submission url  : https://leetcode.com/submissions/detail/998405195/
# Submission json : {"id":998405195,"status_display":"Accepted","lang":"python3","question_id":122,"title_slug":"best-time-to-buy-and-sell-stock-ii","code":"class Solution:\n    def maxProfit(self, prices: List[int]) -> int:\n\t\t# It is impossible to sell stock on first day, set -infinity as initial value for cur_hold\n        cur_hold, cur_not_hold = -float('inf'), 0\n        \n        for stock_price in prices:\n            prev_hold, prev_not_hold = cur_hold, cur_not_hold\n\t\t\t# either keep hold, or buy in stock today at stock price\n            cur_hold = max(prev_hold, prev_not_hold - stock_price)\n\t\t\t\n\t\t\t# either keep not-hold, or sell out stock today at stock price\n            cur_not_hold = max(prev_not_hold, \n                               prev_hold + stock_price)\n            \n        # maximum profit must be in not-hold state\n        return cur_not_hold","title":"Best Time to Buy and Sell Stock II","url":"/submissions/detail/998405195/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1689766552,"status":10,"runtime":"75 ms","is_pending":"Not Pending","memory":"17.7 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # It is impossible to sell stock on first day, set -infinity as initial value for cur_hold
        cur_hold, cur_not_hold = -float("inf"), 0

        for stock_price in prices:
            prev_hold, prev_not_hold = cur_hold, cur_not_hold
            # either keep hold, or buy in stock today at stock price
            cur_hold = max(prev_hold, prev_not_hold - stock_price)

            # either keep not-hold, or sell out stock today at stock price
            cur_not_hold = max(prev_not_hold, prev_hold + stock_price)

        # maximum profit must be in not-hold state
        return cur_not_hold
