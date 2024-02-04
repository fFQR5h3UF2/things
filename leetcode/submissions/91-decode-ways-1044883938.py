# Submission for Decode Ways
# Submission url: https://leetcode.com/submissions/detail/1044883938/


class Solution:
    def numDecodings(self, s: str) -> int:
        char_count = len(s)
        if s[0] == "0":
            return 0
        if char_count == 1:
            return 1

        ways_count = 1
        for i in range(1, char_count):
            num, next_num = s[i - 1 : i + 1], s[i + 1] if i + 1 < char_count else "-1"
            if num == "00":
                return 0
            if "0" in num or num > "27" or next_num == "0":
                continue
            ways_count += 1

        return ways_count
