# Submission title: Number of Dice Rolls With Target Sum
# Submission url  : https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/description/
# Submission url  : https://leetcode.com/submissions/detail/1128708587/
# Submission json : {"id":1128708587,"status_display":"Accepted","lang":"python3","question_id":1263,"title_slug":"number-of-dice-rolls-with-target-sum","code":"class Solution:\n    mod = 10 ** 9 + 7\n\n    def numRollsToTarget(self, n: int, k: int, target: int) -> int:\n        dp = [[-1] * (target + 1) for _ in range(n + 1)]\n        return self.recursion(dp, n, k, target)\n\n    def recursion(self, dp: list, n: int, k: int, target: int) -> int:\n        if target == 0 and n == 0:\n            return 1\n        if n == 0 or target <= 0:\n            return 0\n\n        if dp[n][target] != -1:\n            return dp[n][target] % self.mod\n\n        ways = 0\n        for i in range(1, k + 1):\n            ways = (ways + self.recursion(dp, n - 1, k, target - i)) % self.mod\n\n        dp[n][target] = ways % self.mod\n        return dp[n][target]\n\n\n","title":"Number of Dice Rolls With Target Sum","url":"/submissions/detail/1128708587/","lang_name":"Python3","time":"1 month, 1 week","timestamp":1703578104,"status":10,"runtime":"282 ms","is_pending":"Not Pending","memory":"17.6 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    mod = 10**9 + 7

    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        dp = [[-1] * (target + 1) for _ in range(n + 1)]
        return self.recursion(dp, n, k, target)

    def recursion(self, dp: list, n: int, k: int, target: int) -> int:
        if target == 0 and n == 0:
            return 1
        if n == 0 or target <= 0:
            return 0

        if dp[n][target] != -1:
            return dp[n][target] % self.mod

        ways = 0
        for i in range(1, k + 1):
            ways = (ways + self.recursion(dp, n - 1, k, target - i)) % self.mod

        dp[n][target] = ways % self.mod
        return dp[n][target]
