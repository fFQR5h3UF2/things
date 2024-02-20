# Submission title: Reverse Words in a String III
# Submission url  : https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
# Submission url  : https://leetcode.com/submissions/detail/1064056302/"


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(map(lambda word: word[::-1], s.split()))
