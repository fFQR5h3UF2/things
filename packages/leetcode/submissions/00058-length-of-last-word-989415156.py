# Submission title: for Length of Last Word
# Submission url  : https://leetcode.com/submissions/detail/989415156/
# Submission json : {"id": 989415156, "status_display": "Accepted", "lang": "python3", "question_id": 58, "title_slug": "length-of-last-word", "code": "class Solution:\n    # we need to iterate over the string searching for words\n    # possible combinations:\n    # 1. a whitespace after a symbol: end of the word\n    # 2. a whitespace after a whitespace: ignore\n    # 3. a symbol after a symbol, but it's the last symbol: end of the last word\n    # 4. a symbol after a symbol: ignore\n    def lengthOfLastWord(self, s: str) -> int:\n        length = len(s)\n        if length == 1:\n            return 1\n\n        word_start, word_end, in_word = 0, 0, False\n\n        for i, symbol in enumerate(s):\n            is_whitespace = symbol == \" \"\n            is_last = i == length - 1\n            \n            if is_whitespace and in_word:\n                in_word = False\n                word_end = i - 1\n                continue\n            \n            if is_whitespace and not in_word:\n                continue\n\n            if not is_whitespace and in_word and is_last:\n                word_end = i\n                continue\n\n            if not is_whitespace and not in_word and is_last:\n                word_end = i\n                word_start = i\n                continue\n\n            if not is_whitespace and in_word:\n                continue\n\n            if not is_whitespace and not in_word:\n                word_start = i\n                in_word = True\n                continue\n            \n        return word_end - word_start + 1", "title": "Length of Last Word", "url": "/submissions/detail/989415156/", "lang_name": "Python3", "time": "7\u00a0months", "timestamp": 1688831280, "status": 10, "runtime": "56 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "1111111111111111111111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    # we need to iterate over the string searching for words
    # possible combinations:
    # 1. a whitespace after a symbol: end of the word
    # 2. a whitespace after a whitespace: ignore
    # 3. a symbol after a symbol, but it's the last symbol: end of the last word
    # 4. a symbol after a symbol: ignore
    def lengthOfLastWord(self, s: str) -> int:
        length = len(s)
        if length == 1:
            return 1

        word_start, word_end, in_word = 0, 0, False

        for i, symbol in enumerate(s):
            is_whitespace = symbol == " "
            is_last = i == length - 1

            if is_whitespace and in_word:
                in_word = False
                word_end = i - 1
                continue

            if is_whitespace and not in_word:
                continue

            if not is_whitespace and in_word and is_last:
                word_end = i
                continue

            if not is_whitespace and not in_word and is_last:
                word_end = i
                word_start = i
                continue

            if not is_whitespace and in_word:
                continue

            if not is_whitespace and not in_word:
                word_start = i
                in_word = True
                continue

        return word_end - word_start + 1
