# Submission title: Binary Trees With Factors
# Submission url  : https://leetcode.com/problems/binary-trees-with-factors/description/
# Submission url  : https://leetcode.com/submissions/detail/1084880212/
# Submission json : {"id":1084880212,"status_display":"Accepted","lang":"python3","question_id":843,"title_slug":"binary-trees-with-factors","code":"MOD = 10**9 + 7\n\nclass Solution:\n    def numFactoredBinaryTrees(self, arr: List[int]) -> int:\n        arr.sort()\n        s = set(arr)\n        dp = {x: 1 for x in arr}\n        \n        for i in arr:\n            for j in arr:\n                if j > i**0.5:\n                    break\n                if i % j == 0 and i // j in s:\n                    if i // j == j:\n                        dp[i] += dp[j] * dp[j]\n                    else:\n                        dp[i] += dp[j] * dp[i // j] * 2\n                    dp[i] %= MOD\n        \n        return sum(dp.values()) % MOD\n","title":"Binary Trees With Factors","url":"/submissions/detail/1084880212/","lang_name":"Python3","time":"3 months, 1 week","timestamp":1698350842,"status":10,"runtime":"135 ms","is_pending":"Not Pending","memory":"16.5 MB","compare_result":"111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}

MOD = 10**9 + 7


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        arr.sort()
        s = set(arr)
        dp = {x: 1 for x in arr}

        for i in arr:
            for j in arr:
                if j > i**0.5:
                    break
                if i % j == 0 and i // j in s:
                    if i // j == j:
                        dp[i] += dp[j] * dp[j]
                    else:
                        dp[i] += dp[j] * dp[i // j] * 2
                    dp[i] %= MOD

        return sum(dp.values()) % MOD
