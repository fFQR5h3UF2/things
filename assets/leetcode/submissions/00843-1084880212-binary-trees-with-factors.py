# Submission title: Binary Trees With Factors
# Submission url  : https://leetcode.com/problems/binary-trees-with-factors/description/
# Submission url  : https://leetcode.com/submissions/detail/1084880212/"

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
