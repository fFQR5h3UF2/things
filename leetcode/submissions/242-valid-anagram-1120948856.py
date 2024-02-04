# Submission for 'Valid Anagram'
# Submission url: https://leetcode.com/submissions/detail/1120948856/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False

        letters = [0] * 26
        for char in s:
            letters[ord(char) - ord('a')] += 1

        for char in t:
            i = ord(char) - ord('a')
            letters[i] -= 1
            if letters[i] < 0:
                return False

        return True
