# Submission title: Generate Parentheses
# Submission url  : https://leetcode.com/problems/generate-parentheses/description/
# Submission url  : https://leetcode.com/submissions/detail/1010069020/
# Submission json : {"id":1010069020,"status_display":"Accepted","lang":"python3","question_id":22,"title_slug":"generate-parentheses","code":"class Solution:\n    def generateParenthesis(self, n: int) -> List[str]:\n\n        current = []\n        current_max = n * 2\n        chars = \"()\"\n\n\n        def backtrack(open: int, closed: int) -> Generator[None, None, List[str]]:\n            if len(current) == current_max:\n                yield \"\".join(current)\n            \n            if open:\n                current.append(chars[0])\n                yield from backtrack(open - 1, closed)\n                current.pop()\n            \n            if closed and closed > open:\n                current.append(chars[1])\n                yield from backtrack(open, closed - 1)\n                current.pop()\n        \n        return tuple(combination for combination in backtrack(n, n))","title":"Generate Parentheses","url":"/submissions/detail/1010069020/","lang_name":"Python3","time":"6 months","timestamp":1690961955,"status":10,"runtime":"42 ms","is_pending":"Not Pending","memory":"16.6 MB","compare_result":"11111111","has_notes":false,"flag_type":1}


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        current = []
        current_max = n * 2
        chars = "()"

        def backtrack(open: int, closed: int) -> Generator[None, None, List[str]]:
            if len(current) == current_max:
                yield "".join(current)

            if open:
                current.append(chars[0])
                yield from backtrack(open - 1, closed)
                current.pop()

            if closed and closed > open:
                current.append(chars[1])
                yield from backtrack(open, closed - 1)
                current.pop()

        return tuple(combination for combination in backtrack(n, n))
