# Submission for Richest Customer Wealth
# Submission url: https://leetcode.com/submissions/detail/1000089391/


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
