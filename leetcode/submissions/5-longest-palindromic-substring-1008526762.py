# Submission for Longest Palindromic Substring
# Submission url: https://leetcode.com/submissions/detail/1008526762/


class Solution:
    def longestPalindrome(self, s: str) -> str:

        @cache
        def longest_substr_pal(i: int, j: int) -> str:
            if i == j:
                return s[i]

            length = j - i + 1
            is_even = length % 2 == 0
            half = length // 2

            if is_even and s[i : i + half] == s[j : i + half - 1 : -1]:
                return s[i : j + 1]

            if not is_even and s[i : i + half] == s[j : i + half : -1]:
                return s[i : j + 1]

            ignore_left = longest_substr_pal(i + 1, j)
            ignore_right = longest_substr_pal(i, j - 1)

            return ignore_left if len(ignore_left) > len(ignore_right) else ignore_right

        return longest_substr_pal(0, len(s) - 1)
