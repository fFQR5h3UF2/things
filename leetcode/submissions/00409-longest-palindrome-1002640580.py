# Submission title: Longest Palindrome
# Submission url  : https://leetcode.com/problems/longest-palindrome/description/
# Submission url  : https://leetcode.com/submissions/detail/1002640580/
# Submission json : {"id":1002640580,"status_display":"Accepted","lang":"python3","question_id":409,"title_slug":"longest-palindrome","code":"class Solution:\n    def longestPalindrome(self, s: str) -> int:\n        counts = defaultdict(int)\n\n        for letter in s:\n            counts[letter] += 1\n        \n        result = sum(count if count % 2 == 0 else count - 1\n                     for symbol, count in counts.items())\n\n        if result < len(s):\n            result += 1\n\n        return result","title":"Longest Palindrome","url":"/submissions/detail/1002640580/","lang_name":"Python3","time":"6 months, 2 weeks","timestamp":1690204779,"status":10,"runtime":"42 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = defaultdict(int)

        for letter in s:
            counts[letter] += 1

        result = sum(
            count if count % 2 == 0 else count - 1 for symbol, count in counts.items()
        )

        if result < len(s):
            result += 1

        return result
