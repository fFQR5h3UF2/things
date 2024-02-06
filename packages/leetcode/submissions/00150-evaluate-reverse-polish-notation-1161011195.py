# Submission title: for Evaluate Reverse Polish Notation
# Submission url  : https://leetcode.com/submissions/detail/1161011195/
# Submission json : {"id": 1161011195, "status_display": "Accepted", "lang": "python3", "question_id": 150, "title_slug": "evaluate-reverse-polish-notation", "code": "class Solution:\n    def evalRPN(self, tokens: List[str]) -> int:\n        stack: list[int] = []\n        for token in tokens:\n            match token:\n                case \"+\":\n                    stack.append(stack.pop() + stack.pop())\n                case \"-\":\n                    last, prev = stack.pop(), stack.pop()\n                    stack.append(prev - last)\n                case \"*\":\n                    stack.append(stack.pop() * stack.pop())\n                case \"/\": \n                    last, prev = stack.pop(), stack.pop()\n                    stack.append(int(prev / last))\n                case _:\n                    stack.append(int(token))\n        return stack[0]", "title": "Evaluate Reverse Polish Notation", "url": "/submissions/detail/1161011195/", "lang_name": "Python3", "time": "5\u00a0days, 2\u00a0hours", "timestamp": 1706618212, "status": 10, "runtime": "64 ms", "is_pending": "Not Pending", "memory": "17.1 MB", "compare_result": "111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack: list[int] = []
        for token in tokens:
            match token:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    last, prev = stack.pop(), stack.pop()
                    stack.append(prev - last)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    last, prev = stack.pop(), stack.pop()
                    stack.append(int(prev / last))
                case _:
                    stack.append(int(token))
        return stack[0]
