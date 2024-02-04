# Submission for Longest Palindromic Substring
# Submission url: https://leetcode.com/submissions/detail/1085420219/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(string: str) -> bool:
            return all(string[i] == string[-(i + 1)] for i in range(len(string) // 2))

        length = len(s)
        for i in range(length):
            for j in reversed(range(i + 1, length)):
                sub = s[i : j + 1]
                if is_palindrome(sub):
                    return sub
