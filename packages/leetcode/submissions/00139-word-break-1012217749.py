# Submission title: for Word Break
# Submission url  : https://leetcode.com/submissions/detail/1012217749/
# Submission json : {"id": 1012217749, "status_display": "Accepted", "lang": "python3", "question_id": 139, "title_slug": "word-break", "code": "class Solution:\n    def wordBreak(self, s: str, wordDict: List[str]) -> bool:\n\n        @cache\n        def calculate(i: int) -> bool:\n            if i < 0:\n                return True\n            \n            for word in wordDict:\n                length = len(word)\n                if s[i-length+1:i+1] == word and calculate(i-length):\n                    return True\n            \n            return False\n\n        return calculate(len(s) - 1)\n        \n", "title": "Word Break", "url": "/submissions/detail/1012217749/", "lang_name": "Python3", "time": "6\u00a0months", "timestamp": 1691167079, "status": 10, "runtime": "44 ms", "is_pending": "Not Pending", "memory": "16.6 MB", "compare_result": "1111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @cache
        def calculate(i: int) -> bool:
            if i < 0:
                return True

            for word in wordDict:
                length = len(word)
                if s[i - length + 1 : i + 1] == word and calculate(i - length):
                    return True

            return False

        return calculate(len(s) - 1)
