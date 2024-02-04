# Submission for Evaluate Reverse Polish Notation
# Submission url: https://leetcode.com/submissions/detail/997574303/


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        length = len(tokens)
        stack = []
        for token in tokens:
            if token.lstrip("-").isalnum():
                stack.append(int(token))
                continue

            second, first = stack.pop(), stack.pop()
            result = 0
            match token:
                case "+":
                    result = first + second
                case "-":
                    result = first - second
                case "*":
                    result = first * second
                case "/":
                    result = first // second
                case _:
                    raise Exception(f"invalid token: {token}")

            stack.append(result)

        return stack[-1]
