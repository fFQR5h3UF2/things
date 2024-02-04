# Submission title: for Ransom Note
# Submission url  : https://leetcode.com/submissions/detail/995216343/
# Submission json : {"id": 995216343, "status_display": "Accepted", "lang": "python3", "question_id": 383, "title_slug": "ransom-note", "code": "class Solution:\n    def canConstruct(self, ransomNote: str, magazine: str) -> bool:\n        ransom_i, magazine_i = 0, 0\n        ransom_length, magazine_length = len(ransomNote), len(magazine)\n\n        if magazine_length < ransom_length:\n            return False\n        \n        if ransom_length == 1:\n            return ransomNote in magazine\n\n        symbols = [0 for _ in range(26)]\n\n        for symbol in magazine:\n            symbols[ord(symbol)-97] += 1\n\n        for symbol in ransomNote:\n            symbols[ord(symbol)-97] -= 1\n        \n        \n        return not any((count < 0 for count in symbols))", "title": "Ransom Note", "url": "/submissions/detail/995216343/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689440743, "status": 10, "runtime": "89 ms", "is_pending": "Not Pending", "memory": "16.7 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_i, magazine_i = 0, 0
        ransom_length, magazine_length = len(ransomNote), len(magazine)

        if magazine_length < ransom_length:
            return False

        if ransom_length == 1:
            return ransomNote in magazine

        symbols = [0 for _ in range(26)]

        for symbol in magazine:
            symbols[ord(symbol) - 97] += 1

        for symbol in ransomNote:
            symbols[ord(symbol) - 97] -= 1

        return not any((count < 0 for count in symbols))
