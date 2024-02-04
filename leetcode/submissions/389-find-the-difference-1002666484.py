# Submission for 'Find the Difference'
# Submission url: https://leetcode.com/submissions/detail/1002666484/

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        letters = defaultdict(int)
        for letter in s:
            letters[letter] += 1

        for letter in t:
            if letters[letter] == 0:
                return letter

            letters[letter] -= 1

        return None
