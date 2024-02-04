# Submission for Valid Parentheses
# Submission url: https://leetcode.com/submissions/detail/995760871/


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

            if len(stack) == 0 or brackets_open[stack[-1]] != bracket:
                return False

            stack.pop()

        return not len(stack)
