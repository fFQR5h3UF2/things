# Submission for Backspace String Compare
# Submission url: https://leetcode.com/submissions/detail/1079206898/


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i1, i2 = len(s) - 1, len(t) - 1
        skip1, skip2 = 0, 0

        while i1 >= 0 or i2 >= 0:
            char1, char2 = s[i1] if i1 >= 0 else "", t[i2] if i2 >= 0 else ""
            if char1 == "#":
                i1 -= 1
                skip1 += 1
            elif char2 == "#":
                i2 -= 1
                skip2 += 1
            elif skip1:
                i1 -= skip1
                skip1 = 0
            elif skip2:
                i2 -= skip2
                skip2 = 0
            elif char1 != char2:
                return False
            i1 -= 1
            i2 -= 1

        return True
