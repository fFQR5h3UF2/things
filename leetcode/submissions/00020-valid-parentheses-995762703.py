# Submission title: Valid Parentheses
# Submission url  : https://leetcode.com/problems/valid-parentheses/description/
# Submission url  : https://leetcode.com/submissions/detail/995762703/
# Submission json : {"id":995762703,"status_display":"Accepted","lang":"python3","question_id":20,"title_slug":"valid-parentheses","code":"class Solution:\n    def isValid(self, s: str) -> bool:\n        length = len(s)\n        if length < 2:\n            return False\n\n        brackets_open = {\n            \"{\": \"}\",\n            \"(\": \")\",\n            \"[\": \"]\"\n        }\n        brackets_close = brackets_open.values()\n        stack = [s[0]]\n\n        for bracket in s[1:]:\n            if bracket not in brackets_close:\n                stack.append(bracket)\n                continue\n\n            if len(stack) == 0 or brackets_open.get(stack[-1]) != bracket:\n                return False\n            \n            stack.pop()\n\n        return not len(stack) ","title":"Valid Parentheses","url":"/submissions/detail/995762703/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689500315,"status":10,"runtime":"52 ms","is_pending":"Not Pending","memory":"16.5 MB","compare_result":"111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if length < 2:
            return False

        brackets_open = {"{": "}", "(": ")", "[": "]"}
        brackets_close = brackets_open.values()
        stack = [s[0]]

        for bracket in s[1:]:
            if bracket not in brackets_close:
                stack.append(bracket)
                continue

            if len(stack) == 0 or brackets_open.get(stack[-1]) != bracket:
                return False

            stack.pop()

        return not len(stack)
