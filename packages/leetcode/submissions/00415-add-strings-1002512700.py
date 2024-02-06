# Submission title: for Add Strings
# Submission url  : https://leetcode.com/submissions/detail/1002512700/
# Submission json : {"id": 1002512700, "status_display": "Accepted", "lang": "python3", "question_id": 415, "title_slug": "add-strings", "code": "class Solution:\n    def addStrings(self, num1: str, num2: str) -> str:\n        result = []\n        length_1, length_2 = len(num1), len(num2)\n        index_1, index_2 = length_1 - 1, length_2 - 1\n\n\n        carry = 0\n        while index_1 >= 0 or index_2 >= 0 or carry:\n            digit_1 = num1[index_1] if index_1 >= 0 else 0\n            digit_2 = num2[index_2] if index_2 >= 0 else 0\n            digit = int(digit_1) + int(digit_2) + carry\n            if digit > 9:\n                carry = 1\n                digit %= 10\n            else:\n                carry = 0\n\n            result.append(str(digit))\n            index_1 -= 1\n            index_2 -= 1 \n\n        return \"\".join(reversed(result))", "title": "Add Strings", "url": "/submissions/detail/1002512700/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1690192582, "status": 10, "runtime": "62 ms", "is_pending": "Not Pending", "memory": "16.8 MB", "compare_result": "11111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        result = []
        length_1, length_2 = len(num1), len(num2)
        index_1, index_2 = length_1 - 1, length_2 - 1

        carry = 0
        while index_1 >= 0 or index_2 >= 0 or carry:
            digit_1 = num1[index_1] if index_1 >= 0 else 0
            digit_2 = num2[index_2] if index_2 >= 0 else 0
            digit = int(digit_1) + int(digit_2) + carry
            if digit > 9:
                carry = 1
                digit %= 10
            else:
                carry = 0

            result.append(str(digit))
            index_1 -= 1
            index_2 -= 1

        return "".join(reversed(result))
