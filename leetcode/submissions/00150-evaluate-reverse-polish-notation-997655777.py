# Submission title: Evaluate Reverse Polish Notation
# Submission url  : https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# Submission url  : https://leetcode.com/submissions/detail/997655777/
# Submission json : {"id":997655777,"status_display":"Accepted","lang":"python3","question_id":150,"title_slug":"evaluate-reverse-polish-notation","code":"class Solution:\n    def evalRPN(self, tokens: List[str]) -> int:\n        stack = []\n        operations = {\n            \"+\": lambda first, second: first + second,\n            \"-\": lambda first, second: first - second,\n            \"*\": lambda first, second: first * second,\n            \"/\": lambda first, second: int(first / second)\n        }\n        for token in tokens:\n            if token not in operations:\n                stack.append(int(token))\n                continue\n\n            second, first = stack.pop(), stack.pop()\n            result = operations[token](first, second)\n            stack.append(result)\n            \n        return stack[-1]","title":"Evaluate Reverse Polish Notation","url":"/submissions/detail/997655777/","lang_name":"Python3","time":"6 months, 3 weeks","timestamp":1689692314,"status":10,"runtime":"90 ms","is_pending":"Not Pending","memory":"16.8 MB","compare_result":"111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operations = {
            "+": lambda first, second: first + second,
            "-": lambda first, second: first - second,
            "*": lambda first, second: first * second,
            "/": lambda first, second: int(first / second),
        }
        for token in tokens:
            if token not in operations:
                stack.append(int(token))
                continue

            second, first = stack.pop(), stack.pop()
            result = operations[token](first, second)
            stack.append(result)

        return stack[-1]
