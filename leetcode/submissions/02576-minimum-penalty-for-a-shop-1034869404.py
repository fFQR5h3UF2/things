# Submission title: Minimum Penalty for a Shop
# Submission url  : https://leetcode.com/problems/minimum-penalty-for-a-shop/description/
# Submission url  : https://leetcode.com/submissions/detail/1034869404/
# Submission json : {"id":1034869404,"status_display":"Accepted","lang":"python3","question_id":2576,"title_slug":"minimum-penalty-for-a-shop","code":"class Solution:\n    def bestClosingTime(self, customers: str) -> int:\n        # Start with closing at hour 0, the penalty equals all 'Y' in closed hours.\n        cur_penalty = min_penalty = customers.count(\"Y\")\n        earliest_hour = 0\n        \n        for hour, customer in enumerate(customers):\n            # If status in hour i is 'Y', moving it to open hours decrement\n            # penalty by 1. Otherwise, moving 'N' to open hours increment\n            # penatly by 1.\n            cur_penalty += 1 if customer == \"N\" else -1\n\n            # Update earliest_hour if a smaller penatly is encountered\n            if cur_penalty < min_penalty:\n                earliest_hour = hour + 1\n                min_penalty = cur_penalty\n                \n        return earliest_hour","title":"Minimum Penalty for a Shop","url":"/submissions/detail/1034869404/","lang_name":"Python3","time":"5 months, 1 week","timestamp":1693299053,"status":10,"runtime":"101 ms","is_pending":"Not Pending","memory":"17.4 MB","compare_result":"111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        # Start with closing at hour 0, the penalty equals all 'Y' in closed hours.
        cur_penalty = min_penalty = customers.count("Y")
        earliest_hour = 0

        for hour, customer in enumerate(customers):
            # If status in hour i is 'Y', moving it to open hours decrement
            # penalty by 1. Otherwise, moving 'N' to open hours increment
            # penatly by 1.
            cur_penalty += 1 if customer == "N" else -1

            # Update earliest_hour if a smaller penatly is encountered
            if cur_penalty < min_penalty:
                earliest_hour = hour + 1
                min_penalty = cur_penalty

        return earliest_hour
