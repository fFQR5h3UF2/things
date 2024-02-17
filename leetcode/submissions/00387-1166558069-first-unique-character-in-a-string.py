# Submission title: First Unique Character in a String
# Submission url  : https://leetcode.com/problems/first-unique-character-in-a-string/description/"
# Submission url  : https://leetcode.com/submissions/detail/1166558069/"


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = [0] * 26

        for char in s:
            idx = ord(char) - ord("a")
            if counter[idx] in (0, 1):
                counter[idx] += 1
        for i in range(len(s)):
            if counter[ord(s[i]) - ord("a")] == 1:
                return i
        return -1
