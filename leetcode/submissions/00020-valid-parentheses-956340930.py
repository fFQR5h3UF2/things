# Submission title: for Valid Parentheses
# Submission url  : https://leetcode.com/submissions/detail/956340930/
# Submission json : {"id": 956340930, "status_display": "Accepted", "lang": "python3", "question_id": 20, "title_slug": "valid-parentheses", "code": "class Solution:\n    def isValid(self, s: str) -> bool:\n        brackets = []\n\n        symbols = {\n            \"{\": \"}\",\n            \"(\": \")\",\n            \"[\": \"]\"\n        }\n\n        open = symbols.keys()\n        closed = symbols.values()\n\n        for bracket in s:\n            if bracket in open:\n                brackets.append(bracket)\n                continue\n\n            if not brackets:\n                return False\n\n            last_bracket = brackets[-1]\n            if last_bracket in closed: \n                return False\n\n            correct_closing_bracket = symbols[last_bracket]\n            if bracket != correct_closing_bracket:\n                return False\n            \n            brackets.pop()\n\n        return not len(brackets)", "title": "Valid Parentheses", "url": "/submissions/detail/956340930/", "lang_name": "Python3", "time": "8\u00a0months, 2\u00a0weeks", "timestamp": 1684919609, "status": 10, "runtime": "43 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []

        symbols = {"{": "}", "(": ")", "[": "]"}

        open = symbols.keys()
        closed = symbols.values()

        for bracket in s:
            if bracket in open:
                brackets.append(bracket)
                continue

            if not brackets:
                return False

            last_bracket = brackets[-1]
            if last_bracket in closed:
                return False

            correct_closing_bracket = symbols[last_bracket]
            if bracket != correct_closing_bracket:
                return False

            brackets.pop()

        return not len(brackets)
