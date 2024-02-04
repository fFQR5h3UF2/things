# Submission for Length of Last Word
# Submission url: https://leetcode.com/submissions/detail/989388793/


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])
