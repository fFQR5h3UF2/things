# Submission title: for Determine if String Halves Are Alike
# Submission url  : https://leetcode.com/submissions/detail/1144544966/
# Submission json : {"id": 1144544966, "status_display": "Accepted", "lang": "python3", "question_id": 1823, "title_slug": "determine-if-string-halves-are-alike", "code": "class Solution:\n    def halvesAreAlike(self, s: str) -> bool:\n        def count_vowels(string):\n            vowels = set('aeiouAEIOU')\n            return sum(1 for char in string if char in vowels)\n\n        length = len(s)\n        mid_point = length // 2\n\n        first_half = s[:mid_point]\n        second_half = s[mid_point:]\n\n        return count_vowels(first_half) == count_vowels(second_half)", "title": "Determine if String Halves Are Alike", "url": "/submissions/detail/1144544966/", "lang_name": "Python3", "time": "3\u00a0weeks, 1\u00a0day", "timestamp": 1705092940, "status": 10, "runtime": "30 ms", "is_pending": "Not Pending", "memory": "17.2 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_vowels(string):
            vowels = set("aeiouAEIOU")
            return sum(1 for char in string if char in vowels)

        length = len(s)
        mid_point = length // 2

        first_half = s[:mid_point]
        second_half = s[mid_point:]

        return count_vowels(first_half) == count_vowels(second_half)
