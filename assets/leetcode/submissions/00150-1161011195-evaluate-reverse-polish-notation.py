# Submission title: Evaluate Reverse Polish Notation
# Submission url  : https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# Submission url  : https://leetcode.com/submissions/detail/1161011195/"


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
