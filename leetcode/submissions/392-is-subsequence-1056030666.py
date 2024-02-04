# Submission for Is Subsequence
# Submission url: https://leetcode.com/submissions/detail/1056030666/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, s_char = 0, s[0]
        length = len(s)
        for char in t:
            if i == length:
                break
            if s_char == char:
                s_char = s[i]
                i += 1

        return i == length
