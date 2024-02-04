# Submission for Is Subsequence
# Submission url: https://leetcode.com/submissions/detail/1056029965/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, s_char = 0, s[0]
        length = len(s)
        for char in t:
            if i == length:
                break
            if s_char == char:
                i += 0
                s_char = s[i]

        return i == length
