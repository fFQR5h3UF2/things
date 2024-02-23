# Submission title: Find First Palindromic String in the Array
# Submission url  : https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
# Submission url  : https://leetcode.com/submissions/detail/1174154785/"


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for s in words:
            for i in range(len(s) // 2):
                if s[i] != s[-i - 1]:
                    break
            else:
                return s
        return ""
