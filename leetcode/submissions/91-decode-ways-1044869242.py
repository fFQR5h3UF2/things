# Submission for Decode Ways
# Submission url: https://leetcode.com/submissions/detail/1044869242/


class Solution:
    def numDecodings(self, s: str) -> int:
        char_count = len(s)
        if char_count == 1:
            return 1
        if s[0] == "0":
            return 0
        ways_count = 1
        for i in range(1, char_count):
            if s[i] == "0":
                continue
            ways_count += 1 if s[i - 1 : i + 1] < "27" else 0

        return ways_count
