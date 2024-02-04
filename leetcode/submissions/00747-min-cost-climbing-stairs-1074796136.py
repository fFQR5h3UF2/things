# Submission title: for Min Cost Climbing Stairs
# Submission url  : https://leetcode.com/submissions/detail/1074796136/
# Submission json : {"id": 1074796136, "status_display": "Accepted", "lang": "python3", "question_id": 747, "title_slug": "min-cost-climbing-stairs", "code": "class Solution:\n    def minCostClimbingStairs(self, cost):\n        n = len(cost)\n        dp = [0] * n\n        dp[0] = cost[0]\n        dp[1] = cost[1]\n        \n        for i in range(2, n):\n            dp[i] = cost[i] + min(dp[i-1], dp[i-2])\n        \n        return min(dp[n-1], dp[n-2])", "title": "Min Cost Climbing Stairs", "url": "/submissions/detail/1074796136/", "lang_name": "Python3", "time": "3\u00a0months, 3\u00a0weeks", "timestamp": 1697267680, "status": 10, "runtime": "58 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def minCostClimbingStairs(self, cost):
        n = len(cost)
        dp = [0] * n
        dp[0] = cost[0]
        dp[1] = cost[1]

        for i in range(2, n):
            dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

        return min(dp[n - 1], dp[n - 2])
