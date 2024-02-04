# Submission for Backspace String Compare
# Submission url: https://leetcode.com/submissions/detail/1079202281/


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i1, i2 = len(s) - 1, len(t) - 1

        while i1 >= 0 and i2 >= 0:
            char1, char2 = s[i1] if i1 >= 0 else "", t[i2] if i2 >= 0 else ""
            if char1 == "#":
                i1 -= 2
                continue
            if char2 == "#":
                i2 -= 2
                continue
            if char1 != char2:
                return False
            i1 -= 1
            i2 -= 1

        return True
