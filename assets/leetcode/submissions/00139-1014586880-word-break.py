# Submission title: Word Break
# Submission url  : https://leetcode.com/problems/word-break/description/
# Submission url  : https://leetcode.com/submissions/detail/1014586880/"


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break

        return dp[-1]
