# Submission title: Word Break
# Submission url  : https://leetcode.com/problems/word-break/description/
# Submission url  : https://leetcode.com/submissions/detail/1014585529/"


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @cache
        def dp(i):
            if i < 0:
                return True

            for word in wordDict:
                if s[i - len(word) + 1 : i + 1] == word and dp(i - len(word)):
                    return True

            return False

        return dp(len(s) - 1)
