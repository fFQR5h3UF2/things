# Submission title: Word Break
# Submission url  : https://leetcode.com/problems/word-break/description/"
# Submission url  : https://leetcode.com/submissions/detail/1012217749/"


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def calculate(i: int) -> bool:
            if i < 0:
                return True

            for word in wordDict:
                length = len(word)
                if s[i - length + 1 : i + 1] == word and calculate(i - length):
                    return True

            return False

        return calculate(len(s) - 1)
