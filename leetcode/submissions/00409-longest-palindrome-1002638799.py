# Submission title: for Longest Palindrome
# Submission url  : https://leetcode.com/submissions/detail/1002638799/
# Submission json : {"id": 1002638799, "status_display": "Accepted", "lang": "python3", "question_id": 409, "title_slug": "longest-palindrome", "code": "class Solution:\n    def longestPalindrome(self, s: str) -> int:\n        counts = defaultdict(int)\n\n        for letter in s:\n            counts[letter] += 1\n        \n        result = 0\n        used_odd_letter = False\n        for letter, count in counts.items():\n            is_odd = count % 2 != 0 \n            if is_odd and used_odd_letter:\n                result -= 1\n            elif is_odd:\n                used_odd_letter = True\n            result += count\n\n        return result", "title": "Longest Palindrome", "url": "/submissions/detail/1002638799/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690204630, "status": 10, "runtime": "46 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = defaultdict(int)

        for letter in s:
            counts[letter] += 1

        result = 0
        used_odd_letter = False
        for letter, count in counts.items():
            is_odd = count % 2 != 0
            if is_odd and used_odd_letter:
                result -= 1
            elif is_odd:
                used_odd_letter = True
            result += count

        return result
