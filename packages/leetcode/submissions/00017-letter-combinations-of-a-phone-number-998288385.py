# Submission title: for Letter Combinations of a Phone Number
# Submission url  : https://leetcode.com/submissions/detail/998288385/
# Submission json : {"id": 998288385, "status_display": "Accepted", "lang": "python3", "question_id": 17, "title_slug": "letter-combinations-of-a-phone-number", "code": "class Solution:\n    def letterCombinations(self, digits: str) -> List[str]:\n        length = len(digits)\n        if length == 0:\n            return []\n        \n        digit_map: Dict[int, str] = {\n            1: [],\n            2: [\"a\", \"b\", \"c\"],\n            3: [\"d\", \"e\", \"f\"],\n            4: [\"g\", \"h\", \"i\"],\n            5: [\"j\", \"k\", \"l\"],\n            6: [\"m\", \"n\", \"o\"],\n            7: [\"p\", \"q\", \"r\", \"s\"],\n            8: [\"t\", \"u\", \"v\"],\n            9: [\"w\", \"x\", \"y\", \"z\"],\n            0: [\" \"]\n        }\n        result: List[List[str]] = [\n            digit_map[int(digit)] for digit in digits\n        ]\n        return [\"\".join(i) for i in product(*result)]", "title": "Letter Combinations of a Phone Number", "url": "/submissions/detail/998288385/", "lang_name": "Python3", "time": "6\u00a0months, 2\u00a0weeks", "timestamp": 1689755164, "status": 10, "runtime": "52 ms", "is_pending": "Not Pending", "memory": "16.3 MB", "compare_result": "1111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        length = len(digits)
        if length == 0:
            return []

        digit_map: Dict[int, str] = {
            1: [],
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"],
            0: [" "],
        }
        result: List[List[str]] = [digit_map[int(digit)] for digit in digits]
        return ["".join(i) for i in product(*result)]
