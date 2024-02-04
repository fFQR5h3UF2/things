# Submission for Longest Palindromic Substring
# Submission url: https://leetcode.com/submissions/detail/1008533325/


class Solution:
    def longestPalindrome(self, s: str) -> str:

        @cache
        def longest_substr_pal(i: int, j: int) -> Tuple[int, int]:
            length = j - i + 1
            is_even = length % 2 == 0
            half = length // 2

            if (
                i == j
                or (is_even and s[i : i + half] == s[j : i + half - 1 : -1])
                or (not is_even and s[i : i + half] == s[j : i + half : -1])
            ):
                return i, j

            ignore_left = longest_substr_pal(i + 1, j)
            ignore_right = longest_substr_pal(i, j - 1)
            left_is_bigger = (
                ignore_left[1] - ignore_left[0] > ignore_right[1] - ignore_right[0]
            )

            return ignore_left if left_is_bigger else ignore_right

        i, j = longest_substr_pal(0, len(s) - 1)

        return s[i : j + 1]
