# Submission title: for First Unique Character in a String
# Submission url  : https://leetcode.com/submissions/detail/1002664084/
# Submission json : {"id": 1002664084, "status_display": "Accepted", "lang": "python3", "question_id": 387, "title_slug": "first-unique-character-in-a-string", "code": "class Solution:\n    def firstUniqChar(self, s: str) -> int:\n        counts = defaultdict(int)\n        repeated_index = len(s)\n        for letter in s:\n            counts[letter] += 1\n        \n        for i, letter in enumerate(s):\n            if counts[letter] != 1:\n                continue\n            \n            return i\n        \n        return -1", "title": "First Unique Character in a String", "url": "/submissions/detail/1002664084/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690206693, "status": 10, "runtime": "125 ms", "is_pending": "Not Pending", "memory": "16.6 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def firstUniqChar(self, s: str) -> int:
        counts = defaultdict(int)
        repeated_index = len(s)
        for letter in s:
            counts[letter] += 1

        for i, letter in enumerate(s):
            if counts[letter] != 1:
                continue

            return i

        return -1
