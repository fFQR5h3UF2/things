# Submission title: for Ransom Note
# Submission url  : https://leetcode.com/submissions/detail/995209217/
# Submission json : {"id": 995209217, "status_display": "Accepted", "lang": "python3", "question_id": 383, "title_slug": "ransom-note", "code": "class Solution:\n    # two indexes: ransom_i, magazine_i\n    # sort both ransomNote and magazine (ascending order)\n    # while indexes have not reached the end:\n    # - if ransom symbol is equal to the magazine_symbol: increase both indexes\n    # - if it is not equal, increase only magazine index\n    # return wheter the ranson index is equal to the length of the ransom\n    def canConstruct(self, ransomNote: str, magazine: str) -> bool:\n        ransom_i, magazine_i = 0, 0\n        ransom_length, magazine_length = len(ransomNote), len(magazine)\n\n        if magazine_length < ransom_length:\n            return False\n        \n        if ransom_length == 1:\n            return ransomNote in magazine\n\n        ransomNote = sorted(ransomNote)\n        magazine = sorted(magazine)\n\n        while ransom_i < ransom_length and magazine_i < magazine_length:\n            ransom_symbol, magazine_symbol = ransomNote[ransom_i], magazine[magazine_i]\n            \n            if magazine_symbol > ransom_symbol:\n                return False\n\n            if ransom_symbol == magazine_symbol:\n                ransom_i += 1\n            \n            magazine_i += 1\n\n        return ransom_i == ransom_length", "title": "Ransom Note", "url": "/submissions/detail/995209217/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689440132, "status": 10, "runtime": "143 ms", "is_pending": "Not Pending", "memory": "16.8 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    # two indexes: ransom_i, magazine_i
    # sort both ransomNote and magazine (ascending order)
    # while indexes have not reached the end:
    # - if ransom symbol is equal to the magazine_symbol: increase both indexes
    # - if it is not equal, increase only magazine index
    # return wheter the ranson index is equal to the length of the ransom
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_i, magazine_i = 0, 0
        ransom_length, magazine_length = len(ransomNote), len(magazine)

        if magazine_length < ransom_length:
            return False

        if ransom_length == 1:
            return ransomNote in magazine

        ransomNote = sorted(ransomNote)
        magazine = sorted(magazine)

        while ransom_i < ransom_length and magazine_i < magazine_length:
            ransom_symbol, magazine_symbol = ransomNote[ransom_i], magazine[magazine_i]

            if magazine_symbol > ransom_symbol:
                return False

            if ransom_symbol == magazine_symbol:
                ransom_i += 1

            magazine_i += 1

        return ransom_i == ransom_length
