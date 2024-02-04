# Submission for Find the Difference
# Submission url: https://leetcode.com/submissions/detail/1058460034/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        count = Counter(s)
        for char in t:
            count[char] -= 1
            if count[char] == -1:
                return char
