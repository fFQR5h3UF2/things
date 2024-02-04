# Submission for Find the Difference
# Submission url: https://leetcode.com/submissions/detail/1002665137/


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = set(s)
        for letter in t:
            if letter in letters:
                continue

            return letter

        return None
