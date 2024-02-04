# Submission title: for Valid Anagram
# Submission url  : https://leetcode.com/submissions/detail/1120948856/
# Submission json : {"id": 1120948856, "status_display": "Accepted", "lang": "python3", "question_id": 242, "title_slug": "valid-anagram", "code": "class Solution:\n    def isAnagram(self, s: str, t: str) -> bool:\n        if (len(s) != len(t)):\n            return False\n            \n        letters = [0] * 26\n        for char in s:\n            letters[ord(char) - ord('a')] += 1\n        \n        for char in t:\n            i = ord(char) - ord('a')\n            letters[i] -= 1\n            if letters[i] < 0:\n                return False\n\n        return True", "title": "Valid Anagram", "url": "/submissions/detail/1120948856/", "lang_name": "Python3", "time": "1\u00a0month, 2\u00a0weeks", "timestamp": 1702720915, "status": 10, "runtime": "63 ms", "is_pending": "Not Pending", "memory": "16.8 MB", "compare_result": "111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = [0] * 26
        for char in s:
            letters[ord(char) - ord("a")] += 1

        for char in t:
            i = ord(char) - ord("a")
            letters[i] -= 1
            if letters[i] < 0:
                return False

        return True
