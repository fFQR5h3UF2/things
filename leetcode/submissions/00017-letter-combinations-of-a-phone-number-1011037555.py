# Submission title: Letter Combinations of a Phone Number
# Submission url  : https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
# Submission url  : https://leetcode.com/submissions/detail/1011037555/
# Submission json : {"id":1011037555,"status_display":"Accepted","lang":"python3","question_id":17,"title_slug":"letter-combinations-of-a-phone-number","code":"class Solution:\n    def letterCombinations(self, digits: str) -> List[str]:\n        length = len(digits)\n        if length == 0:\n            return []\n\n        digit_map: Dict[int, str] = {\n            \"1\": [],\n            \"2\": [\"a\", \"b\", \"c\"],\n            \"3\": [\"d\", \"e\", \"f\"],\n            \"4\": [\"g\", \"h\", \"i\"],\n            \"5\": [\"j\", \"k\", \"l\"],\n            \"6\": [\"m\", \"n\", \"o\"],\n            \"7\": [\"p\", \"q\", \"r\", \"s\"],\n            \"8\": [\"t\", \"u\", \"v\"],\n            \"9\": [\"w\", \"x\", \"y\", \"z\"],\n            \"0\": [\" \"]\n        }\n\n        current = []\n        \n        def backtrack(digit: int) -> Generator[None, None, str]:\n            if digit == length:\n                yield \"\".join(current[:])\n                return\n            \n            for char in digit_map[digits[digit]]:\n                current.append(char)\n                yield from backtrack(digit + 1)\n                current.pop()\n\n        return tuple(combination for combination in backtrack(0))","title":"Letter Combinations of a Phone Number","url":"/submissions/detail/1011037555/","lang_name":"Python3","time":"6 months","timestamp":1691055211,"status":10,"runtime":"43 ms","is_pending":"Not Pending","memory":"16.3 MB","compare_result":"1111111111111111111111111","has_notes":false,"flag_type":1}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        if length == 0:
            return []

        digit_map: Dict[int, str] = {
            "1": [],
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
            "0": [" "],
        }

        current = []

        def backtrack(digit: int) -> Generator[None, None, str]:
            if digit == length:
                yield "".join(current[:])
                return

            for char in digit_map[digits[digit]]:
                current.append(char)
                yield from backtrack(digit + 1)
                current.pop()

        return tuple(combination for combination in backtrack(0))
