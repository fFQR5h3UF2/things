# Submission title: for Richest Customer Wealth
# Submission url  : https://leetcode.com/submissions/detail/1000089391/
# Submission json : {"id": 1000089391, "status_display": "Accepted", "lang": "python3", "question_id": 1791, "title_slug": "richest-customer-wealth", "code": "class Solution:\n    def maximumWealth(self, accounts: List[List[int]]) -> int:\n        max_wealth = 0\n        for i in range(len(accounts)):\n            wealth = 0\n            for j in range(len(accounts[i])):\n                wealth += accounts[i][j]\n            \n            if wealth > max_wealth:\n                max_wealth = wealth\n        \n        return max_wealth", "title": "Richest Customer Wealth", "url": "/submissions/detail/1000089391/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1689935194, "status": 10, "runtime": "66 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth = 0
        for i in range(len(accounts)):
            wealth = 0
            for j in range(len(accounts[i])):
                wealth += accounts[i][j]

            if wealth > max_wealth:
                max_wealth = wealth

        return max_wealth
