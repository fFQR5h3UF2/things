# Submission title: for Minimum Number of Steps to Make Two Strings Anagram
# Submission url  : https://leetcode.com/submissions/detail/1145100663/
# Submission json : {"id": 1145100663, "status_display": "Accepted", "lang": "python3", "question_id": 1469, "title_slug": "minimum-number-of-steps-to-make-two-strings-anagram", "code": "class Solution:\n    def minSteps(self, s: str, t: str) -> int:\n        count_s = [0] * 26\n        count_t = [0] * 26\n\n        for char in s:\n            count_s[ord(char) - ord('a')] += 1\n\n        for char in t:\n            count_t[ord(char) - ord('a')] += 1\n\n        steps = 0\n        for i in range(26):\n            steps += abs(count_s[i] - count_t[i])\n\n        return steps // 2", "title": "Minimum Number of Steps to Make Two Strings Anagram", "url": "/submissions/detail/1145100663/", "lang_name": "Python3", "time": "3\u00a0weeks, 1\u00a0day", "timestamp": 1705156428, "status": 10, "runtime": "149 ms", "is_pending": "Not Pending", "memory": "17.8 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = [0] * 26
        count_t = [0] * 26

        for char in s:
            count_s[ord(char) - ord("a")] += 1

        for char in t:
            count_t[ord(char) - ord("a")] += 1

        steps = 0
        for i in range(26):
            steps += abs(count_s[i] - count_t[i])

        return steps // 2
