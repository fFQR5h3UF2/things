# Submission title: for Word Pattern
# Submission url  : https://leetcode.com/submissions/detail/995264601/
# Submission json : {"id": 995264601, "status_display": "Accepted", "lang": "python3", "question_id": 290, "title_slug": "word-pattern", "code": "class Solution:\n    def wordPattern(self, pattern: str, s: str) -> bool:\n        words = s.split()\n        words_length, pattern_length = len(words), len(pattern)\n\n        if words_length != pattern_length:\n            return False\n        \n        symbol_to_word = {}\n        word_to_symbol = {}\n\n        for i, symbol in enumerate(pattern):\n            word = words[i]\n            symbol_in, word_in = symbol in symbol_to_word, word in word_to_symbol\n\n            if symbol_in and word_in and symbol_to_word[symbol] == word:\n                continue\n\n            if not symbol_in and not word_in:\n                symbol_to_word[symbol] = word\n                word_to_symbol[word] = symbol\n                continue\n\n            return False\n        \n        return True\n            \n", "title": "Word Pattern", "url": "/submissions/detail/995264601/", "lang_name": "Python3", "time": "6\u00a0months, 3\u00a0weeks", "timestamp": 1689444696, "status": 10, "runtime": "57 ms", "is_pending": "Not Pending", "memory": "16.4 MB", "compare_result": "11111111111111111111111111111111111111111", "has_notes": false, "flag_type": 1}


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        words_length, pattern_length = len(words), len(pattern)

        if words_length != pattern_length:
            return False

        symbol_to_word = {}
        word_to_symbol = {}

        for i, symbol in enumerate(pattern):
            word = words[i]
            symbol_in, word_in = symbol in symbol_to_word, word in word_to_symbol

            if symbol_in and word_in and symbol_to_word[symbol] == word:
                continue

            if not symbol_in and not word_in:
                symbol_to_word[symbol] = word
                word_to_symbol[word] = symbol
                continue

            return False

        return True
