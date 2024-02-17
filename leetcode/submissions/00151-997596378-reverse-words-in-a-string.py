# Submission title: Reverse Words in a String
# Submission url  : https://leetcode.com/problems/reverse-words-in-a-string/description/"
# Submission url  : https://leetcode.com/submissions/detail/997596378/"


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])
