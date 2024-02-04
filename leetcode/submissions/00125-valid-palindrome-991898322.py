# Submission title: for Valid Palindrome
# Submission url  : https://leetcode.com/submissions/detail/991898322/
# Submission json : {"id": 991898322, "status_display": "Accepted", "lang": "python3", "question_id": 125, "title_slug": "valid-palindrome", "code": "class Solution:\n    def isPalindrome(self, s: str) -> bool:\n        length = len(s)\n\n        # if the sring has only one symbol and it is alphanumeric, it is a palyndrom\n        if s.isalnum() and length == 1:\n            return True \n        \n        i, j = 0, length - 1\n        # iterate from the start and from the end using two indexes:\n        # - if one the symbols is not alphanumeric, move the corresponding index\n        # - if symbols are alphanumeric and not equal, return False\n        # - move indexes\n        while i < j:\n            symbol_start, symbol_end = s[i].lower(), s[j].lower()\n            if not symbol_start.isalnum():\n                i += 1\n                continue\n            if not symbol_end.isalnum():\n                j -= 1\n                continue\n            \n            if symbol_start != symbol_end:\n                return False\n            \n            i += 1\n            j -= 1\n        \n        return True", "title": "Valid Palindrome", "url": "/submissions/detail/991898322/", "lang_name": "Python3", "time": "6\u00a0months, 4\u00a0weeks", "timestamp": 1689086547, "status": 10, "runtime": "68 ms", "is_pending": "Not Pending", "memory": "17.1 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def isPalindrome(self, s: str) -> bool:
        length = len(s)

        # if the sring has only one symbol and it is alphanumeric, it is a palyndrom
        if s.isalnum() and length == 1:
            return True

        i, j = 0, length - 1
        # iterate from the start and from the end using two indexes:
        # - if one the symbols is not alphanumeric, move the corresponding index
        # - if symbols are alphanumeric and not equal, return False
        # - move indexes
        while i < j:
            symbol_start, symbol_end = s[i].lower(), s[j].lower()
            if not symbol_start.isalnum():
                i += 1
                continue
            if not symbol_end.isalnum():
                j -= 1
                continue

            if symbol_start != symbol_end:
                return False

            i += 1
            j -= 1

        return True
