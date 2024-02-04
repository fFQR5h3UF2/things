# Submission title: for Backspace String Compare
# Submission url  : https://leetcode.com/submissions/detail/1079211036/
# Submission json : {"id": 1079211036, "status_display": "Accepted", "lang": "python3", "question_id": 874, "title_slug": "backspace-string-compare", "code": "class Solution:\n    def backspaceCompare(self, s: str, t: str) -> bool:\n        i1, i2 = len(s) - 1, len(t) - 1\n        skip1, skip2 = 0, 0\n\n        while i1 >= 0 or i2 >= 0:\n            char1, char2 = s[i1] if i1 >= 0 else \"\", t[i2] if i2 >= 0 else \"\"\n            if char1 == \"#\":\n                i1 -= 1\n                skip1 += 1\n            elif char2 == \"#\":\n                i2 -= 1\n                skip2 += 1\n            elif skip1 > 0:\n                i1 -= 1\n                skip1 -= 1\n            elif skip2 > 0:\n                i2 -= 1\n                skip2 -= 1\n            elif char1 != char2:\n                return False\n            else:\n                i1 -= 1\n                i2 -= 1\n        \n        return True ", "title": "Backspace String Compare", "url": "/submissions/detail/1079211036/", "lang_name": "Python3", "time": "3\u00a0months, 2\u00a0weeks", "timestamp": 1697724586, "status": 10, "runtime": "41 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        i1, i2 = len(s) - 1, len(t) - 1
        skip1, skip2 = 0, 0

        while i1 >= 0 or i2 >= 0:
            char1, char2 = s[i1] if i1 >= 0 else "", t[i2] if i2 >= 0 else ""
            if char1 == "#":
                i1 -= 1
                skip1 += 1
            elif char2 == "#":
                i2 -= 1
                skip2 += 1
            elif skip1 > 0:
                i1 -= 1
                skip1 -= 1
            elif skip2 > 0:
                i2 -= 1
                skip2 -= 1
            elif char1 != char2:
                return False
            else:
                i1 -= 1
                i2 -= 1

        return True
