# Submission title: for License Key Formatting
# Submission url  : https://leetcode.com/submissions/detail/1002796928/
# Submission json : {"id": 1002796928, "status_display": "Accepted", "lang": "python3", "question_id": 482, "title_slug": "license-key-formatting", "code": "class Solution:\n    def licenseKeyFormatting(self, s: str, k: int) -> str:\n        result = []\n        count = 0\n        for letter in reversed(s):\n            if letter == \"-\":\n                continue\n\n            if count == k:\n                result.append(\"-\")\n                count = 0\n            \n            count += 1\n            result.append(letter.upper())\n\n        return \"\".join(reversed(result))", "title": "License Key Formatting", "url": "/submissions/detail/1002796928/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690216488, "status": 10, "runtime": "71 ms", "is_pending": "Not Pending", "memory": "20.5 MB", "compare_result": "11111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        result = []
        count = 0
        for letter in reversed(s):
            if letter == "-":
                continue

            if count == k:
                result.append("-")
                count = 0

            count += 1
            result.append(letter.upper())

        return "".join(reversed(result))
