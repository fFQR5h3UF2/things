# Submission title: Longest Palindrome
# Submission url  : https://leetcode.com/problems/longest-palindrome/description/"
# Submission url  : https://leetcode.com/submissions/detail/1002640580/"


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = defaultdict(int)

        for letter in s:
            counts[letter] += 1

        result = sum(
            count if count % 2 == 0 else count - 1
            for symbol, count in counts.items()
        )

        if result < len(s):
            result += 1

        return result
