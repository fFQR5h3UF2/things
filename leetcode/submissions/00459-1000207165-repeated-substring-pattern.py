# Submission title: Repeated Substring Pattern
# Submission url  : https://leetcode.com/problems/repeated-substring-pattern/description/
# Submission url  : https://leetcode.com/submissions/detail/1000207165/"


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        length = len(s)
        for i in range(length - 1):
            if length % (i + 1) != 0:
                continue

            if s == s[: i + 1] * (length // (i + 1)):
                return True

        return False
