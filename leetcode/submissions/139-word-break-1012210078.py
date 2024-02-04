# Submission for Word Break
# Submission url: https://leetcode.com/submissions/detail/1012210078/


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        length = len(s)
        word_dict = set(wordDict)

        if length == 1:
            return s in word_dict

        if s in word_dict:
            return True

        left = 0
        for right in range(0, length):
            if s[left : right + 1] not in word_dict:
                continue

            left = right + 1

        return left == length
